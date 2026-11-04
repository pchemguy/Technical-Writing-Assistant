"""Run current-source structural, routing, recipe, negative-fixture, and whitespace checks for campaign 006_f2000ee."""

from __future__ import annotations

import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

REPO_ROOT = Path(__file__).resolve().parents[5]
sys.dont_write_bytecode = True
sys.path.insert(0, str(REPO_ROOT / "tools"))
import check_package  # noqa: E402

CURRENT_ROOT_DOCS = [
    "AGENTS.md",
    "AI_DISCLOSURE.md",
    "README.md",
    "SDD-MANAGER.md",
    "SKILL_DISCOVERY_PROTOCOL.md",
    "WINDOWS_SHELL_POLICY.md",
]

CURRENT_DEV_DOCS = [
    "docs/dev/CAPABILITY_MAP.md",
    "docs/dev/HANDOFF.md",
    "docs/dev/PLAN.md",
    "docs/dev/SPEC.md",
    "docs/dev/reviews/006_f2000ee-comprehensive-skill-review/REVIEW-PLAN.md",
    "docs/dev/reviews/006_f2000ee-comprehensive-skill-review/REVIEW-REPORT.md",
    "docs/dev/reviews/006_f2000ee-comprehensive-skill-review/evidence/check_current.py",
    "docs/dev/reviews/006_f2000ee-comprehensive-skill-review/evidence/consumer-a.md",
    "docs/dev/reviews/006_f2000ee-comprehensive-skill-review/evidence/consumer-b.md",
    "docs/dev/reviews/006_f2000ee-comprehensive-skill-review/independent/consumer-assessment.md",
    "docs/dev/reviews/006_f2000ee-comprehensive-skill-review/independent/editorial.md",
    "docs/dev/reviews/006_f2000ee-comprehensive-skill-review/independent/interfaces.md",
]

CURRENT_EVIDENCE_ASSETS = [
    "docs/dev/reviews/006_f2000ee-comprehensive-skill-review/evidence/icon-128.png",
    "docs/dev/reviews/006_f2000ee-comprehensive-skill-review/evidence/icon-32.png",
    "docs/dev/reviews/006_f2000ee-comprehensive-skill-review/evidence/structural-results.json",
]

HISTORICAL_PLACEHOLDERS = [
    "docs/dev/REVIEW.md",
    "docs/dev/REVISION_REVIEW.md",
    "docs/dev/revision_plans/REVISION_PLAN_1cc08a2.md",
]


def build_current_fixture(dest: Path) -> None:
    """Populate a bounded current-source fixture excluding closed historical records and .agents."""
    for rel in CURRENT_ROOT_DOCS + CURRENT_DEV_DOCS + CURRENT_EVIDENCE_ASSETS:
        src = REPO_ROOT / rel
        if not src.exists():
            continue
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, target)
    for rel in HISTORICAL_PLACEHOLDERS:
        target = dest / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("", encoding="utf-8")
    shutil.copytree(REPO_ROOT / "technical-writing-assistant", dest / "technical-writing-assistant")
    (dest / "tools").mkdir(parents=True, exist_ok=True)
    shutil.copy2(REPO_ROOT / "tools/check_package.py", dest / "tools/check_package.py")


def extract_table_rows(markdown: str, header_prefix: str) -> list[tuple[str, ...]]:
    """Extract pipe-table rows following a specific header line."""
    lines = markdown.splitlines()
    rows: list[tuple[str, ...]] = []
    in_table = False
    for line in lines:
        if line.strip().startswith(header_prefix):
            in_table = True
            continue
        if in_table:
            if not line.strip().startswith("|"):
                break
            if re.match(r"^\|\s*---", line.strip()):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.append(tuple(cells))
    return rows


def main() -> int:
    evidence_dir = Path(__file__).resolve().parent
    results: dict[str, object] = {}

    with tempfile.TemporaryDirectory() as tmp:
        fixture = Path(tmp) / "current"
        build_current_fixture(fixture)
        errors, link_count, ref_count = check_package.check(fixture)
        results["current_source_fixture"] = {
            "errors": errors,
            "link_count": link_count,
            "reference_count": ref_count,
            "included_root_docs": CURRENT_ROOT_DOCS,
            "included_dev_docs": CURRENT_DEV_DOCS,
            "historical_existence_placeholders": HISTORICAL_PLACEHOLDERS,
        }

        # Negative fixture 1: missing routed reference
        neg_missing = Path(tmp) / "neg_missing"
        shutil.copytree(fixture, neg_missing)
        (neg_missing / "technical-writing-assistant/references/language-revision.md").unlink()
        neg1_errors, _, _ = check_package.check(neg_missing)

        # Negative fixture 2: broken heading anchor
        neg_anchor = Path(tmp) / "neg_anchor"
        shutil.copytree(fixture, neg_anchor)
        skill_md = neg_anchor / "technical-writing-assistant/SKILL.md"
        skill_md.write_text(
            skill_md.read_text(encoding="utf-8") + "\nSee [broken](references/manager.md#missing-anchor).\n",
            encoding="utf-8",
        )
        neg2_errors, _, _ = check_package.check(neg_anchor)

        # Negative fixture 3: link escaping repository
        neg_escape = Path(tmp) / "neg_escape"
        shutil.copytree(fixture, neg_escape)
        skill_md_esc = neg_escape / "technical-writing-assistant/SKILL.md"
        skill_md_esc.write_text(
            skill_md_esc.read_text(encoding="utf-8") + "\nSee [escape](../../outside.md).\n",
            encoding="utf-8",
        )
        neg3_errors, _, _ = check_package.check(neg_escape)

        results["negative_fixtures"] = {
            "missing_reference": neg1_errors,
            "broken_anchor": neg2_errors,
            "escaping_link": neg3_errors,
        }

    # APA validators
    apa_val = subprocess.run(
        [sys.executable, str(REPO_ROOT / ".agents/skills/agent-package-author/scripts/validate_skill.py"), str(REPO_ROOT / "technical-writing-assistant")],
        capture_output=True,
        text=True,
        check=False,
    )
    apa_insp = subprocess.run(
        [sys.executable, str(REPO_ROOT / ".agents/skills/agent-package-author/scripts/inspect_package.py"), str(REPO_ROOT / "technical-writing-assistant")],
        capture_output=True,
        text=True,
        check=False,
    )
    results["apa_checks"] = {
        "validate_skill_returncode": apa_val.returncode,
        "validate_skill_stdout": apa_val.stdout.strip(),
        "validate_skill_stderr": apa_val.stderr.strip(),
        "inspect_package_returncode": apa_insp.returncode,
        "inspect_package_stdout": apa_insp.stdout.strip(),
    }

    # Routing and recipe parity
    skill_text = (REPO_ROOT / "technical-writing-assistant/SKILL.md").read_text(encoding="utf-8")
    manager_text = (REPO_ROOT / "technical-writing-assistant/references/manager.md").read_text(encoding="utf-8")
    map_text = (REPO_ROOT / "docs/dev/CAPABILITY_MAP.md").read_text(encoding="utf-8")

    actual_refs = sorted(p.name for p in (REPO_ROOT / "technical-writing-assistant/references").glob("*.md"))
    routed_in_skill = sorted(set(re.findall(r"\]\(references/([^)#]+\.md)(?:#[^)]*)?\)", skill_text)))
    table_routes = extract_table_rows(skill_text, "| Need | Reference |")
    map_decomp_rows = extract_table_rows(map_text, "| Reference | Scope and outputs | Boundary |")
    manager_recipes = extract_table_rows(manager_text, "| Workflow | Typical sequence | Result |")
    map_recipes = extract_table_rows(map_text, "| Workflow | Typical sequence | Result |")

    results["routing_and_recipes"] = {
        "actual_reference_count": len(actual_refs),
        "routed_in_skill_count": len(routed_in_skill),
        "skill_table_row_count": len(table_routes),
        "map_decomposition_row_count": len(map_decomp_rows),
        "manager_recipe_count": len(manager_recipes),
        "map_recipe_count": len(map_recipes),
        "recipes_identical": manager_recipes == map_recipes,
        "recipe_names": [r[0] for r in manager_recipes],
    }

    # File metrics and whitespace check
    runtime_files = ["technical-writing-assistant/SKILL.md"] + [
        f"technical-writing-assistant/references/{name}" for name in actual_refs
    ]
    support_files = [
        "technical-writing-assistant/agents/openai.yaml",
        "technical-writing-assistant/assets/icon.svg",
        "tools/check_package.py",
    ] + CURRENT_ROOT_DOCS + CURRENT_DEV_DOCS

    metrics: dict[str, dict[str, int]] = {}
    whitespace_issues: list[str] = []
    for rel in runtime_files + support_files:
        p = REPO_ROOT / rel
        raw = p.read_bytes()
        text = raw.decode("utf-8")
        lines = text.splitlines()
        metrics[rel] = {
            "lines": len(lines),
            "words": len(text.split()),
            "bytes": len(raw),
        }
        if not text.endswith("\n"):
            whitespace_issues.append(f"{rel}: missing final newline")
        for idx, line in enumerate(lines, 1):
            if line.endswith((" ", "\t")):
                whitespace_issues.append(f"{rel}:{idx}: trailing whitespace")
            if "\t" in line:
                whitespace_issues.append(f"{rel}:{idx}: tab character")

    results["file_metrics"] = metrics
    results["whitespace_issues"] = whitespace_issues

    # Render icon.svg at 128x128 and 32x32 using PySide6.QtSvg if available
    icon_render: dict[str, object] = {"rendered": False}
    try:
        from PySide6.QtCore import QSize, Qt
        from PySide6.QtGui import QGuiApplication, QImage, QPainter
        from PySide6.QtSvg import QSvgRenderer

        app = QGuiApplication.instance() or QGuiApplication([])
        svg_path = REPO_ROOT / "technical-writing-assistant/assets/icon.svg"
        renderer = QSvgRenderer(str(svg_path))
        if renderer.isValid():
            outputs: dict[str, str] = {}
            for size in (128, 32):
                image = QImage(QSize(size, size), QImage.Format.Format_ARGB32)
                image.fill(Qt.GlobalColor.transparent)
                painter = QPainter(image)
                renderer.render(painter)
                painter.end()
                out_png = evidence_dir / f"icon-{size}.png"
                image.save(str(out_png), "PNG")
                outputs[f"{size}x{size}"] = str(out_png.relative_to(REPO_ROOT)).replace("\\", "/")
            icon_render = {
                "rendered": True,
                "engine": "PySide6.QtSvg.QSvgRenderer",
                "outputs": outputs,
            }
        del app
    except Exception as exc:  # pragma: no cover
        icon_render = {"rendered": False, "reason": str(exc)}

    results["icon_render"] = icon_render

    out_path = evidence_dir / "structural-results.json"
    out_path.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out_path.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
