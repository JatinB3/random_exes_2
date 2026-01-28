"""
Author: Jatin
Date: 28 Jan 2026

Description: This is the main application that generates random numbers and letters using multiprocessing. 
It runs three separate processes to generate random numbers, letters, and alphanumerics every 2 seconds.

"""
import multiprocessing
import time
from random_nums import generate_random_numbers 
from random_letters import generate_random_letters
from random_alphanum import generate_random_alphanumeric

def generate_numbers_periodically(stop_event):
    while not stop_event.is_set():
        nums = generate_random_numbers()
        print("Generated random numbers:", nums)
        time.sleep(2)  # Wait for 2 seconds before generating again
    

def generate_letters_periodically(stop_event):
    while not stop_event.is_set():
        letters = generate_random_letters()
        print("Generated random letters:", letters)
        time.sleep(2)  # Wait for 2 seconds before generating again

def generate_random_alphanumeric_periodically(stop_event):
    while not stop_event.is_set():
        alphanum = generate_random_alphanumeric()
        print("Generated random alphanumeric string:", alphanum)
        time.sleep(2)  # Wait for 2 seconds before generating again

# if __name__ == "__main__":
#     multiprocessing.freeze_support()  # For Windows support when using multiprocessing
def  run_main():
    stop_event = multiprocessing.Event()

    number_process = multiprocessing.Process(target=generate_numbers_periodically, args=(stop_event,), daemon=True)
    letter_process = multiprocessing.Process(target=generate_letters_periodically, args=(stop_event,), daemon=True)
    alphanum_process = multiprocessing.Process(target=generate_random_alphanumeric_periodically, args=(stop_event,), daemon=True)

    number_process.start()
    letter_process.start()
    alphanum_process.start()

    try:
        while True:
            time.sleep(1)  # Keep the main program running
    except KeyboardInterrupt:
        print("\nMain program terminated by user. Stopping child processes...")
        stop_event.set()
        number_process.join()
        letter_process.join()
        alphanum_process.join()
        print("All processes have been terminated.")
        

