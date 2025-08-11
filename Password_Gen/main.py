import string
import secrets

# Step 1 & 2 from before
length = int(input("Enter password length: "))
include_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
include_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
include_digits = input("Include numbers? (y/n): ").lower() == "y"
include_symbols = input("Include symbols? (y/n): ").lower() == "y"

char_pool = ""
if include_lower:
    char_pool += string.ascii_lowercase
if include_upper:
    char_pool += string.ascii_uppercase
if include_digits:
    char_pool += string.digits
if include_symbols:
    char_pool += string.punctuation

# Step 3: Generate the password using secrets
password = ''.join(secrets.choice(char_pool) for _ in range(length))

print("Generated password:", password)
