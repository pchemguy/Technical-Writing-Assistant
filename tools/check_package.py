"""Check repository links, routing coverage, and local presentation properties.

Run with Python 3.11 or newer. This read-only, standard-library checker supports
inline Markdown links, one-line string scalars and a two-space string metadata
mapping. Unsupported YAML is reported as unverified with a nonzero result.
It does not retrieve URLs, execute the skill, or judge prose.
"""

from collections import Counter
import json
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET


FRONTMATTER_FIELDS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
IMPLICIT_VALUES = {"null", "true", "false", "~", ".inf", "+.inf", "-.inf", ".nan"}
NUMBER = re.compile(r"[-+]?(?:0[xob][0-9a-f_]+|[0-9][0-9_]*(?:\.[0-9_]*)?(?:e[-+]?[0-9]+)?|\.[0-9]+(?:e[-+]?[0-9]+)?)$", re.I)


def string_scalar(value: str) -> str:
    """Read a supported YAML string; never coerce a nonstring into a string."""
    value = value.strip()
    if value.startswith('"'):
        try:
            parsed, end = json.JSONDecoder().raw_decode(value)
        except ValueError as error:
            raise ValueError("unsupported double-quoted scalar") from error
        remainder = value[end:]
        if not isinstance(parsed, str) or (remainder and not re.fullmatch(r"\s+#.*|\s+", remainder)):
            raise ValueError("unsupported quoted scalar suffix")
        return parsed
    if value.startswith("'"):
        match = re.fullmatch(r"'((?:[^']|'')*)'(?:\s+#.*)?", value)
        if not match:
            raise ValueError("unsupported single-quoted scalar")
        return match[1].replace("''", "'")
    value = re.split(r"\s+#", value, maxsplit=1)[0].rstrip()
    if (not value or value[0] in "[{>|&*!@`\"'" or value.startswith(("- ", "? ", ": "))
            or value.lower() in IMPLICIT_VALUES or NUMBER.fullmatch(value)
            or re.match(r"\d{4}-\d{2}-\d{2}(?:$|[Tt ])", value)
            or ": " in value or any(ord(char) < 32 for char in value)):
        raise ValueError("expected a one-line string scalar; unsupported or nonstring YAML")
    return value


def frontmatter_fields(text: str) -> dict:
    """Parse the documented subset, rejecting duplicates and unverified syntax."""
    fields = {}
    nested = False
    implicit_empty_metadata = False
    for line in text.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith("  "):
            match = re.fullmatch(r"  ([A-Za-z0-9_][\w.-]*):\s*(.*)", line)
            if not nested or not match:
                raise ValueError("unsupported nesting or indentation")
            key, value = match.groups()
            if key in fields["metadata"]:
                raise ValueError(f"duplicate metadata key: {key}")
            fields["metadata"][key] = string_scalar(value)
            continue
        match = re.fullmatch(r"([a-z][a-z-]*):\s*(.*)", line)
        if not match:
            raise ValueError("unsupported frontmatter line or indentation")
        key, value = match.groups()
        if key in fields:
            raise ValueError(f"duplicate frontmatter key: {key}")
        if key not in FRONTMATTER_FIELDS:
            raise ValueError(f"unsupported frontmatter field: {key}")
        nested = key == "metadata" and (not value.strip() or value.lstrip().startswith("#"))
        if key == "metadata":
            if not nested and not re.fullmatch(r"\{\}(?:\s+#.*)?", value.strip()):
                raise ValueError("metadata must be a string mapping")
            fields[key] = {}
            implicit_empty_metadata = nested
        else:
            fields[key] = string_scalar(value)
    if implicit_empty_metadata and not fields["metadata"]:
        raise ValueError("metadata has no mapping entries; use metadata: {} for an empty mapping")
    return fields


def anchors(text: str) -> set[str]:
    """Return GitHub-style anchors for the plain headings used in this project."""
    seen: Counter[str] = Counter()
    result: set[str] = set()
    for heading in re.findall(r"^#{1,6}\s+(.+)$", text, re.MULTILINE):
        base = re.sub(r"[^\w\- ]", "", heading.lower()).replace(" ", "-")
        count = seen[base]
        result.add(f"{base}-{count}" if count else base)
        seen[base] += 1
    return result


def check(root: Path) -> tuple[list[str], int, int]:
    """Return errors and inspected link/reference counts for this repository.

    Args:
        root: Repository directory containing the skill and capability map.

    Returns:
        Error messages, count of local Markdown links, and reference count.
    """
    errors: list[str] = []
    link_count = 0
    skill = root / "technical-writing-assistant"
    entry_path = skill / "SKILL.md"
    if not entry_path.is_file():
        return ["Missing skill entry point"], 0, 0
    entry = entry_path.read_text(encoding="utf-8")
    front = re.match(r"\A---\n(.*?)\n---\n", entry, re.DOTALL)
    if not front:
        errors.append("Missing frontmatter delimiters")
    else:
        try:
            fields = frontmatter_fields(front[1])
        except ValueError as error:
            errors.append(f"Frontmatter invalid or unverified: {error}")
        else:
            if fields.get("name") != skill.name:
                errors.append("Skill name missing or does not match its directory")
            if not 1 <= len(fields.get("description", "")) <= 1024:
                errors.append("Description missing or length outside supported range")
            if len(fields.get("compatibility", "")) > 500:
                errors.append("Compatibility length outside supported range")
    references = {p.name for p in (skill / "references").glob("*.md")}
    routed = set(re.findall(r"\]\(references/([^)#]+\.md)(?:#[^)]*)?\)", entry))
    if routed != references:
        errors.append(f"Routing mismatch: missing={sorted(references-routed)}, extra={sorted(routed-references)}")
    map_path = root / "docs/dev/CAPABILITY_MAP.md"
    if map_path.is_file():
        declared = set(re.findall(r"^\| `([^`]+\.md)` \|", map_path.read_text(encoding="utf-8"), re.MULTILINE))
        if declared != references:
            errors.append("Capability-map references disagree with package inventory")
    else:
        errors.append("Missing governing capability map")
    for path in sorted(root.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if path.is_relative_to(skill) and re.search(
            r"Implementation work remaining|Status:.*(?:skeleton|scaffold)", text
        ):
            errors.append(f"Implementation scaffold remains: {path.relative_to(root)}")
        for target in re.findall(r"!?\[[^\]\n]*\]\(([^)\n]+)\)", text):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            link_count += 1
            file_part, _, fragment = target.partition("#")
            destination = (path.parent / file_part).resolve() if file_part else path
            if not destination.is_relative_to(root):
                errors.append(f"Link escapes repository: {path.relative_to(root)} -> {target}")
            elif not destination.exists():
                errors.append(f"Missing link target: {path.relative_to(root)} -> {target}")
            elif fragment and (not destination.is_file() or fragment not in anchors(destination.read_text(encoding="utf-8"))):
                errors.append(f"Missing anchor: {path.relative_to(root)} -> {target}")
    metadata = skill / "agents/openai.yaml"
    if metadata.is_file():
        values = {}
        for key, value in re.findall(r'^  ([a-z_]+): (".*")$', metadata.read_text(encoding="utf-8"), re.MULTILINE):
            try:
                values[key] = json.loads(value)
            except ValueError:
                errors.append(f"Invalid quoted presentation scalar: {key}")
        if not 25 <= len(values.get("short_description", "")) <= 64:
            errors.append("Invalid presentation summary length")
        if "$technical-writing-assistant" not in values.get("default_prompt", ""):
            errors.append("Presentation prompt lacks skill invocation")
        for key in ("icon_small", "icon_large"):
            if values.get(key) != "./assets/icon.svg":
                errors.append(f"Unexpected local icon path: {key}")
    else:
        errors.append("Missing optional presentation component advertised by repository")
    try:
        icon = ET.parse(skill / "assets/icon.svg").getroot()
        if icon.tag != "{http://www.w3.org/2000/svg}svg":
            errors.append("Icon root is not SVG")
        for element in icon.iter():
            if element.tag.endswith("script") or any("href" in key and not value.startswith("#") for key, value in element.attrib.items()):
                errors.append("Icon contains executable or external content")
    except (OSError, ET.ParseError):
        errors.append("Icon missing or invalid XML")
    return errors, link_count, len(references)


def main() -> int:
    """Print structural results and exit nonzero for errors."""
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors, links, references = check(root)
    for error in errors:
        print(f"ERROR: {error}")
    print(f"Checked {references} references and {links} local Markdown links; {len(errors)} errors.")
    print("Scope: local structural checks; runtime and external URLs not assessed.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
