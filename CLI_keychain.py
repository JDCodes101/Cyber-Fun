import argparse
import json
import os
import random
import string
import time
from cryptography.fernet import Fernet
from Password_Strength_Checker import check_password_strength
from Dictionary_Attack import dictionary_attack

# Define functions for key management

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("Key generated and saved to 'secret.key'.")

def load_key():
    if not os.path.exists("secret.key"):
        print("Key file 'secret.key' not found. Generating a new key.")
        generate_key()
    return open("secret.key", "rb").read()

# Define functions for password operations

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for i in range(length))

def encrypt_password(password):
    key = load_key()
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password):
    key = load_key()
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypted_password).decode()
    return decrypted_password

def save_password(username, encrypted_password):
    data = {username: encrypted_password.decode()}  # Convert encrypted_password bytes to string
    with open("passwords.json", "a") as file:
        json.dump(data, file)
        file.write("\n")  # Write each entry on a new line

def retrieve_password(username):
    with open("passwords.json", "r") as file:
        for line in file:
            data = json.loads(line)  # Load the JSON data from each line
            if username in data:
                return data[username].encode()  # Return the encrypted password bytes
    return None  # If the username is not found

def view_passwords():
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            for line in file:
                data = json.loads(line)  # Load the JSON data from each line
                for username, encrypted_password in data.items():
                    print(f"Username: {username}, Encrypted Password: {encrypted_password}")
    else:
        print("No password file found.")

def main():
    while True:
        print("\nPassword Manager CLI Tool")
        print("1. Generate a Password")
        print("2. Save a Password")
        print("3. Retrieve a Password")
        print("4. Check Password Strength")
        print("5. Run Dictionary Attack")
        print("6. View Stored Passwords")
        print("7. Generate Encryption Key")
        print("8. Exit")

        choice = input("Select an option (1-8): ")

        if choice == "1":
            password = generate_password()
            print(f"Generated password: {password}")

        elif choice == "2":
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            encrypted = encrypt_password(password)
            save_password(username, encrypted)
            print(f"Password for {username} saved successfully.")

        elif choice == "3":
            username = input("Enter the username: ")
            encrypted_password = retrieve_password(username)
            if encrypted_password:
                decrypted = decrypt_password(encrypted_password)
                print(f"Retrieved password for {username}: {decrypted}")
            else:
                print(f"Password for {username} not found.")

        elif choice == "4":
            username = input("Enter the username of the account to check password strength: ")
            encrypted_password = retrieve_password(username)
            if encrypted_password:
                password = decrypt_password(encrypted_password)
                result = check_password_strength(password)
                print(f"Password strength for {username}: {result}")
            else:
                print(f"Password for {username} not found.")

        elif choice == "5":
            password = input("Enter the password to crack: ")
            dictionary_file = input("Enter the path to the dictionary file: ")
            start_time = time.time()
            attempts, time_taken, found_password = dictionary_attack(password, dictionary_file)

            if found_password:
                print(f"Password found: {found_password}")
                print(f"Attempts taken: {attempts}")
                print(f"Time taken: {time_taken:.4f} seconds")
            else:
                print(f"Password not found in the dictionary after {attempts} attempts.")
                print(f"Time taken: {time.time() - start_time:.4f} seconds")

        elif choice == "6":
            view_passwords()

        elif choice == "7":
            generate_key()

        elif choice == "8":
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please select a number between 1 and 8.")

if __name__ == "__main__":
    main()
