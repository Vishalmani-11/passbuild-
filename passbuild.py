import re
import time
import random
import string
import os
import json
import math
import pyfiglet
from datetime import datetime

# ─────────────────────────────────────────────────
#  HISTORY FILE
# ─────────────────────────────────────────────────
HISTORY_FILE = "password_history.json"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def loading_bar(message="Processing", length=40, delay=0.05):
    print(f"\n{message} ", end="")
    for _ in range(length):
        print("#", end="", flush=True)
        time.sleep(delay)
    print("\nDone!")


def copy_to_clipboard(text):
    """Copy text to clipboard (Linux/Windows/Mac)."""
    try:
        if os.name == "nt":
            import subprocess
            subprocess.run("clip", input=text.encode(), check=True)
        else:
            import subprocess
            # Try xclip first, then xsel
            try:
                subprocess.run(["xclip", "-selection", "clipboard"],
                               input=text.encode(), check=True)
            except FileNotFoundError:
                subprocess.run(["xsel", "--clipboard", "--input"],
                               input=text.encode(), check=True)
        return True
    except Exception:
        return False


def save_to_history(entry_type, password):
    """Save a password entry to history file."""
    history = load_history()
    history.append({
        "type": entry_type,
        "password": password,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)


def load_history():
    """Load password history from file."""
    if not os.path.exists(HISTORY_FILE):
        return []
    try:
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    except Exception:
        return []


# ─────────────────────────────────────────────────
#  ENTROPY CALCULATOR
# ─────────────────────────────────────────────────
def calculate_entropy(pwd: str):
    """Calculate password entropy and estimated crack time."""
    charset = 0
    if re.search(r"[a-z]", pwd):
        charset += 26
    if re.search(r"[A-Z]", pwd):
        charset += 26
    if re.search(r"\d", pwd):
        charset += 10
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", pwd):
        charset += 32

    if charset == 0:
        return 0, "instantly"

    entropy = len(pwd) * math.log2(charset)

    # Assume 10 billion guesses/sec (modern GPU brute-force)
    combinations = 2 ** entropy
    seconds = combinations / 1e10

    if seconds < 1:
        crack_time = "less than a second"
    elif seconds < 60:
        crack_time = f"{int(seconds)} seconds"
    elif seconds < 3600:
        crack_time = f"{int(seconds/60)} minutes"
    elif seconds < 86400:
        crack_time = f"{int(seconds/3600)} hours"
    elif seconds < 31536000:
        crack_time = f"{int(seconds/86400)} days"
    elif seconds < 3.154e9:
        crack_time = f"{int(seconds/31536000)} years"
    else:
        crack_time = f"{seconds/3.154e9:.2e} centuries"

    return round(entropy, 2), crack_time


# ─────────────────────────────────────────────────
#  PASSWORD STRENGTH CHECKER
# ─────────────────────────────────────────────────
def pass_checker(pwd: str):
    length_error      = len(pwd) < 8
    digit_error       = re.search(r"\d", pwd) is None
    uppercase_error   = re.search(r"[A-Z]", pwd) is None
    lowercase_error   = re.search(r"[a-z]", pwd) is None
    symbol_error      = re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", pwd) is None

    errors = {
        "Minimum 8 characters"       : length_error,
        "At least one digit"         : digit_error,
        "At least one uppercase letter" : uppercase_error,
        "At least one lowercase letter" : lowercase_error,
        "At least one symbol"        : symbol_error,
    }

    print("\n" + "=" * 45)
    print("         PASSWORD STRENGTH REPORT")
    print("=" * 45)

    for criteria, failed in errors.items():
        status = "❌ MISSING" if failed else "✅ PASSED "
        print(f"  {status}  →  {criteria}")

    print("-" * 45)

    error_count = sum(errors.values())
    entropy, crack_time = calculate_entropy(pwd)

    print(f"  Entropy Score  : {entropy} bits")
    print(f"  Crack Time     : ~{crack_time} (at 10B guesses/sec)")
    print("-" * 45)

    if error_count == 0:
        print("  RATING  →  ✅  STRONG PASSWORD")
    elif error_count < 2:
        print("  RATING  →  ⚠️   MODERATE PASSWORD")
    else:
        print("  RATING  →  ❌  WEAK PASSWORD")

    print("=" * 45)


# ─────────────────────────────────────────────────
#  PASSWORD MUNGING
# ─────────────────────────────────────────────────
def munging_password(pwd: str):
    replacements = {
        "a": "@", "A": "@",
        "i": "!", "I": "!",
        "s": "$", "S": "$",
        "o": "0", "O": "0",
        "e": "3", "E": "3",
        "t": "7", "T": "7",
        "b": "8", "B": "8",
        "g": "9", "G": "9",
    }

    munged = ""
    for char in pwd:
        munged += replacements.get(char, char)

    loading_bar("Munging password")
    print(f"\n  Original  : {pwd}")
    print(f"  Munged    : {munged}")

    try:
        num = int(input("\n  How many extra symbols to append? (0 to skip): ").strip())
    except ValueError:
        print("  Invalid input. Skipping extra symbols.")
        num = 0

    for i in range(num):
        add = input(f"  Enter symbol/text {i+1}: ").strip()
        munged += add

    print(f"\n  [+] Final munged password : {munged}")
    pass_checker(munged)

    # Save and clipboard
    save_to_history("munged", munged)
    if copy_to_clipboard(munged):
        print("\n  [+] Password copied to clipboard!")
    else:
        print("\n  [!] Could not copy to clipboard (install xclip on Linux).")

    print(f"  [+] Password saved to history.")


# ─────────────────────────────────────────────────
#  PASSWORD GENERATOR
# ─────────────────────────────────────────────────
def pass_generator():
    print("\n" + "=" * 45)
    print("      CUSTOM PASSWORD GENERATOR")
    print("=" * 45)

    try:
        length = int(input("  Enter desired password length (min 8): ").strip())
    except ValueError:
        print("  [!] Invalid input.")
        return

    if length < 8:
        print("\n  [!] Password must be at least 8 characters long!")
        return

    lower   = string.ascii_lowercase
    upper   = string.ascii_uppercase
    digits  = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"

    all_char = lower + upper + digits + symbols

    # Guarantee at least one from each category
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols),
    ]
    password += random.choices(all_char, k=length - 4)
    random.shuffle(password)

    loading_bar("Generating password", length=20, delay=0.1)
    finalpass = "".join(password)

    print("\n" + "=" * 45)
    print(f"  [!!] Your password  :  {finalpass}")
    print("=" * 45)

    pass_checker(finalpass)
    save_to_history("generated", finalpass)

    if copy_to_clipboard(finalpass):
        print("\n  [+] Password copied to clipboard!")
    else:
        print("\n  [!] Could not copy to clipboard (install xclip on Linux).")
    print("  [+] Password saved to history.")


# ─────────────────────────────────────────────────
#  PASSPHRASE GENERATOR
# ─────────────────────────────────────────────────
def passphrase_generator():
    print("\n" + "=" * 45)
    print("       PASSPHRASE GENERATOR")
    print("=" * 45)
    print("  Generates a human-readable but strong")
    print("  passphrase like: Horse-Battery-Staple-99!")
    print("=" * 45)

    # Built-in word list (no file needed)
    words = [
        "apple", "tiger", "castle", "rocket", "monkey", "purple", "dragon",
        "hammer", "silver", "forest", "planet", "jungle", "falcon", "butter",
        "winter", "shadow", "marble", "copper", "golden", "violet", "spider",
        "bridge", "candle", "flower", "gravel", "knight", "lemon", "mango",
        "napkin", "oyster", "pepper", "quartz", "ribbon", "saddle", "turban",
        "unique", "velvet", "walnut", "xyster", "yellow", "zipper", "anchor",
        "barrel", "cactus", "dagger", "engine", "fridge", "guitar", "harbor"
    ]

    try:
        num_words = int(input("  How many words? (recommended: 4-6): ").strip())
    except ValueError:
        print("  [!] Invalid input. Using 4 words.")
        num_words = 4

    if num_words < 2:
        print("  [!] Minimum 2 words. Setting to 2.")
        num_words = 2

    separator = input("  Separator (default: - ): ").strip() or "-"
    add_number = input("  Add a random number at the end? (y/n): ").strip().lower() == "y"
    add_symbol = input("  Add a random symbol at the end? (y/n): ").strip().lower() == "y"

    selected = [random.choice(words).capitalize() for _ in range(num_words)]
    passphrase = separator.join(selected)

    if add_number:
        passphrase += str(random.randint(10, 999))
    if add_symbol:
        passphrase += random.choice("!@#$%&*?")

    loading_bar("Building passphrase", length=20, delay=0.1)

    print("\n" + "=" * 45)
    print(f"  [!!] Your passphrase  :  {passphrase}")
    print("=" * 45)

    pass_checker(passphrase)
    save_to_history("passphrase", passphrase)

    if copy_to_clipboard(passphrase):
        print("\n  [+] Passphrase copied to clipboard!")
    else:
        print("\n  [!] Could not copy to clipboard.")
    print("  [+] Passphrase saved to history.")


# ─────────────────────────────────────────────────
#  PASSWORD HISTORY
# ─────────────────────────────────────────────────
def show_history():
    history = load_history()
    print("\n" + "=" * 60)
    print("              PASSWORD HISTORY")
    print("=" * 60)

    if not history:
        print("  [!] No history found. Generate some passwords first!")
        print("=" * 60)
        return

    for i, entry in enumerate(reversed(history), 1):
        print(f"  [{i}] {entry['date']}  |  {entry['type'].upper():<12}  |  {entry['password']}")

    print("=" * 60)
    print(f"  Total entries: {len(history)}")
    print("=" * 60)

    choice = input("\n  Clear all history? (yes/no): ").strip().lower()
    if choice == "yes":
        os.remove(HISTORY_FILE)
        print("  [+] History cleared.")


# ─────────────────────────────────────────────────
#  TITLE CARD
# ─────────────────────────────────────────────────
def title_card():
    clear()
    print("#" * 60)
    print("*" * 60)
    logo = pyfiglet.figlet_format("PASS BUILDER", font="slant")
    print(logo)
    print("*" * 60)
    print("  Author  : GOD$EYE")
    print("  Purpose : Generate | Check | Munge | Passphrase | History")
    print("#" * 60)
    print()


# ─────────────────────────────────────────────────
#  MAIN MENU
# ─────────────────────────────────────────────────
def main_menu():
    while True:
        print("\n" + "=" * 45)
        print("       --- WHAT BRINGS YOU HERE? ---")
        print("=" * 45)
        print("  1. Password Generator")
        print("  2. Password Strength Checker")
        print("  3. Munge Your Password")
        print("  4. Passphrase Generator")
        print("  5. Password History")
        print("  99. Exit")
        print("=" * 45)

        x = input("\n  [!] Enter your choice: ").strip()

        if x == "1":
            pass_generator()
        elif x == "2":
            pwd = input("\n  Enter your password to check: ").strip()
            pass_checker(pwd)
        elif x == "3":
            pwd = input("\n  Enter your password to munge: ").strip()
            munging_password(pwd)
        elif x == "4":
            passphrase_generator()
        elif x == "5":
            show_history()
        elif x == "99":
            print("\n  Thanks for using PASSWORD BUILDER!")
            print("  Cyaa!! 👋\n")
            break
        else:
            print("\n  [!] Invalid option. Please try again.")


# ─────────────────────────────────────────────────
#  ENTRY POINT
# ─────────────────────────────────────────────────
if __name__ == "__main__":
    title_card()
    main_menu()