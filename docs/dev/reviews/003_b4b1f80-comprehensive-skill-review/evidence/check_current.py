"""Reproduce campaign 003 bounded structural observations; no network or writes to source."""
from pathlib import Path
from tempfile import TemporaryDirectory
import importlib.util
import json
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[5]
CAMPAIGN = Path(__file__).resolve().parents[1].relative_to(ROOT)
BASELINE = 'b4b1f80b375c9bb9811eae9a1d513c4580f00025'
CURRENT = ['README.md', 'AGENTS.md', 'SDD-MANAGER.md', 'AI_DISCLOSURE.md',
           'docs/dev/HANDOFF.md', 'docs/dev/SPEC.md', 'docs/dev/PLAN.md',
           'docs/dev/CAPABILITY_MAP.md', 'tools/check_package.py']
HISTORICAL = {'docs/dev/REVIEW.md', 'docs/dev/REVISION_REVIEW.md',
              'docs/dev/revision_plans/REVISION_PLAN_1cc08a2.md'}

def recipe_rows(path):
    return [line for line in path.read_text().splitlines()
            if line.startswith('| ') and len(line.split('|')) == 5 and '→' in line]

runtime = sorted(p for p in (ROOT / 'technical-writing-assistant').rglob('*') if p.is_file())
manager_rows = recipe_rows(ROOT / 'technical-writing-assistant/references/manager.md')
map_rows = recipe_rows(ROOT / 'docs/dev/CAPABILITY_MAP.md')
assert len(manager_rows) == len(map_rows) == 17 and manager_rows == map_rows
observations = {'baseline': BASELINE, 'runtime_files': len(runtime),
                'runtime_markdown_whitespace_words': sum(len(p.read_text().split()) for p in runtime if p.suffix == '.md'),
                'recipes': 17, 'recipe_rows_equal': True}
with TemporaryDirectory(prefix='twa-review003-') as temporary:
    fixture = Path(temporary)
    selected = [ROOT / p for p in CURRENT] + runtime
    selected += sorted(p for p in (ROOT / CAMPAIGN).rglob('*') if p.is_file() and '__pycache__' not in p.parts)
    for source in selected:
        target = fixture / source.relative_to(ROOT)
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    placeholders = set()
    for source in selected:
        if source.suffix != '.md':
            continue
        for link in re.findall(r'!?\[[^\]\n]*\]\(([^)\n]+)\)', source.read_text()):
            if re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', link):
                continue
            part, _, fragment = link.partition('#')
            original = (source.parent / part).resolve() if part else source
            if not original.is_relative_to(ROOT):
                continue
            relative = original.relative_to(ROOT)
            if relative.as_posix() in HISTORICAL:
                assert original.is_file() and not fragment, f'Historical placeholder requires content: {link}'
                target = fixture / relative
                target.parent.mkdir(parents=True, exist_ok=True)
                target.touch()
                placeholders.add(relative.as_posix())
    spec = importlib.util.spec_from_file_location('campaign_checker', fixture / 'tools/check_package.py')
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    errors, links, references = checker.check(fixture)
    observations['positive'] = {'references': references, 'local_links': links, 'errors': errors,
                                'selected_markdown_files': sum(p.suffix == '.md' for p in selected),
                                'existence_only_placeholders': sorted(placeholders)}
    assert not errors, errors
    missing = fixture / 'technical-writing-assistant/references/writing-brief.md'
    saved = missing.read_text()
    missing.unlink()
    negative_errors, _, _ = checker.check(fixture)
    assert any('Routing mismatch' in error for error in negative_errors)
    observations['missing_resource_negative'] = {'error_count': len(negative_errors), 'errors': negative_errors}
    missing.write_text(saved)
    entry = fixture / 'technical-writing-assistant/SKILL.md'
    original_entry = entry.read_text()
    entry.write_text(original_entry.replace('(references/manager.md)', '(references/manager.md#nonexistent-campaign003-anchor)', 1))
    anchor_errors, _, _ = checker.check(fixture)
    assert len(anchor_errors) == 1 and 'Missing anchor' in anchor_errors[0]
    observations['broken_anchor_negative'] = {'error_count': len(anchor_errors), 'errors': anchor_errors}
    entry.write_text(original_entry)
    assert not checker.check(fixture)[0]
protected = ['technical-writing-assistant', 'README.md', 'AGENTS.md', 'SDD-MANAGER.md',
             'AI_DISCLOSURE.md', 'docs/dev/SPEC.md', 'docs/dev/CAPABILITY_MAP.md', 'docs/dev/PLAN.md',
             'tools', 'docs/dev/reviews/001_dead567-comprehensive-skill-review',
             'docs/dev/reviews/002_6e6b0d7-size-scope-substance',
             'docs/dev/REVIEW.md', 'docs/dev/REVISION_REVIEW.md', 'docs/dev/revision_plans', 'docs/dev/validation']
subprocess.run(['git', 'diff', '--exit-code', BASELINE, '--', *protected], cwd=ROOT, check=True)
subprocess.run(['git', 'diff', '--check'], cwd=ROOT, check=True)
observations['protected_source_diff'] = 'unchanged'
print(json.dumps(observations, indent=2))
