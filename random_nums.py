import random
import time

def generate_random_numbers():
    random_numbers = [random.randint(1, 100) for _ in range(10)]
    return random_numbers

if __name__ == "__main__":
    try:
        while True:
            nums = generate_random_numbers()
            print("Generated random numbers:", nums)
            time.sleep(5)  # Wait for 5 seconds before generating again
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")