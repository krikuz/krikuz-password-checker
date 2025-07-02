import re

def load_common_passwords():
    try:
        with open("common_passwords.txt", "r") as f:
            return set(line.strip() for line in f)
    except FileNotFoundError:
        print("⚠️ 'common_passwords.txt' not found. Skipping common password check.")
        return set()

def check_password_strength(password, common_passwords):
    score = 0
    issues = []

    # Length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        issues.append("Too short (< 8 characters)")

    # Character mix
    if re.search(r"[a-z]", password):
        score += 1
    else:
        issues.append("No lowercase letters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        issues.append("No uppercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        issues.append("No digits")

    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        score += 1
    else:
        issues.append("No special characters")

    # Common passwords
    if password.lower() in common_passwords:
        score = 0
        issues.append("This password is too common")

    # Strength rating
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    elif score == 5:
        strength = "Strong"
    elif score >= 6:
        strength = "Very Strong"

    return strength, issues

def main():
    print("🔒 Krikuz Password Strength Checker 🔍\n")
    pwd = input("Enter a password to check: ")

    common_pwds = load_common_passwords()
    strength, issues = check_password_strength(pwd, common_pwds)

    print(f"\nStrength: {strength}")
    if issues:
        print("⚠️ Issues:")
        for i in issues:
            print(f" - {i}")
    else:
        print("Your password looks solid.")

if __name__ == "__main__":
    main()
