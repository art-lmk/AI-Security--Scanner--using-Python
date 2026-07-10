# AI Security Scanner for Python

An AI-powered static analysis tool that scans Python code for security 
vulnerabilities using large language model reasoning, going beyond 
traditional pattern-matching scanners.

## Why this is different

Most existing tools (Bandit, Semgrep) flag code based on fixed rules — 
e.g. "this uses `eval()`, flag it" — regardless of context. This leads 
to noisy false positives and misses logic-based vulnerabilities that 
don't match a known pattern.

This scanner uses an LLM to read code the way a human reviewer would:
- Understands context (e.g. whether user input was already sanitized)
- Explains *why* something is risky, in plain language
- Suggests a concrete fix, not just a flag
- Generalizes to novel vulnerability patterns rule-based tools miss

## What it checks for

- SQL injection risks
- Hardcoded secrets / API keys
- Unsafe use of `eval()`, `exec()`, `pickle`, `subprocess`
- Insecure file handling / path traversal
- Poor input validation

## Tech stack

- Python 3.10
- [OpenAI API — specify which]
- [Any other libraries you're using]

## Setup

```bash
git clone https://github.com/art-lmk/AI-Security--Scanner--using-Python.git
cd AI-Security--Scanner--using-Python
pip install -r requirements.txt
```

## Usage

```bash
python scanner.py [path-to-file-or-directory]
```

## Status

🚧 Work in progress

## Author

[Your name] — Data Analyst | AI/Cloud upskilling