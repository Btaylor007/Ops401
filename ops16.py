
#!/usr/bin/env python3

import time

def offensive_mode(word_list_path):
    try:
        with open(word_list_path, 'r') as file:
            for word in file:
                word = word.strip()
                time.sleep(0.5)  # Add a delay between words
                print(f"Word: {word}")
    except FileNotFoundError:
        print("Error: Word list file not found.")

def defensive_mode(user_input, word_list_path):
    try:
        with open(word_list_path, 'r') as file:
            word_list = [line.strip() for line in file]

            if user_input in word_list:
                print(f"The word '{user_input}' is recognized.")
            else:
                print(f"The word '{user_input}' is not recognized.")
    except FileNotFoundError:
        print("Error: Word list file not found.")

def main():
    print("Select Mode:")
    print("1. Offensive; Dictionary Iterator")
    print("2. Defensive; Password Recognized")

    mode = input("Enter mode (1 or 2): ")

    if mode == '1':
        word_list_path = input("Enter the path of the word list file: ")
        offensive_mode(word_list_path)
    elif mode == '2':
        user_input = input("Enter a string to check: ")
        word_list_path = input("Enter the path of the word list file: ")
        defensive_mode(user_input, word_list_path)
    else:
        print("Invalid mode. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

attributions
chatgpt.com
bard.com

