# Copilot Instructions

## Coding standards
- Use Python 3.11 with type hints on all function parameters and return values.
- Follow PEP 8 with a maximum line length of 100.
- Write Google-style docstrings for every public function.
- Use the logging module for messages. Never use print().
- For invalid input, raise ValueError with a clear message. Never return None or False to signal an error.

## Project rules
- All authentication logic lives only in app/auth.py.
- Never hardcode secrets. Read them from app/config.py.
- Return errors from API routes using format_error in app/utils.py.
