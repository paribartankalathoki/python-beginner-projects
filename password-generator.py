"""
Random Password Generator

This program generates a random password
based on the length entered by the user.
It includes letters, numbers and special characters.
"""

import random

print("\n===== RANDOM PASSWORD GENERATOR =====")

print("\nCreate a random password in seconds!")
print("Choose your desired password length and let Python generate one for you.")

passwordLength = int(input("\nHow long should your password be? "))

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%&!(){}[]?"

password = ""

for i in range(passwordLength):
    password += random.choice(characters)

print("\nYour generated password is:", password)
print("Password length:", passwordLength)

print("\n===== THANK YOU FOR USING THE PROGRAM =====\n\n")