# Final code analysis

## Outcome and scope

All nine requirements are implemented in `test.py`, with 21 passing unittest
methods in `tests/test_student.py`. Flake8 findings changed from **1 to 0**.
The initial report and original archive retain their genuine baseline defects.
No application dependency, persistence layer, GUI, or export feature was added.

## Requirement traceability

| # | Requirement | Implementation | Test evidence |
|---|---|---|---|
| 1 | Create student | Student.__init__; CLI create action | identity, invalid identity, independent grades, multiple-student CLI |
| 2 | Numeric grades 0-100 | add_grade; _validate_grade | multiple numeric grades; invalid text/bool/NaN/infinity/range |
| 3 | Average all grades | average property | decimal average; ungraded results |
| 4 | Letter grade | letter_grade property | all integer boundaries and just-below decimal thresholds |
| 5 | Pass/fail | status property | boundary table; fresh status after changes |
| 6 | Clear validation | constructor and mutators; CLI ValueError boundary | invalid identity/grades; invalid CLI inputs; EOF/interrupt |
| 7 | Boolean honor | honor_roll property | threshold table; recomputation after add/removal |
| 8 | Remove value/index | remove_grade_by_value; remove_grade_by_index | duplicate/missing/invalid/empty removals; zero-based indices |
| 9 | Formatted summary | report; CLI summary action | exact seven-field report; ungraded report; subprocess CLI |

21 is the number of unittest methods; their subTest iterations are not separate
test counts. The CLI suite includes real subprocess runs, plus a mocked keyboard
interrupt. Coverage percentage was not measured.

## Authentic local checks

Commands were executed from the repository root using the local virtual environment.

| Check | Exact command | Exit |
|---|---|---:|
| Phase 4 tests | `.venv/Scripts/python.exe -m unittest discover -s tests -v` | 0 |
| CLI smoke | `.venv/Scripts/python.exe test.py`, stdin from `evidence/phase-4-cli-input.txt` | 0 |
| Final HTML lint | `.venv/Scripts/python.exe -m flake8 --isolated test.py tests --format=html --htmldir=reports/final --htmlpep8 true --statistics` | 0 |
| Final tests | `.venv/Scripts/python.exe -m unittest discover -s tests -v` | 0 |

Installed direct tool versions: [privacy-redacted version record](../evidence/public/tool-versions.txt).

Captured output is in `evidence/phase-4-tests.txt`,
`evidence/phase-4-cli-output.txt`, `evidence/phase-5-final-lint.txt`, and
`evidence/phase-5-final-tests.txt`. These files contain real subprocess stdout
and stderr, not PowerShell error wrappers. The final lint file is intentionally
empty: both stdout and stderr were empty, exit 0. Separate command/exit/byte
metadata is in `evidence/verification-metadata.json`.

The unmodified generated final HTML says "No flake8 errors found in 2 files
scanned." Its stylesheet and local links are structurally checked. A clean run
does not generate per-file error/source pages; none were fabricated.

## Manual review and assumptions

- Names follow PEP 8: Student, student_id, add_grade, and related snake_case methods.
  The faulty sample was rewritten; repository search found no external API callers.
- Fixed business rules are named MIN_GRADE, MAX_GRADE, PASS_THRESHOLD,
  HONOR_THRESHOLD, and LETTER_THRESHOLDS; no duplicated bare pass/honor
  thresholds remain in business calculations.
- Numeric validation rejects text, booleans, NaN, infinity, and out-of-range values.
  The API accepts real numbers; the CLI parses text to float before validation.
- Grades are exposed as a read-only tuple, so callers cannot bypass validation by
  appending to a public list. Different students have independent lists.
- Derived values are recomputed, not cached. No grades means N/A average/letter,
  Not graded status, and False honor roll. No artificial zero or false failure.
- Continuous thresholds resolve the rubric's integer interval shorthand for
  decimal averages. Classification precedes two-decimal display rounding.
- IDs are case-sensitive, stripped, and unique within the CLI session. Duplicate
  creation does not overwrite an existing student. All data is session-only.
- Missing-value and invalid-index removal leave grades unchanged. Duplicate-value
  removal deletes only the first match. Indices are explicitly zero-based.
- Expected validation errors are caught at the terminal boundary, with no catch-all
  exception suppression. EOF and keyboard interrupt close the session gracefully.
- This is an in-memory teaching program, not a production student records system.
  Huge datasets, concurrency, disk persistence, and identity mutation are out of scope.
- The original division is always by zero if reached, not only for empty lists.
  Its observed run stopped earlier on the mixed numeric/string grades.
- HTML timestamps use host UTC+1; Ecuador is UTC-5. Generated evidence is unchanged.

## Workflow preparation

`.github/workflows/coding-standards.yml` uses pull_request targeting main and
workflow_dispatch, read-only contents permission, Ubuntu, and Python 3.11.
It installs pinned `requirements-dev.txt`, then lints only active source/tests
and runs unittest. Official action tags were read through GitHub's API:
checkout v6 resolved to `d23441a48e516b6c34aea4fa41551a30e30af803` and
setup-python v7 to `5fda3b95a4ea91299a34e894583c3862153e4b97`.
Those immutable SHAs are pinned with version comments.

The installed PyYAML parser parsed the workflow; assertions checked triggers,
branch, contents permission, runner, and step count. This is not actionlint or
proof of a remote run. Authentic screenshots now document phases 1-6,
including local workflow validation only. The English PDF lab report is
generated locally and validated: 16 pages, 11 authentic figures, all nine
requirements, four official sections, and clickable public repository links.
Every page was rendered and visually checked. Final publication remains
pending user approval; actual remote CI execution remains pending.

## Final candidate identity

After the named-business-constants correction, final HTML lint and all 21
tests were rerun with exit 0. Source SHA256: `d1f1ed4a9bd5bb804546eff9abaf3d15424d328c01a89357951da6997f0badc5`.
Source, tests, workflow, requirements, generated HTML, and existing
screenshots/logs were checked unchanged during PDF generation.
Internal freeze metadata is local-only and not a public deliverable.
