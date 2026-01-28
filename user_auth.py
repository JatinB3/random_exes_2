"""
Author: Jatin
Date: 28 Jan 2026

Description: This script serves as a wrapper to authenticate users before allowing access to the main application.
It prompts the user for a password and only runs the main application if the correct password is provided
"""

import getpass
import multiprocessing
import sys
import data_processor

def authenticate_user():
    correct_password = "123"  # Replace with your desired password
    attempts = 3

    for attempt in range(attempts):
        password = getpass.getpass("Enter the password to run the application: ") # Prompt for password without echoing
        if password == correct_password:
            print("Authentication successful. Starting the application...")
            return True
        else:
            print(f"Incorrect password. You have {attempts - attempt - 1} attempts left.")

    print("Authentication failed. Exiting the application.")
    return False

if __name__ == "__main__":
    multiprocessing.freeze_support()  # For Windows support when using multiprocessing
    try:
        if authenticate_user():
            data_processor.run_main()
        else:
            print("wrong password...")
            sys.exit(1)
    except (KeyboardInterrupt, SystemExit):
        print("\nApplication terminated by user.")
        sys.exit(0)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
