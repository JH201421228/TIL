# Repository Guidelines

## Project Structure & Module Organization
The repository is organized per BOJ problem: each `boj_<id>/` directory houses language-specific solutions (`1st.py`, `1st.cpp`, `1st.js`, `Main.java`), the problem statement (`problem.md`), and a local harness in `input.txt`. Keep new problems self-contained by duplicating that layout, storing any supplementary notes under subfolders such as `boj_1234/docs/`. Shared helpers should live directly beside the solution that relies on them so submissions stay copy-paste-ready for the online judge.

## Build, Test, and Development Commands
Run commands from inside the target problem directory:
- `python3 1st.py < input.txt` – executes the Python solution with the bundled sample input.
- `g++ -std=c++17 -O2 1st.cpp -o 1st && ./1st < input.txt` – builds/tests the C++ version.
- `javac Main.java && java boj_5977.Main < input.txt` – compiles and runs Java; adjust the package to match the folder name.
- `node 1st.js < input.txt` – runs the JavaScript variant via Node.js.

## Coding Style & Naming Conventions
Follow the existing naming scheme: folders use `boj_<problemId>`, files use numbered stems (`1st`, `2nd`) to reflect iteration order, and Java keeps its `Main` entry point inside a matching package. Python modules use 4-space indentation and favor `snake_case` helpers; C++/Java keep braces on their own lines with minimal macros; JavaScript sticks to `const`/`let` and template literals only when necessary. Run formatters (e.g., `python -m black`, `clang-format`) only if the entire file benefits, then document that decision in the PR.

## Testing Guidelines
Each directory’s `input.txt` acts as the smoke-test harness—update it or add `input.sampleN.txt` files as new cases appear, and mention coverage decisions in the PR. Prefer verifying the same logic in at least two languages when both exist to catch off-by-one issues. Capture tricky boundary cases (e.g., `K = 1`, `K = N`, maximum constraints) and include the expected stdout in comments or PR notes. There is no CI, so local verification is mandatory before sharing changes.

## Commit & Pull Request Guidelines
Git history uses concise entries such as `20251112 #1`; keep that `YYYYMMDD #n` pattern and write imperatively (“Add DP for 5977”). When opening a PR, include: (1) the problem ID and language touched in the title, (2) a short summary of the algorithmic change, (3) test evidence (command + sample input/output), and (4) links to any external references used. Screenshots are unnecessary, but paste console snippets if behavior changed.

## Environment & IO Tips
Most scripts redirect `sys.stdin` or buffered streams to `input.txt` for repeatable runs; switch back to `sys.stdin = sys.__stdin__` (or rely on default readers) before exporting code to BOJ. Avoid hardcoding absolute paths or OS-specific optimizations—use relative paths and standard fast I/O patterns (`ios::sync_with_stdio(false)`, `BufferedReader`). Keep `input.txt` small enough for quick diffs, and ignore binaries (e.g., `1st.exe`) in commits unless reproducibility requires them.
