from cryptography.fernet import Fernet

# Load encryption key file
def load_key():
    return open("secret.key", "rb").read()

# Encrypt Password
def encrypt_password(password):
    key = load_key()
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())
    return encrypted_password

# Decrypt Password
def decrypt_password(encrypted_password):
    key = load_key()
    fernet = Fernet(key)
    decrypted_password = fernet.decrypt(encrypt_password).decode()
    return decrypted_password
    