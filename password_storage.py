import json
import os

def save_password(account, password):
    encrypted_password = encrypt_password(password)
    if os.path.exists("passwords.json"):
        with open("passwords.json", "r") as file:
            passwords = json.load(file)
    else:
        passwords = {}

    passwords[account] = encrypted_password.decode()
    with open("passwords.json", "w") as file:
        json.dump(passwords, file)

def retrieve_password(account):
    if os.path.exists("password.json"):
        with open("password.json", "r") as file:
            password = json.load(file)
            encrypted_password = passwords.get(account)
            if encrypted_password:
                return decrypt_password(encrypted_password.encode())
            else:
                    return "Account not found."
    else:
        return "No passwords saved yet."
