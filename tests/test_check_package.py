"""Regression contracts for the repository checker, using isolated packages."""

from pathlib import Path
import shutil

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
