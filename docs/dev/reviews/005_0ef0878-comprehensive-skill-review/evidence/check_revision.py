"""Check the bounded campaign 005 revision without loading historical reports."""
from pathlib import Path
from tempfile import TemporaryDirectory
import importlib.util
import json
import re
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[5]
CAMPAIGN = Path(__file__).resolve().parents[1]
REVIEW = 'cb25838027d2b047078a535675ac9bae6cdb66e1'
BASELINE = '0ef087801f826d749c791f4116012930dcddfce7'
SOURCE = 'technical-writing-assistant/references/outline-review.md'
CURRENT = ['README.md', 'AGENTS.md', 'SDD-MANAGER.md', 'AI_DISCLOSURE.md',
           'WINDOWS_SHELL_POLICY.md', 'SKILL_DISCOVERY_PROTOCOL.md', 'docs/dev/HANDOFF.md',
           'docs/dev/SPEC.md', 'docs/dev/PLAN.md', 'docs/dev/CAPABILITY_MAP.md', 'tools/check_package.py']
HISTORY = {'docs/dev/REVIEW.md', 'docs/dev/REVISION_REVIEW.md',
           'docs/dev/revision_plans/REVISION_PLAN_1cc08a2.md'}
original = subprocess.check_output(['git', 'show', REVIEW + ':' + SOURCE], cwd=ROOT).decode()
current = (ROOT / SOURCE).read_bytes().decode()
addition = '''- A required "Context" topic appears as a heading, but no supplied content explains it. Topic presence is satisfied; explanatory adequacy is not assessable. If the brief also requires content notes, their absence fails that separate requirement. Do not invent a note requirement for a topic-only outline.
- One contradictory status claim fails both source fidelity and required-topic representation. Report one finding carrying both criterion bases and its shared remedy. Keep independent defects separate.
'''
assert current.replace(addition, '', 1) == original
runtime_changes = subprocess.check_output(['git', 'diff', '--name-only', REVIEW, '--', 'technical-writing-assistant'], cwd=ROOT, text=True).splitlines()
assert runtime_changes == [SOURCE], runtime_changes
result = {'review_source': REVIEW, 'source_file': SOURCE,
          'candidate_blob': subprocess.check_output(['git', 'hash-object', SOURCE], cwd=ROOT, text=True).strip(),
          'added_words': len(addition.split()), 'source_change': 'Exactly two examples; existing source preserved.'}
protected = ['REVIEW-PLAN.md', 'evidence/consumer-a.md', 'evidence/consumer-b.md',
             'evidence/check_current.py', 'evidence/structural-results.json',
             'evidence/icon-128.png', 'evidence/icon-32.png', 'independent/editorial.md',
             'independent/interfaces.md', 'independent/consumer-assessment.md']
subprocess.run(['git', 'diff', '--exit-code', REVIEW, '--', *[str((CAMPAIGN / p).relative_to(ROOT)) for p in protected]], cwd=ROOT, check=True)
result['original_review_evidence'] = 'unchanged'
with TemporaryDirectory(prefix='twa-revision005-') as temp:
    fixture = Path(temp)
    files = [ROOT / p for p in CURRENT]
    files += [p for p in (ROOT / 'technical-writing-assistant').rglob('*') if p.is_file()]
    files += [p for p in CAMPAIGN.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
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
            original_path = (source.parent / part).resolve() if part else source
            if original_path.is_relative_to(ROOT) and original_path.relative_to(ROOT).as_posix() in HISTORY:
                assert original_path.is_file() and not anchor
                target = fixture / original_path.relative_to(ROOT)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.touch()
                placeholders.add(original_path.relative_to(ROOT).as_posix())
    spec = importlib.util.spec_from_file_location('revision005_checker', fixture / 'tools/check_package.py')
    checker = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checker)
    errors, links, references = checker.check(fixture)
    assert not errors, errors
    result['structural'] = {'references': references, 'links': links, 'errors': errors,
                            'selected_markdown_files': sum(p.suffix == '.md' for p in files),
                            'existence_only_placeholders': sorted(placeholders)}
def recipe_rows(name):
    return [line for line in (ROOT / name).read_text().splitlines()
            if line.startswith('| ') and len(line.split('|')) == 5 and chr(8594) in line]
a = recipe_rows('technical-writing-assistant/references/manager.md')
b = recipe_rows('docs/dev/CAPABILITY_MAP.md')
assert len(a) == len(b) == 17 and a == b
result['recipe_rows_equal'] = 17
changed = subprocess.check_output(['git', 'diff', '--name-only', BASELINE], cwd=ROOT, text=True).splitlines()
untracked = subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard'], cwd=ROOT, text=True).splitlines()
prefix = CAMPAIGN.relative_to(ROOT).as_posix() + '/'
assert all(p in {'docs/dev/HANDOFF.md', SOURCE} or p.startswith(prefix) for p in changed + untracked)
subprocess.run(['git', 'diff', '--check'], cwd=ROOT, check=True)
result['protected_scope'] = 'Only outline-review, HANDOFF and campaign 005 differ; previous closed packages/current governing sources unchanged.'
print(json.dumps(result, indent=2))
