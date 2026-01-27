import random
import time
import string

def generate_random_letters():
    random_letters = [random.choice(string.ascii_letters) for _ in range(10)]
    return random_letters

if __name__ == "__main__":
    try:
        while True:
            letters = generate_random_letters()
            print("Generated random letters:", letters)
            time.sleep(5)  # Wait for 5 seconds before generating again
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")