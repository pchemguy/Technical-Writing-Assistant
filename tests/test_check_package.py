"""Regression contracts for the repository checker, using isolated packages."""

from pathlib import Path
import shutil
import subprocess
import sys

import pytest

from tools import check_package


@pytest.fixture
def project(tmp_path):
    """Build a real package with minimal, nonhistorical governing documents."""
    root = tmp_path / "repo"
    source = Path(__file__).resolve().parents[1]
    shutil.copytree(source / "technical-writing-assistant", root / "technical-writing-assistant")
    dev = root / "docs/dev"
    dev.mkdir(parents=True)
    refs = sorted((root / "technical-writing-assistant/references").glob("*.md"))
    (dev / "CAPABILITY_MAP.md").write_text(
        "# Capabilities\n\n| Reference |\n| --- |\n" +
        "".join(f"| `{ref.name}` |\n" for ref in refs), encoding="utf-8")
    return root


def set_frontmatter(root, fields):
    entry = root / "technical-writing-assistant/SKILL.md"
    body = entry.read_text(encoding="utf-8").partition("\n---\n")[2]
    entry.write_text("---\n" + fields + "\n---\n" + body, encoding="utf-8")


BASE = "name: technical-writing-assistant\ndescription: Review technical writing."


def test_current_package_is_valid(project):
    errors, _, references = check_package.check(project)
    assert errors == []
    assert references == 20


@pytest.mark.parametrize("extra", [
    "license: MIT",
    "compatibility: Python 3.11+",
    "allowed-tools: Read Grep",
    "metadata:\n  aliases: '[\"TWA\", \"twa\"]'\n  author: PChemGuy",
    "metadata:\n  empty: ''\n  quoted: \"true\"\n  url: https://example.invalid/target#fragment",
    "metadata: {}",
])
def test_supported_optional_string_fields_are_valid(project, extra):
    set_frontmatter(project, BASE + "\n" + extra)
    assert check_package.check(project)[0] == []


def test_quoted_required_fields_and_comments_are_valid(project):
    set_frontmatter(project, 'name: "technical-writing-assistant" # package\n'
                    "description: 'Review: preserve the author''s meaning.'")
    assert check_package.check(project)[0] == []


@pytest.mark.parametrize("fields", [
    BASE + "\nname: technical-writing-assistant",
    "name: wrong\n" + BASE,
    BASE + "\ndescription: Repeated",
    BASE + "\nmetadata:\n  author: A\n  author: B",
    BASE + "\nmetadata: {}\nmetadata: {}",
])
def test_duplicate_keys_are_errors(project, fields):
    set_frontmatter(project, fields)
    assert any("duplicate" in error.lower() for error in check_package.check(project)[0])


@pytest.mark.parametrize("value", ['["TWA", "twa"]', "true", "12", "null", "|", "2026-11-05"])
def test_nonstring_or_unhandled_metadata_is_not_a_clean_pass(project, value):
    set_frontmatter(project, BASE + "\nmetadata:\n  aliases: " + value)
    assert check_package.check(project)[0]


@pytest.mark.parametrize("fields", [
    "name: technical-writing-assistant\ndescription: |\n  Multiline description",
    BASE + "\nmetadata:\n  nested:\n    child: value",
    BASE + "\nmetadata: [not, a, mapping]",
    BASE + "\nunknown:\n  nested: value",
    "name: technical-writing-assistant\ndescription: true",
    "name: technical-writing-assistant",
    BASE + "\ncompatibility: " + "x" * 501,
])
def test_invalid_or_unsupported_frontmatter_fails_explicitly(project, fields):
    set_frontmatter(project, fields)
    assert check_package.check(project)[0]


def test_missing_reference_is_still_detected(project):
    (project / "technical-writing-assistant/references/language-revision.md").unlink()
    assert any("Routing mismatch" in error for error in check_package.check(project)[0])


def test_broken_anchor_is_still_detected(project):
    entry = project / "technical-writing-assistant/SKILL.md"
    entry.write_text(entry.read_text() + "\n[Bad](references/manager.md#no-such-heading)\n")
    assert any("Missing anchor" in error for error in check_package.check(project)[0])


def test_escaping_link_is_still_detected(project):
    entry = project / "technical-writing-assistant/SKILL.md"
    entry.write_text(entry.read_text() + "\n[Bad](../../outside.md)\n")
    assert any("Link escapes repository" in error for error in check_package.check(project)[0])


def write_doc(root, relative, text):
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def cli(root, *args):
    script = Path(check_package.__file__)
    return subprocess.run([sys.executable, str(script), str(root), *args],
                          capture_output=True, text=True, check=False)


@pytest.mark.parametrize("relative", [
    "docs/dev/reviews/001_closed/REVIEW-REPORT.md",
    "docs/dev/features/001_closed/FEATURE.md",
    "docs/dev/reports/phases/001/REPORT.md",
    "docs/dev/revision_plans/old.md",
    "docs/dev/validation/old.md",
    "docs/dev/REVIEW.md",
    "docs/dev/REVISION_REVIEW.md",
    ".agents/skills/unrelated/SKILL.md",
])
def test_default_current_mode_excludes_retained_and_tool_records(project, relative):
    write_doc(project, relative, "[Historical](missing.md)\n")
    assert check_package.check(project)[0] == []


def test_active_campaign_is_checked_without_inactive_campaign(project):
    active = "docs/dev/reviews/008_active"
    write_doc(project, active + "/REVIEW-REPORT.md", "[Active](missing-active.md)\n")
    write_doc(project, "docs/dev/reviews/001_closed/REVIEW-REPORT.md", "[Old](missing-old.md)\n")
    errors = check_package.check(project, active_campaigns=[active])[0]
    assert any("missing-active.md" in error for error in errors)
    assert not any("missing-old.md" in error for error in errors)


def test_cli_current_scope_accepts_explicit_valid_active_campaign(project):
    active = "docs/dev/reviews/008_active"
    write_doc(project, active + "/REVIEW-REPORT.md", "# Current report\n")
    write_doc(project, "docs/dev/reviews/001_closed/REVIEW-REPORT.md", "[Old](missing.md)\n")
    result = cli(project, "--active-campaign", active)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "Scope: current" in result.stdout


def test_current_document_errors_are_not_excluded(project):
    write_doc(project, "docs/guide.md", "[Current](missing-current.md)\n")
    result = cli(project)
    assert result.returncode == 1
    assert "missing-current.md" in result.stdout


def test_archived_link_fragment_is_existence_only_without_content_read(project):
    old = project / "docs/dev/reviews/001_closed/REVIEW-REPORT.md"
    old.parent.mkdir(parents=True)
    original = b"\xffinvalid utf8: must not be read"
    old.write_bytes(original)
    write_doc(project, "README.md", "[History](docs/dev/reviews/001_closed/REVIEW-REPORT.md#old-heading)\n")
    assert check_package.check(project)[0] == []
    assert old.read_bytes() == original


def test_missing_historical_target_is_still_a_current_link_error(project):
    write_doc(project, "README.md", "[History](docs/dev/reviews/001_closed/missing.md)\n")
    assert any("Missing link target" in error for error in check_package.check(project)[0])


def test_all_scope_is_explicit_and_detects_retained_record_errors(project):
    write_doc(project, "docs/dev/reviews/001_closed/REVIEW-REPORT.md", "[Old](missing.md)\n")
    result = cli(project, "--scope", "all")
    assert result.returncode == 1
    assert "Scope: all" in result.stdout and "missing.md" in result.stdout


@pytest.mark.parametrize("selection", ["../outside", "docs/dev", "docs/dev/reviews/missing"])
def test_cli_rejects_nonexistent_or_uncontained_campaign_selection(project, selection):
    result = cli(project, "--active-campaign", selection)
    assert result.returncode == 2
    assert "error:" in result.stderr


def test_cli_rejects_unknown_flags(project):
    assert cli(project, "--no-such-option").returncode == 2


def test_all_scope_rejects_ambiguous_active_selection(project):
    active = "docs/dev/reviews/008_active"
    write_doc(project, active + "/REVIEW-REPORT.md", "# Active\n")
    assert cli(project, "--scope", "all", "--active-campaign", active).returncode == 2
