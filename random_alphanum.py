"""
Author: Jatin
Date: 28 Jan 2026

Description: This is a program that generates random alphanumeric strings by combining random numbers and letters.
"""

import random
import string
import time

def generate_random_alphanumeric():
    alphanums = [random.choice(string.ascii_letters + string.digits) for _ in range(10)] # Generate 10 random alphanumeric characters
    return alphanums

if __name__ == "__main__":
    try:
        while True:
            alphanum = generate_random_alphanumeric()
            print("Generated random alphanumeric string:", alphanum)
            time.sleep(2)  # Wait for 2 seconds before generating again
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
