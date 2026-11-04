"""Reproduce campaign 005 current-source structural checks without modifying source."""
from pathlib import Path
from tempfile import TemporaryDirectory
import importlib.util
import json
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[5]
CAMPAIGN = Path(__file__).resolve().parents[1]
BASELINE = '0ef087801f826d749c791f4116012930dcddfce7'
CURRENT = ['README.md', 'AGENTS.md', 'SDD-MANAGER.md', 'AI_DISCLOSURE.md',
           'WINDOWS_SHELL_POLICY.md', 'SKILL_DISCOVERY_PROTOCOL.md', 'docs/dev/HANDOFF.md',
           'docs/dev/SPEC.md', 'docs/dev/PLAN.md', 'docs/dev/CAPABILITY_MAP.md', 'tools/check_package.py']
HISTORY = {'docs/dev/REVIEW.md', 'docs/dev/REVISION_REVIEW.md',
           'docs/dev/revision_plans/REVISION_PLAN_1cc08a2.md'}
runtime = sorted(p for p in (ROOT / 'technical-writing-assistant').rglob('*') if p.is_file())

def recipes(path):
    return [line for line in path.read_text().splitlines()
            if line.startswith('| ') and len(line.split('|')) == 5 and '→' in line]

manager = recipes(ROOT / 'technical-writing-assistant/references/manager.md')
capability = recipes(ROOT / 'docs/dev/CAPABILITY_MAP.md')
assert len(manager) == len(capability) == 17 and manager == capability
result = {'baseline': BASELINE, 'runtime_files': len(runtime), 'recipe_rows': 17,
          'recipe_rows_equal': True,
          'runtime_markdown_words': sum(len(p.read_text().split()) for p in runtime if p.suffix == '.md'),
          'word_counts': {str(p.relative_to(ROOT)): len(p.read_text().split()) for p in runtime},
          'root_policy_words': {name: len((ROOT / name).read_text().split())
                                for name in ['AGENTS.md', 'SKILL_DISCOVERY_PROTOCOL.md', 'WINDOWS_SHELL_POLICY.md']}}
with TemporaryDirectory(prefix='twa-review005-') as temporary:
    fixture = Path(temporary)
    files = [ROOT / name for name in CURRENT] + runtime
    files += sorted(p for p in CAMPAIGN.rglob('*') if p.is_file() and '__pycache__' not in p.parts)
    for source in files:
        target = fixture / source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    placeholders = set()
    for source in files:
        if source.suffix != '.md':
            continue
        for link in re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)', source.read_text()):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', link):
                continue
            part, _, anchor = link.partition('#')
            original = (source.parent / part).resolve() if part else source
            if original.is_relative_to(ROOT) and original.relative_to(ROOT).as_posix() in HISTORY:
                assert original.is_file() and not anchor
                target = fixture / original.relative_to(ROOT)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.touch()
                placeholders.add(original.relative_to(ROOT).as_posix())
    spec = importlib.util.spec_from_file_location('campaign005_checker', fixture / 'tools/check_package.py')
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    errors, links, references = checker.check(fixture)
    result['positive'] = {'references': references, 'local_links': links, 'errors': errors,
                          'selected_markdown_files': sum(p.suffix == '.md' for p in files),
                          'existence_only_placeholders': sorted(placeholders)}
    assert not errors, errors
    missing = fixture / 'technical-writing-assistant/references/writing-brief.md'
    saved = missing.read_bytes()
    missing.unlink()
    negative, _, _ = checker.check(fixture)
    assert any('Routing mismatch' in error for error in negative)
    result['missing_resource'] = {'errors': negative, 'count': len(negative)}
    missing.write_bytes(saved)
    entry = fixture / 'technical-writing-assistant/SKILL.md'
    saved_entry = entry.read_text()
    entry.write_text(saved_entry.replace('(references/manager.md)', '(references/manager.md#missing-review005-anchor)', 1))
    negative, _, _ = checker.check(fixture)
    assert len(negative) == 1 and 'Missing anchor' in negative[0]
    result['broken_anchor'] = {'errors': negative, 'count': len(negative)}
    entry.write_text(saved_entry)
    assert not checker.check(fixture)[0]
changed = subprocess.check_output(['git', 'diff', '--name-only', BASELINE], cwd=ROOT, text=True).splitlines()
untracked = subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard'], cwd=ROOT, text=True).splitlines()
allowed_prefix = CAMPAIGN.relative_to(ROOT).as_posix() + '/'
assert all(p == 'docs/dev/HANDOFF.md' or p.startswith(allowed_prefix) for p in changed + untracked)
subprocess.run(['git', 'diff', '--check'], cwd=ROOT, check=True)
result['source_preservation'] = 'Only HANDOFF and campaign 005 records differ; runtime/current source and all closed records unchanged.'
print(json.dumps(result, indent=2))
