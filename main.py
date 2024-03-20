import re
def assess_password_strength(password):
    # Defining criteria
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r'[A-Z]', password)),
        "lowercase": bool(re.search(r'[a-z]', password)),
        "digit": bool(re.search(r'\d', password)),
        "special_character": bool(re.search(r'[!@#$%^&*()_+=\[\]{};:\'",.<>?\\|`~-]', password))
    }
    # Calculating score
    score = sum(criteria.values())

    # Assessing strength
    if score == 5:
        return "Very Strong"
    elif score >= 4:
        return "Strong"
    elif score >= 3:
        return "Moderate"
    elif score >= 2:
        return "Weak"
    else:
        return "Very Weak"

# Enter a password until a strong one is provided
while True:
    password = input("Enter your password: ")
    strength = assess_password_strength(password)
    print("Password strength:", strength)

    if strength in ["Very Strong", "Strong"]:
        break  # Exit the loop if a strong password is provided
    else:
        print("Please enter a stronger password.\n")

