## password-mask-analyzer

This tool reads a password file and identifies the top three most common hashcat-style password masks.

## Overview

A password mask (pattern) provides insight into the structure of a password. This tool converts each character in a password into one of the following categories:

?l — Lowercase letters (a-z)

?u — Uppercase letters (A-Z)

?d — Digits (0-9)

?s — Special characters (all non-alphanumeric)

#Example

Password: P@ssw0rd!23$
Mask: ?u?s?l?l?l?d?l?l?s?d?d?s

## How to Use

#Clone the repository:
git clone https://github.com/port-zero-cyber/password-mask-analyzer.git
cd password-mask-analyzer

#Add or replace the 'realistic_mixed_length_passwords.txt' file with your own list of passwords.

#Run the script:
python3 password_mask_counter.py

#Output example:

Top 3 Password Masks
--------------------
1. ?d?d?d?d?d?d   : 5
2. ?l?l?l?l?l?l   : 3
3. ?u?l?l?l?l?l?s?s : 2
