"""
Author: Jatin
Date: 28 Jan 2026

Description: This is a program that generates random letters.
"""

import random
import time
import string

def generate_random_letters():
    random_letters = [random.choice(string.ascii_letters) for _ in range(10)] # Generate 10 random letters
    return random_letters

if __name__ == "__main__":
    try:
        while True:
            letters = generate_random_letters()
            print("Generated random letters:", letters)
            time.sleep(2)  # Wait for 2 seconds before generating again
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
