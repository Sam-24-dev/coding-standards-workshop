# Evidence index

These files preserve genuine workshop outputs. Browser screenshots show the public repository/commit, generated HTML reports, and actual saved subprocess output displayed in the browser; they are not simulated terminal interfaces. The VS Code capture is an authentic source-screen-region capture that excludes unrelated panes. Images were not retouched.

## Screenshots

- `phase-1-original-commit.png` — initial published commit.
- `phase-1-public-repository.png` — public repository page.
- `phase-2-initial-html.png` — initial generated HTML report.
- `phase-2-initial-findings.png` — finding detail in the initial report.
- `phase-2-lint-output.png` — actual saved initial lint output displayed in the browser.
- `phase-3-vscode-refactored.png` — refactored source in VS Code.
- `phase-4-tests.png` — test output.
- `phase-4-cli.png` — CLI exercise.
- `phase-5-final-html.png` — final generated HTML report.
- `phase-5-final-verification.png` — final verification evidence.

There is no CI screenshot yet. No coverage percentage was measured. A direct native-terminal screenshot was not captured; actual command output is preserved in files and browser snapshots show those outputs rather than a fabricated terminal UI.

## Captured outputs and metadata

- `phase-2-install.txt` — pip installation stdout/stderr.
- `phase-2-initial-lint.txt` — initial Flake8 output (one `F841` finding).
- `public/phase-2-original-runtime.txt` — privacy-redacted derivative of the original runtime output; the local raw source is excluded from Git.
- `public/tool-versions.txt` — privacy-redacted installed tool-version record; the local raw source is excluded from Git.
- `phase-4-cli-input.txt`, `phase-4-cli-output.txt` — CLI input and actual output.
- `phase-4-tests.txt` — 21 passing unittest methods.
- `phase-5-final-lint.txt` — final Flake8 output (zero findings; empty output on success).
- `phase-5-final-tests.txt` — final test output.
- `baseline-preservation.json`, `implementation-freeze.json`, `verification-metadata.json` — source and verification metadata.

The initial scan found one `F841`; the final scan found zero findings. HTML report timestamps reflect the generating host (UTC+1), while Ecuador is UTC-5. Timestamps were not rewritten.