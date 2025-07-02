# 🔒 Krikuz Password Strength Checker

> 👑 Because "password123" ain’t it, chief.

This is a simple yet powerful Python tool that checks how strong your passwords really are.  
It analyzes the length, complexity, and whether it’s a commonly used password, and gives you a strength rating, along with tips to improve it.
[note: the list of common passwords may not be 100% accurate but we use RockYou so it's pretty reliable.]

Built for real-world use, not just coding practice.

---

## 🚀 How to Run It

1. Clone the repo or download the files:
    git clone https://github.com/krikuz/krikuz-password-checker.git
    cd krikuz-password-checker

2. Run the script:
    python krikuz_passcheck.py

3. Enter a password when prompted.

You’ll get a strength rating like:
    Weak
    Medium
    Strong
    Very Strong
along with feedback to help you.

## Features
Checks for length (8+ is good, 12+ is recommended)

Requires a mix of:
    Uppercase letters
    Lowercase letters
    Digits
    Special characters

Compares against a list of common passwords &
Tells you what your password is missing

## Future Upgrades (Coming Soon):
    Integration with HaveIBeenPwned API for breach detection
    GUI version for non-terminal folks
    Batch-checking password files (for pentesters)
    Discord bot version

## Disclaimer:
This tool is for educational purposes only.
Don’t use it to test other people’s passwords, crack accounts, or do anything illegal.
Stay Moral. Stay Responsible.

## Star this repo if you appreciate it