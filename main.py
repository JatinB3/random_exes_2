import multiprocessing
import time
from random_nums import generate_random_numbers 
from random_letters import generate_random_letters

def generate_numbers_periodically():
    try:
        while True:
            nums = generate_random_numbers()
            print("Generated random numbers:", nums)
            time.sleep(5)  # Wait for 5 seconds before generating again
    except KeyboardInterrupt:
        print("\nNumber generation process terminated by user.")

def generate_letters_periodically():
    try:
        while True:
            letters = generate_random_letters()
            print("Generated random letters:", letters)
            time.sleep(5)  # Wait for 5 seconds before generating again
    except KeyboardInterrupt:
        print("\nLetter generation process terminated by user.")

if __name__ == "__main__":
    multiprocessing.freeze_support()  # For Windows support when using multiprocessing
    number_process = multiprocessing.Process(target=generate_numbers_periodically)
    letter_process = multiprocessing.Process(target=generate_letters_periodically)

    number_process.start()
    letter_process.start()

    try:
        number_process.join()
        letter_process.join()
    except KeyboardInterrupt:
        print("\nMain program terminated by user.")
        number_process.terminate()
        letter_process.terminate()