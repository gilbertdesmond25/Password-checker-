# Password Strength Checker

A beginner Python project, built as a first step toward cybersecurity.

## What it does
Asks for a password, scores it out of 5, and tells you exactly how to make it stronger:
length, uppercase, lowercase, numbers, and special characters.

## How to run it
```bash
python3 password_strength_checker.py
```
Type a test password, or type `quit` to stop.

## What I learned building it
- Variables and user input
- `if/else` decisions
- Loops (`while`, `for`)
- Functions (`check_password`, `rating`)
- Checking strings with `any()`, `isupper()`, `islower()`, `isdigit()`

## Safety note
This runs only on your own device and never sends a password anywhere.
Use test passwords, not a real one you use for an account.

## Next upgrade ideas
- Read passwords from a file and check a list at once
- Check for common passwords like `password123`
- Hash a password instead of ever printing it in plain text
