import re

def check_password_strength(password):
    min_length = 8
    # If statements 
    if len(password) < min_length:
        return "Weak: Password too short (Must exceed 8 characters!)"
    
    if not re.search("[a-z]", password):
        return "Weak: Add lowercase letters"
    
    if not re.search("[A-Z]", password):
        return "Weak: Add uppercase letters"
    
    if not re.search("[0-9]", password):
        return "Weak: Add numbers"
    
    if not re.search("[@#$%^&+=]", password):
        return "Weak: Add special characters e.g. [@#$%^&+=]"
    
    return "Strong password"

def main():
    while True:
        # Prompts user to either enter password or exit the terminal.
        password = input("Enter a password to check (or type 'exit to quit): ")
        # Check if user wants to exit
        if password.lower() == 'exit':
            print("Programing exiting.")
            break

        # Check password strength
        result = check_password_strength(password)

        # Print result and prompt user if password is weak
        print(result)
        if result == "Strong Password":
            print("Password is Strong!")
            break




if __name__ == "__main__":
    main()
