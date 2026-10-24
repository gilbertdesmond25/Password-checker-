"""
Password Strength Checker
A beginner Python project for a cybersecurity portfolio.

What it teaches:
  - variables, input(), if/else, loops, functions
  - checking strings for uppercase, lowercase, digits, symbols
  - giving clear feedback instead of just a yes/no

Safety note: this runs only on your own device.
It never sends your password anywhere. Test it with
example passwords, not a password you actually use.
"""

def check_password(password):
    """Return a score (0-5) and a list of tips to improve it."""
    score = 0
    tips = []

    # 1. Length - longer is harder to guess
    if len(password) >= 12:
        score += 1
    else:
        tips.append("Make it at least 12 characters long.")

    # 2. Uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        tips.append("Add at least one uppercase letter (A-Z).")

    # 3. Lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        tips.append("Add at least one lowercase letter (a-z).")

    # 4. Numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        tips.append("Add at least one number (0-9).")

    # 5. Special characters
    special = "!@#$%^&*()-_=+[]{};:,.<>?/"
    if any(char in special for char in password):
        score += 1
    else:
        tips.append("Add at least one special character, like ! or #.")

    return score, tips


def rating(score):
    """Turn a score into a plain-English rating."""
    if score <= 1:
        return "Weak"
    if score == 2:
        return "Fair"
    if score == 3:
        return "Good"
    if score == 4:
        return "Strong"
    return "Very Strong"


def main():
    print("Password Strength Checker")
    print("Type 'quit' to stop.\n")

    while True:
        password = input("Enter a password to check: ")

        if password.lower() == "quit":
            print("Goodbye!")
            break

        if password == "":
            print("You didn't type anything. Try again.\n")
            continue

        score, tips = check_password(password)
        print(f"\nScore: {score}/5 - {rating(score)}")

        if tips:
            print("To make it stronger:")
            for tip in tips:
                print(f"  - {tip}")
        else:
            print("Nice - this one ticks every box.")
        print()


if __name__ == "__main__":
    main()
