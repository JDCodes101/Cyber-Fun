import itertools
import string
import time

# Define the variables
target_password = "abc12"
character_set = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

# Brute Force Attack Function
def brute_force_attack(target_password):
    attempts = 0
    start_time = time.time()

    for password_length in range(1, len(target_password) + 1):
        for guess in itertools.product(character_set, repeat=password_length):
            attempts += 1
            guess = ''.join(guess)
            # Verify that guessed password matches target password
            if guess == target_password:
                end_time = time.time()
                time_taken = end_time - start_time
                return attempts, time_taken, guess
    

# Run BFA
attempts, time_taken, guess = brute_force_attack(target_password)
print(f"Password found: {guess}")
print(f"Attempts taken: {attempts}")
print(f"Time taken: {time_taken:.4f} seconds")