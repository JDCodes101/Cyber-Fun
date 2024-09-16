import argparse
from Password_Strength_Checker import check_password_strength
from Dictionary_Attack import dictionary_attack
import time

def main():
    parser = argparse.ArgumentParser(description="Password Cracker & Strength Checker Tool")
    
    # Add mutually exclusive arguments for mode selection
    parser.add_argument(
        "-m", "--mode", 
        choices=["strength", "crack"], 
        required=True, 
        help="Choose 'strength' to check password strength, or 'crack' to run a dictionary attack"
    )

    # Argument for password input (required for both modes)
    parser.add_argument(
        "-p", "--password", 
        type=str, 
        required=True,  # Now required for both modes
        help="The password to check or crack (for strength check)"
    )

    # Argument for dictionary file (required only for dictionary attack)
    parser.add_argument(
        "-d", "--dictionary", 
        type=str, 
        help="Path to the dictionary file (required for dictionary attack)"
    )

    # Parse the arguments
    args = parser.parse_args()

    if args.mode == "strength":
        # Run the password strength checker
        print(f"Checking password strength for: {args.password}")
        result = check_password_strength(args.password)
        print(result)

    elif args.mode == "crack":
        if not args.dictionary:
            print("Error: You must provide a dictionary file for the dictionary attack.")
        else:
            # Run the dictionary attack
            print(f"Attempting to crack the password: {args.password}")
            start_time = time.time()
            attempts, time_taken, found_password = dictionary_attack(args.password, args.dictionary)

            # Print the result of the dictionary attack
            if found_password:
                print(f"Password found: {found_password}")
                print(f"Attempts taken: {attempts}")
                print(f"Time taken: {time_taken:.4f} seconds")
            else:
                print(f"Password not found in the dictionary after {attempts} attempts.")
                print(f"Time taken: {time.time() - start_time:.4f} seconds")

if __name__ == "__main__":
    main()
