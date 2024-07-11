import re

def check_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[^A-Za-z0-9]', password))
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    if score == 5:
        strength = "Very Strong"
    elif score >= 3:
        strength = "Strong"
    elif score >= 2:
        strength = "Moderate"
    else:
        strength = "Weak"
    return strength

password = input("Enter your password to check its complexity: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")