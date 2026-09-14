# Vulnerable Login Demo

A demonstration of SQL injection: a deliberately vulnerable login system, the exploit that breaks it, and the fix that patches it.

## Why I built it
To understand SQL injection from both sides — how the attack works and how to properly defend against it — rather than just reading about it.

## How it works
`app_vulnerable.py` builds SQL queries using raw string formatting, so user input can be crafted to alter the query's logic. `app_patched.py` fixes this using parameterized queries, where input is always treated as data, never as executable code.

## Setup
```bash
pip install -r requirements.txt
python setup_db.py
python app_vulnerable.py
