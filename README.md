# 🔐 PASSWORD BUILDER

<div align="center">

```
 ____   _    ____  ______        _____  ____  ____
|  _ \ / \  / ___||  ___| |     / _ \ / ___||  _ \
| |_) / _ \ \___ \| |_  | |    | | | | |  _ | | | |
|  __/ ___ \ ___) |  _| | |___ | |_| | |_| || |_| |
|_| /_/   \_\____/|_|   |_____| \___/ \____||____/

 ____  _   _ ___ _     ____  _____ ____
| __ )| | | |_ _| |   |  _ \| ____|  _ \
|  _ \| | | || || |   | | | |  _| | |_) |
| |_) | |_| || || |___| |_| | |___|  _ <
|____/ \___/|___|_____|____/|_____|_| \_\
```

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20Mac-lightgrey?style=for-the-badge&logo=linux)
![Security](https://img.shields.io/badge/Security-Password%20Tool-red?style=for-the-badge&logo=gnuprivacyguard)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**A terminal-based Python tool to generate strong passwords, check password strength, and munge existing passwords — built for security enthusiasts.**

</div>

---

## 📌 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
- [Menu Overview](#-menu-overview)
- [Feature Details](#-feature-details)
  - [Password Generator](#1--password-generator)
  - [Password Strength Checker](#2--password-strength-checker)
  - [Password Munging](#3--password-munging)
- [Examples](#-examples)
- [How It Works](#-how-it-works)
- [Project Structure](#-project-structure)
- [Security Notes](#-security-notes)
- [Contributing](#-contributing)
- [Author](#-author)
- [License](#-license)

---

## 📖 About

**PASSWORD BUILDER** is a simple but powerful terminal-based Python tool designed to help users:

- **Create** strong, randomized passwords from scratch
- **Check** how strong an existing password is
- **Munge** (transform) an existing password using leet-speak style character substitutions to make it significantly harder to crack

This tool is ideal for cybersecurity learners, ethical hackers, sysadmins, and anyone who wants to take control of their password security without relying on third-party online services.

> 💡 All password operations happen **locally on your machine** — nothing is sent to the internet.

---

## ✨ Features

- ✅ **Random Password Generator** — generates cryptographically shuffled passwords with guaranteed use of uppercase, lowercase, digits, and symbols
- ✅ **Password Strength Checker** — rates your password as Strong / Moderate / Weak based on 5 security criteria
- ✅ **Password Munging** — transforms plain passwords using leet-speak substitutions (e.g. `a→@`, `s→$`, `e→3`) and lets you append extra custom symbols
- ✅ **Custom Length** — choose exactly how long your generated password should be
- ✅ **Visual Progress Bar** — loading animations for a satisfying experience
- ✅ **Simple Menu Interface** — no complex flags or arguments needed

---

## 🖥️ Requirements

| Requirement | Details |
|---|---|
| Operating System | Linux / Windows / macOS |
| Python | 3.6 or higher |
| pip package | `pyfiglet` |
| Privileges | No root required (root recommended on Linux) |

---

## ⚙️ Installation

### Step 1 — Clone the repository
```bash
git clone https://github.com/Vishalmani-11/password-builder.git
cd password-builder
```

### Step 2 — Install Python dependency
```bash
pip install pyfiglet
```

### Step 3 — Run the tool
```bash
python3 passbuild.py
```

> On Linux, run as root for best experience:
> ```bash
> sudo python3 passbuild.py
> ```

---

## 🚀 Usage

```bash
python3 passbuild.py
```

You will be greeted with the title card and then taken to the main menu automatically.

---

## 📋 Menu Overview

```
****************************************
---What brings u here !---
1. password maker
2. password strength checker
3. munging your password
99. Exit
****************************************

[!] Enter your choice :
```

---

## 🔍 Feature Details

### 1. 🔑 Password Generator

Generates a strong, fully randomized password of your chosen length.

**How to use:**
```
Menu → 1
Enter the length of your password (minimum 8 chars): 16
```

**What it guarantees:**
- At least **1 uppercase** letter
- At least **1 lowercase** letter
- At least **1 digit**
- At least **1 symbol**
- Remaining characters are **randomly chosen** from all categories
- Final password is **shuffled** so patterns are unpredictable

**Character sets used:**

| Type | Characters |
|---|---|
| Lowercase | `a-z` |
| Uppercase | `A-Z` |
| Digits | `0-9` |
| Symbols | `!@#$%^&*()-_=+[]{};:,.<>?/` |

---

### 2. 🔎 Password Strength Checker

Analyzes a password against 5 security criteria and rates it.

**How to use:**
```
Menu → 2
Enter your password to be checked: MyP@ssw0rd
```

**Criteria checked:**

| Check | Requirement |
|---|---|
| Length | At least 8 characters |
| Digit | Contains at least one number (0-9) |
| Uppercase | Contains at least one uppercase letter (A-Z) |
| Lowercase | Contains at least one lowercase letter (a-z) |
| Symbol | Contains at least one special character |

**Rating system:**

| Errors | Rating |
|---|---|
| 0 errors | ✅ **Strong password** |
| 1 error | ⚠️ **Moderate password** |
| 2+ errors | ❌ **Weak password** |

---

### 3. 🔀 Password Munging

Takes your existing password and transforms it using **leet-speak substitutions**, then lets you add extra symbols on top.

**How to use:**
```
Menu → 3
Enter your password to be munged: password
```

**Substitution table:**

| Original | Replaced with |
|---|---|
| `a` or `A` | `@` |
| `i` or `I` | `!` |
| `s` or `S` | `$` |
| `o` or `O` | `0` |
| `e` or `E` | `3` |

**Example:**
```
Input:    password
Munged:   p@$$w0rd

Then you can add extra symbols:
Enter the number of extra symbols to add: 2
Enter symbol 1 to add: #
Enter symbol 2 to add: 99
Final: p@$$w0rd#99
```

> 💡 Munging is a great way to upgrade an old weak password into something much harder to brute-force without completely reinventing it.

---

## 💡 Examples

### Generate a 20-character password:
```
[!] Enter your choice: 1
Enter the length of your password (minimum 8 char): 20

Generating your password####################

[!!] Your final password is: t$K3#mPqZ!nR8@wLxV2&
```

---

### Check if a password is strong:
```
[!] Enter your choice: 2
Enter your password to be checked: hello

Weak password
```

```
[!] Enter your choice: 2
Enter your password to be checked: H3ll0@World!

Strong password
```

---

### Munge an existing password:
```
[!] Enter your choice: 3
Enter your password to be munged: ilovesecurity

Loading ########################################
Your password had Done munging.....
Enter the number of extra symbols to add: 1
Enter symbol 1 to add: @2024

The final munged password is: !l0v3$3cur!ty@2024
```

---

## 🔧 How It Works

### Password Generator
1. Creates 4 guaranteed characters — one from each required category
2. Fills the remaining slots with random characters from the combined pool
3. Shuffles the entire list using `random.shuffle()` to eliminate positional patterns
4. Joins and displays the result

### Strength Checker
1. Uses **Python regex** (`re` module) to scan the password for each character type
2. Counts how many criteria are NOT met (errors)
3. Returns a rating based on the error count

### Password Munging
1. Iterates character by character through the input password
2. Replaces matching characters using a predefined dictionary
3. Lets the user interactively append additional symbols
4. Returns the fully transformed password

---

## 📁 Project Structure

```
password-builder/
│
├── passbuild.py      # Main script
├── README.md         # This file
└── LICENSE           # MIT License
```

---

## 🔒 Security Notes

- **Do NOT use the generator for banking or critical accounts without storing the password in a proper password manager** (e.g. Bitwarden, KeePass).
- **Munging alone is not enough** — common leet-speak substitutions are well known to attackers and included in modern wordlists. Always add unique symbols.
- **The strength checker is a guide, not a guarantee.** A "Strong" rating means it passes basic rules — it does not mean it cannot be cracked.
- **Never share generated passwords** over unencrypted channels (SMS, plain email, etc.).
- All processing is **100% local** — no data leaves your machine.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are always welcome!

1. Fork the repository
2. Create your feature branch:
   ```bash
   git checkout -b feature/new-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add: your feature description"
   ```
4. Push to GitHub:
   ```bash
   git push origin feature/new-feature
   ```
5. Open a **Pull Request**

### Ideas for future features:
- [ ] Password history log (save generated passwords locally encrypted)
- [ ] Passphrase generator (word-based passwords)
- [ ] Entropy score display for passwords
- [ ] Clipboard copy support (auto-copy password after generation)
- [ ] Bulk password generation (generate N passwords at once)
- [ ] Export generated passwords to an encrypted file
- [ ] GUI version using `tkinter`

---

## 👤 Author

**GOD$EYE**

- GitHub: [@Vishalmani-11](https://github.com/Vishalmani-11)

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

```
MIT License

Copyright (c) 2024 GOD$EYE

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files, to deal in the Software
without restriction, including without limitation the rights to use, copy,
modify, merge, publish, distribute, sublicense, and/or sell copies of the
Software.
```

---

<div align="center">

Made with 🔐 by **GOD$EYE** aka Vishalmani-11

⭐ If this tool helped you, give it a star on GitHub!

</div>
