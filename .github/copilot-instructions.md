## Repository snapshot

This repository is currently a minimal Python coursework project containing a single top-level script: `test.py`.

What I found:
- `test.py` — a simple script that prints "Hello, World!". No package manifests, tests, or CI configuration were detected.

## Quick-start actions for an AI coding agent

- Read `test.py` first to understand the program surface quickly.
- Run the code locally (macOS / zsh):

  python3 test.py

- If you add third-party packages, add a `requirements.txt` or `pyproject.toml` at the repo root and include install/run hints in this file.

## What changes are acceptable and how to propose them

- The project is single-file and small. Make focused, minimal edits that keep the script runnable with `python3 test.py`.
- If adding new files (modules, tests), place them beneath the repository root. Suggested layout for growth:

  - src/  (optional, Python packages)
  - tests/ (unit tests)

- When you introduce dependencies or tests, include short README notes and the exact commands to run them.

## Project-specific notes and examples

- Example: to change the printed message, update `print("Hello, World!")` in `test.py` and verify by running `python3 test.py`.
- No CI or lint configuration exists. If you add linting or formatting (flake8/black), commit the config files and update this instruction file with the exact commands.

## Edge cases and constraints discovered

- There is no existing test harness or dependency manifest — assume changes must remain small and self-contained unless you add project scaffolding (and document it).

## When to ask for human review

- For any behavior-changing edits beyond cosmetic string changes (for example: adding network access, heavy refactors, adding new dependencies), create a draft PR and request reviewer guidance.

## Summary / verification checklist for the agent

- Read `test.py` (done).
- Confirm changes run with `python3 test.py` on macOS/zsh.
- If adding packages/tests, add `requirements.txt` or `pyproject.toml` and update this file with run instructions.

---

If you'd like, I can expand this file to include a recommended template for tests, a minimal `requirements.txt`, or a starter `Makefile` — tell me which and I'll add it.
