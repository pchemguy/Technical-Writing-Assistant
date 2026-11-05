"""Reproduce campaign 008 structural observations without scanning closed records."""

import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[5]
CAMPAIGN = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import check_package

ROOT_DOCS = ["AGENTS.md", "README.md", "SDD-MANAGER.md", "AI_DISCLOSURE.md"]
DEV_DOCS = ["docs/dev/SPEC.md", "docs/dev/CAPABILITY_MAP.md", "docs/dev/PLAN.md",
            "docs/dev/HANDOFF.md"]
HISTORICAL_TARGETS = ["docs/dev/REVIEW.md", "docs/dev/REVISION_REVIEW.md",
                      "docs/dev/revision_plans/REVISION_PLAN_1cc08a2.md"]
BASELINE = "fecf8cc097c9bccc78c0ac29676d397a1fefaa15"


def fixture(destination):
    """Copy current inputs and active records; retain historical existence only."""
    shutil.copytree(ROOT / "technical-writing-assistant",
                    destination / "technical-writing-assistant")
    members = [ROOT / p for p in ROOT_DOCS + DEV_DOCS + ["tools/check_package.py"]]
    members.extend(p for p in CAMPAIGN.rglob("*") if p.is_file())
    for source in members:
        target = destination / source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    for rel in HISTORICAL_TARGETS:
        target = destination / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text("", encoding="utf-8")


def recipe_rows(text):
    """Extract this project's simple recipe table, retaining all cell content."""
    tail = text.split("| Workflow | Typical sequence | Result |", 1)[1]
    rows = []
    for line in tail.splitlines()[1:]:
        if not line.startswith("|"):
            break
        if re.match(r"\|\s*-", line):
            continue
        rows.append([cell.strip() for cell in line.strip("|").split("|")])
    return rows


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apa-scripts", required=True, type=Path)
    args = parser.parse_args()
    sys.path.insert(0, str(args.apa_scripts.resolve()))
    from validate_skill import validate_skill

    results = {"baseline": BASELINE, "python": sys.version.split()[0],
               "method": "Offline structure and synthetic fixtures; no agent/client execution",
               "historical_existence_placeholders": HISTORICAL_TARGETS}
    results["apa"] = []
    for script in ["validate_skill.py", "inspect_package.py"]:
        run = subprocess.run([sys.executable, str(args.apa_scripts / script),
                              str(ROOT / "technical-writing-assistant")],
                             capture_output=True, text=True, check=False)
        results["apa"].append({"script": script, "exit": run.returncode,
                               "stdout": run.stdout.strip(), "stderr": run.stderr.strip()})

    with tempfile.TemporaryDirectory() as temporary:
        base = Path(temporary) / "current"
        fixture(base)
        errors, links, references = check_package.check(base)
        results["current"] = {"errors": errors, "local_links": links, "references": references}
        cases = {}
        mutations = {
            "missing_reference": lambda p: (p / "technical-writing-assistant/references/language-revision.md").unlink(),
            "broken_anchor": lambda p: append_entry(p, "\nSee [anchor](references/manager.md#absent-campaign008-anchor).\n"),
            "escaping_link": lambda p: append_entry(p, "\nSee [outside](../../outside-campaign008.md).\n"),
            "duplicate_name": lambda p: replace_entry(p, "name: technical-writing-assistant", "name: incorrect-name\nname: technical-writing-assistant"),
            "nonstring_aliases": lambda p: replace_entry(p, "aliases: '[\"TWA\", \"twa\"]'", "aliases: [\"TWA\", \"twa\"]"),
            "valid_optional_license": lambda p: replace_entry(p, "metadata:\n", "license: MIT\nmetadata:\n"),
            "synthetic_closed_record": lambda p: synthetic_history(p),
        }
        for name, mutate in mutations.items():
            path = Path(temporary) / name
            shutil.copytree(base, path)
            mutate(path)
            found, count, refs = check_package.check(path)
            cases[name] = {"checker_errors": found, "local_links": count, "references": refs}
            if name in {"duplicate_name", "nonstring_aliases", "valid_optional_license"}:
                issues = []
                for issue in validate_skill(path / "technical-writing-assistant"):
                    record = asdict(issue)
                    record["path"] = str(Path(issue.path).relative_to(path))
                    issues.append(record)
                cases[name]["apa_issues"] = issues
        results["synthetic_cases"] = cases

    runtime = sorted((ROOT / "technical-writing-assistant").rglob("*"))
    inspected = [p for p in runtime if p.is_file()]
    inspected += [ROOT / p for p in ROOT_DOCS + DEV_DOCS + ["tools/check_package.py"]]
    results["inventory"] = []
    for path in inspected:
        raw = path.read_bytes()
        results["inventory"].append({"path": str(path.relative_to(ROOT)),
                                      "bytes": len(raw), "words": len(raw.decode().split()),
                                      "lines": len(raw.decode().splitlines()),
                                      "sha256": hashlib.sha256(raw).hexdigest()})
    manager = (ROOT / "technical-writing-assistant/references/manager.md").read_text()
    mapping = (ROOT / "docs/dev/CAPABILITY_MAP.md").read_text()
    recipes = recipe_rows(manager)
    results["recipes"] = {"manager": len(recipes), "map": len(recipe_rows(mapping)),
                           "identical": recipes == recipe_rows(mapping)}
    style = (ROOT / "technical-writing-assistant/references/style-guidelines.md").read_text()
    shared_style = style.split("### Mechanics and grammar", 1)[1].split("## Optional handoffs", 1)[0].strip()
    mapped_style = mapping.split("### Mechanics and grammar", 1)[1].split("## Module contracts and coupling", 1)[0].strip()
    results["shared_style_identical"] = shared_style == mapped_style
    results["metadata"] = {"note": "aliases is intentionally a JSON-encoded string, not a YAML sequence"}
    checks = {
        "current_clean": not errors and references == 20,
        "apa_clean": all(r["exit"] == 0 for r in results["apa"]),
        "recipe_parity": results["recipes"]["identical"] and len(recipes) == 17,
        "shared_style_parity": results["shared_style_identical"],
        "missing_reference_detected": any("Routing mismatch" in e for e in cases["missing_reference"]["checker_errors"]),
        "broken_anchor_detected": any("Missing anchor" in e for e in cases["broken_anchor"]["checker_errors"]),
        "escape_detected": any("Link escapes repository" in e for e in cases["escaping_link"]["checker_errors"]),
        "duplicate_false_accept_reproduced": not cases["duplicate_name"]["checker_errors"] and bool(cases["duplicate_name"]["apa_issues"]),
        "metadata_false_accept_reproduced": not cases["nonstring_aliases"]["checker_errors"] and bool(cases["nonstring_aliases"]["apa_issues"]),
        "optional_field_false_reject_reproduced": bool(cases["valid_optional_license"]["checker_errors"]) and not cases["valid_optional_license"]["apa_issues"],
        "closed_record_scope_problem_reproduced": any("not-a-current-target.md" in e for e in cases["synthetic_closed_record"]["checker_errors"]),
    }
    results["observation_assertions"] = checks
    results["all_observation_assertions_passed"] = all(checks.values())
    output = Path(__file__).resolve().parent / "structural-results.json"
    output.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"current": results["current"], "recipes": results["recipes"],
                      "observation_assertions": checks, "output": str(output.relative_to(ROOT))}, indent=2))
    return 0 if all(checks.values()) else 1


def append_entry(path, text):
    entry = path / "technical-writing-assistant/SKILL.md"
    entry.write_text(entry.read_text() + text)


def replace_entry(path, before, after):
    entry = path / "technical-writing-assistant/SKILL.md"
    text = entry.read_text()
    assert before in text
    entry.write_text(text.replace(before, after, 1))


def synthetic_history(path):
    record = path / "docs/dev/reviews/000_synthetic-closed/REVIEW-REPORT.md"
    record.parent.mkdir(parents=True)
    record.write_text("# Synthetic historical record\n\n[Historical reference](not-a-current-target.md)\n")


if __name__ == "__main__":
    raise SystemExit(main())
