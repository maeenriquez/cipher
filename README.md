# Substitution Cipher (C)

## Description
A C program that implements a substitution cipher. The program encrypts plaintext by substituting each letter with a corresponding letter from a user-provided key. The key must be a valid permutation of the alphabet containing exactly 26 unique alphabetic characters.

---

## Features
- Validates encryption key length and uniqueness
- Rejects non-alphabetic or duplicate characters in the key
- Preserves letter case (uppercase/lowercase)
- Leaves non-alphabetic characters unchanged
- Dynamically allocates memory for ciphertext

---

## Tech Stack
- **Language:** C
- **Libraries**: stdio.h, stdlib.h, string.h, ctype.h
- **Concepts**: Arrays, Strings, Pointers, Dynamic Memory, Input Validation

---

## How to Run

1. Compile the program:
```bash
gcc cipher.c -o cipher
```
2. Run the executable with a 26-character key:
```bash
./cipher YTNSHKVEFXRBAUQZCLWDMIPGJO
```
3. Enter the plaintext when prompted.
4. The program will output the encrypted ciphertext.

---

## Key Requirements
- Must contain exactly 26 characters
- Must contain alphabetic characters only
- Must contain no repeated letters (case-insensitive)
*Invalid keys will result in an error message.*

---

## Notes
- Encryption preserves the original case of each letter.
- Non-letter characters (spaces, punctuation, numbers) are not modified.
- Memory allocated for the ciphertext is properly freed after use.
