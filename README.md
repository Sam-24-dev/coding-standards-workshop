# ESPOL Software Engineering II - Coding Standards Workshop

A small Python 3.11 terminal application implementing all nine Student Grade
Management requirements. Public repository:
https://github.com/Sam-24-dev/coding-standards-workshop

## Run and check

The application uses only the Python standard library. From the repository root:

```powershell
python test.py
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements-dev.txt
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
.\.venv\Scripts\python.exe -m flake8 --isolated test.py tests
```

Select a menu action, enter a student ID, and follow the prompts. Grade indices
start at **0**; removing a value removes its first occurrence only. Multiple
students are supported in memory. Data is **not saved after exit**.

To regenerate a final HTML report (do not overwrite the preserved initial report):

```powershell
.\.venv\Scripts\python.exe -m flake8 --isolated test.py tests --format=html --htmldir=reports/final --htmlpep8 true --statistics
```

The plugin requires the explicit value `true` for `--htmlpep8`.
On macOS/Linux, use `.venv/bin/python` instead of the Windows executable.

## Nine requirements

1. Create students with nonempty string IDs and names.
2. Add multiple real numeric grades in the inclusive range 0-100.
3. Average all grades; use N/A for an empty grade list.
4. Assign A >= 90, B >= 80, C >= 70, D >= 60, and F < 60.
5. Mark graded students Passed at 60 or above; otherwise Failed.
6. Display clear validation errors without crashing.
7. Compute a boolean Honor Roll flag at average >= 90.
8. Remove by value or zero-based index, handling invalid removals safely.
9. Format ID, name, count, average, letter, pass/fail, and honor roll.

Ungraded students are "Not graded", with N/A average/letter and False honor roll.
Classification uses the unrounded average; display uses two decimal places.

## Evidence and deliverables

- Original published baseline: commit `b6261a990d2c92d57d6d411113817c3b0c7b4a73`.
- Exact original archived at [original/test.py](original/test.py), SHA256
  `2049753365204B1D6BF7E02CEF0A0A15A8709213D0D2EC59740831867D845786`.
  Its deliberate defects remain unchanged; it is excluded from final lint/tests.
- [Initial HTML](reports/initial/index.html) and
  [initial analysis](reports/initial-analysis.md): one F841 finding.
- [Final HTML](reports/final/index.html) and
  [final analysis](reports/final-analysis.md): zero findings in two files.
- [Behavioral tests](tests/test_student.py): 21 passing unittest methods;
  subTest cases are not counted as separate tests.
- [Evidence index](evidence/README.md), authentic process screenshots, captured outputs, and [privacy-redacted tool versions](evidence/public/tool-versions.txt) are retained.
  Phases 1-6 have authentic screenshots, including local workflow validation;
  there is no actual remote CI screenshot or run yet.
- [CI workflow](.github/workflows/coding-standards.yml) runs lint and tests for
  pull requests to main and supports manual dispatch. Remote execution is pending.
- Complete English [PDF lab report](docs/lab-report.pdf) with Introduction,
  Development, Conclusions, and Recommendations: generated locally and validated
  (16 pages, 11 authentic figures). [Markdown source](docs/lab-report.md).
  Canvas accepts PDF only; HTML reports remain supplementary evidence.
- Final publication is pending user approval of the file summary.
  The public repository currently contains the original baseline; final local
  artifacts are not yet uploaded. Actual remote CI execution remains pending.

Generated HTML timestamps reflect the host UTC+1 timezone, not Ecuador UTC-5.
The generated reports and screenshots are not edited to change their timestamps.
