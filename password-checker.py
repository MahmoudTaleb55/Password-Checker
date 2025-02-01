import re

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password must be at least 8 characters long."
    if not re.search("[a-z]", password):
        return "Weak: Password must contain lowercase letters."
    if not re.search("[A-Z]", password):
        return "Weak: Password must contain uppercase letters."
    if not re.search("[0-9]", password):
        return "Weak: Password must contain digits."
    if not re.search("[@#$%^&+=]", password):
        return "Weak: Password must contain special characters."
    return "Strong Password!"

password = input("Enter a password to check: ")
print(check_password_strength(password))