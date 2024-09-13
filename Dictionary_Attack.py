import time

def dictionary_attack(target_password, dictionary_file):
    attempts = 0
    start_time = time.time()
    
    # Open dictionary file and go down the line one by one, removing the \n character after each line.
    with open(dictionary_file, 'r') as file:
        for password in file:
            attempts += 1
            password = password.strip()


            # Check if password in dictionary matches target password
            if password == target_password:
                end_time = time.time()
                time_taken = end_time - start_time
                return attempts, time_taken, password
            
    return attempts, time.time() - start_time, None
def main():
    target_password = input("Enter the target password to find: ")
    dictionary_file = input("Enter the path to the dictionary file: ")

    attempts, time_taken, found_password = dictionary_attack(target_password, dictionary_file)

    if found_password:
        print(f"Password found: {found_password}")
        print(f"Attempts taken: {attempts}")
        print(f"Time taken: {time_taken:.4f} seconds")
    else:
        print(f"Password not found in the dictionary after {attempts} attempts.")
        print(f"Time taken: {time_taken:.4f} seconds")


if __name__ == "__main__":
    main()
