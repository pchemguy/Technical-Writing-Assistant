# Campaign 008 revision report

## Authority and preserved baseline

The user authorized planning, fixes and closure; subsequent routing-table questions added the bounded R-003 correction. [REVISION-PLAN.md](REVISION-PLAN.md) owns actions A-001–A-004. Original source review and reproduced-defect evidence remain unchanged except the separately recorded review correction. Starting review source is `fecf8cc097c9bccc78c0ac29676d397a1fefaa15`; completed review is `7fff37d4720ba38665ce688635a34e62b006fe48`; accepted plan is `699dc1ae6f48e9042a64c6971b742acad2bbb58c`; amended routing plan is `13d4f74ad52422c4ef57848970e545ddbab81364`.

## A-001 / R-001: frontmatter checking

**Executed and verified.** The standard-library checker now parses its documented one-line string subset, detects duplicate required/optional/nested keys, validates string metadata values, accepts supported optional fields and reports unsupported/ambiguous YAML as invalid or unverified with a nonzero result. Quoted required fields/comments and explicit empty metadata mappings are supported. Missing/oversized description and oversized compatibility remain failures. The runtime skill was not changed for this action.

Regression tests in `tests/test_check_package.py` exercise actual temporary copies of the package and literal format contrasts. The initial RED command produced **19 failed, 10 passed**, demonstrating duplicate-key/nonstring-metadata false acceptance, optional/quoted-field false rejection and unsupported-form gaps. After the production change, the same command produced **29 passed**:

```console
python -m pytest tests/test_check_package.py -q --tb=short -p no:cacheprovider
```

The session initially lacked pytest. Pytest 9.2.0 and its test-only dependencies were installed into an isolated scratch target and selected through command-local PYTHONPATH; no global install or runtime dependency was added. PYTHONDONTWRITEBYTECODE=1 prevents test bytecode output. The command above assumes pytest is available to the chosen Python.

The suite covers current package acceptance, valid optional/quoted/empty-string inputs, duplicate keys at both levels, unsupported/nonstring values, and missing-reference/broken-anchor/escaping-link regressions. It is format/checker evidence, not writing-workflow or client acceptance. The original review helper/JSON still describe the pre-revision checker and are not rerun or overwritten against this revised source.

## A-002 / R-002: supported current-source checks

**Executed and verified.** `python tools/check_package.py` now defaults to current root Markdown, the runtime package and current docs. Retained reviews/features/phase reports/revision plans/validation collections, legacy review documents and repository-local tool trees are not scanned as current sources. Explicit `--active-campaign PATH` options add selected immediate review-campaign directories; path/type/existence checks reject invalid selections. Excluded retained link targets receive existence-only checks without reading their contents or historical fragments. `--scope all` is an explicit, separately labelled full-repository operation and cannot be combined ambiguously with active selection.

README and AGENTS document the command, exclusions, parser subset, active selection and regression command. The real checkout passes both default scope (20 references / 164 links) and explicit campaign 008 scope (20 references / 176 links), with zero errors at this checkpoint.

Pytest RED before the scope implementation: **17 failed, 31 passed**. GREEN after implementation: **48 passed**. The new cases include synthetic inactive/tool records, active/current broken links, an unreadable historical target with a fragment (proving its contents are not read), missing historical targets, all-scope selection, invalid/unknown CLI options and ambiguous combinations. Full scope was tested only on synthetic fixtures; actual closed records were not read or validated.

## Remaining actions and closure boundary

A-001 was published as `62d2178d3f1a51c3cefd603018d62aa1871c5bfb`. Publish/read back A-002 before continuing. A-003 (all 20 entry routing rows and minimal composite handoffs) and user-requested A-004 (remove README Status, Illustrative revision and the identified safeguard paragraph) remain pending. Closure and main integration follow verified completion of all four actions, not this intermediate checkpoint.
