# ESPOL Software Engineering II — Coding Standards Workshop

This repository is the working space for the Python coding-standards lab. The supplied `test.py` is the deliberately faulty original; preserve it as the initial baseline until the lab analysis begins.

## Workshop requirements

1. Create students with nonempty IDs and names.
2. Add multiple numeric grades in the range 0–100.
3. Calculate the average of all grades and safely handle students with no grades.
4. Assign letters: A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60, and F < 60.
5. Mark students Passed at 60 or above; otherwise mark them Failed.
6. Show clear errors for invalid IDs, names, or grades without crashing.
7. Set a boolean Honor Roll flag when the average is at least 90.
8. Remove grades by value or index; clearly handle missing values and out-of-range indices.
9. Print a formatted summary with ID, name, grade count, average, letter, pass/fail, and honor roll.
## Tools and planned workflow

Python 3.11, VS Code, Flake8, `flake8-html`, and GitHub are the selected tools. Later phases will create a virtual environment, install the lint tools, and generate HTML reports. Planned commands:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install flake8 flake8-html
.\.venv\Scripts\python.exe -m flake8 test.py --format=html --htmldir=reports/initial --htmlpep8
```

## Deliverables and status

- Public GitHub repository URL — **NOT YET COMPLETED**
- Four-section English lab report (Introduction, Development, Conclusions, Recommendations) — **NOT YET COMPLETED**
- Initial and final HTML lint reports — **NOT YET COMPLETED**
- Real screenshots of the work and evidence — **NOT YET COMPLETED**
- Pull-request-to-main lint workflow challenge — **NOT YET COMPLETED**
- Code analysis, fixes, and tests — **NOT YET COMPLETED**
- CI workflow — **NOT YET COMPLETED**

No analysis, fixes, tests, reports, screenshots, CI, or public repository evidence is claimed at this stage.