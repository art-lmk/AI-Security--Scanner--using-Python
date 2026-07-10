# AI Security Scanner for Python

An AI-powered static analysis tool that scans Python code for security 
vulnerabilities using Google's Gemini models, going beyond traditional 
pattern-matching scanners.

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
- Google Gemini API (`google-genai`)
- `python-dotenv` for environment variable management

## Setup

```bash
git clone https://github.com/art-lmk/AI-Security--Scanner--using-Python.git
cd AI-Security--Scanner--using-Python
python -m venv venv
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```

Create a `.env` file in the project root with your Gemini API key:
