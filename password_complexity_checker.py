
import re

def check_password_complexity(password):
    # Criteria initialization
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r' [A-Z]', password) is not None
    lowercase_criteria = re.search(r' [a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    symbol_criteria = re.search(r' [!@#$%^&*(),.?":{}|<>]', password) is not None
    common_word_criteria = not re.search(r'password|123456|qwerty', password)

    # Check all criteria
    complexity = {
        "Length >= 8": length_criteria,
        "Contains uppercase letter": uppercase_criteria,
        "Contains lowercase letter": lowercase_criteria,
        "Contains digit": digit_criteria,
        "Contains symbol": symbol_criteria,
        "Does not contain common words": common_word_criteria,
    }

    # Calculate score
    score = sum(complexity.values())

    # Print criteria and results
    for criterion, met in complexity.items():
        print(f"{criterion}: {'✓' if met else 'X'}")
    print(f"\nPassword complexity score: {score}/6")

    if score == 6:
        print("Password is very strong.")
    elif score >= 4:
        print("Password is strong.")
    elif score >= 2:
        print("Password is weak.")
    else:
        print("Password is very weak.")

    return complexity, score

# Example usage
password = input("Enter a password to check its complexity: ")
check_password_complexity(password)
