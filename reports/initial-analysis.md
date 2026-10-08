# Initial baseline analysis

## Lint run

Command from the repository root:

```powershell
.\.venv\Scripts\python.exe -m flake8 --isolated test.py --format=html --htmldir=reports/initial --htmlpep8 true --statistics
```

The `flake8-html` 0.4.3 option `--htmlpep8` requires a value; `true` enables its PEP 8-style text report. Flake8 exited **1**, expected because it found a violation (not a tool failure). Authentic captured output: `evidence/phase-2-initial-lint.txt`.

| Observed result | Count |
|---|---:|
| Flake8 findings | 1 |
| `F841` — local variable `avg` is assigned but never used | 1 |

The HTML index reports one finding for `test.py`. `index.html`, `test.report.html`, `test.source.html`, `styles.css`, `back.svg`, and `file.svg` exist and the report links resolve to local files. This is a structural/file check, not a separate standards-compliance validation of generated HTML. The report is a snapshot of Flake8's enabled checks, not a complete assessment of functional requirements.

## Runtime and manual inspection

Running the original file exited **1** with a `TypeError` when `addGrades("Fifty")` leaves a string in the grade list and `calcaverage` tries to add it to an integer. This is a runtime failure, not a Flake8 finding; execution stops before later defects are reached. Captured output: [privacy-redacted public copy](../evidence/public/phase-2-original-runtime.txt). The original local file `evidence/phase-2-original-runtime.txt` is preserved byte-for-byte and excluded from Git; it includes the PowerShell native-command error wrapper around the traceback.

Manual inspection identifies further issues not reported by this run: division by zero; the calculated average is not returned; `checkHonor` calls `calcAverage`, which does not match `calcaverage`; no numeric grade checks; `honor` is a string rather than a boolean; no letter-grade or pass/fail calculation; `report` references an undefined `letter`, concatenates a string with `len(...)`, and omits the average/status fields; deletion is index-only and has no handling for absent grades or invalid indices.

## Nine-requirement baseline gaps

1. Constructor accepts empty names/IDs; the sample name is empty.
2. Grades are not constrained to numeric values or 0–100; the sample adds a string.
3. Average always divides by zero if reached and is not returned.
4. Required A/B/C/D/F thresholds are absent.
5. Passed/Failed status logic is absent.
6. Invalid IDs, names, and grades are not validated or reported clearly.
7. Honor Roll is a string, not a boolean; threshold behavior is not implemented (and the method call name is incorrect).
8. Deletion supports only index, without handling missing values or invalid indices.
9. Summary references missing data and invalid concatenation; required fields are missing.

## Baseline identity

- Source: `test.py`
- SHA256 before and after analysis: `2049753365204B1D6BF7E02CEF0A0A15A8709213D0D2EC59740831867D845786`
- Source lines: 42

No source edits or fixes were made in this phase.