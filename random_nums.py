"""
Author: Jatin
Date: 28 Jan 2026

Description: This is a program that generates random numbers.
"""

import random
import time

def generate_random_numbers():
    random_numbers = [random.randint(1, 100) for _ in range(10)] # Generate 10 random numbers between 1 and 100
    return random_numbers

if __name__ == "__main__":
    try:
        while True:
            nums = generate_random_numbers()
            print("Generated random numbers:", nums)
            time.sleep(2)  # Wait for 2 seconds before generating again
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
