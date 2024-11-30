#Mini-games will be defined in this file and imported for usage

import time
import sys
import select
import random
from game_effects import timed_print

def input_with_timeout(prompt, timeout):
    timed_print(prompt)
    start_time = time.time()
    user_input = ''

    while time.time() - start_time < timeout:
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]: # select.select is a non stopping way to check for input
            char = sys.stdin.read(1) # reads char from input
            user_input += char
            if char == '\n':
                break
    return user_input

class MiniGames:

    def word_jumble(self, word="", msg=""):
        # Takes in word jumbles it ,and you have to guess the word
        timed_print(msg)

        # turns string word into array of characters and shuffles it
        chars = list(word)
        random.shuffle(chars)
        jumbled_word = ''.join(chars)


        timed_print("Unscramble this word: " + jumbled_word, delay=0.3)

        tries = 3
        while tries > 0:
            guess = input("Rearranged word: ")
            if guess == word:
                timed_print("Correct!")
                return True
            else:
                timed_print("Wrong!")
                tries -= 1

        timed_print(f"The correct word was: {word}")
        time.sleep(1)  # clears input buffer
        return False

    def quick_click(self, msg="", time=2):
        # game where player has to input a charcter within {time} time, msg prints at the start of the function
        try:
            # waits for user input for {time} seconds
            timed_print(msg)
            user_input = input_with_timeout("Enter the letter G to disarm it! Quick!!", timeout=time)
            return 'G' == user_input.strip()  # .strip() removes spaces around char
        except Exception as e:
            timed_print(f"Error: {e}")
            return False

        return False

    def quiz(self, qs:str , answers:[], answer: int):
        # function that displays multiple choice question and checks for correct answer
        # Question defined in qs, multiple choices defined in answers, answer index is answer


        timed_print(qs,delay=0.05)
        timed_print("....", delay=0.05)

        for i, ans in enumerate(answers):
            # printing potential answers
            timed_print(f"{i + 1}. {ans}", delay=0.05)

        try:
            # prompting user input
            choice = int(input("Enter the number of question you think is correct."))

            # checking invalid input
            time.sleep(1) # clears input buffer
            if choice > len(answers) or choice < 1:
                return False
            return choice == answer + 1  # return True if user input was correct, + 1 to make up for index
        except ValueError:
            timed_print("invalid input")
            time.sleep(1) # clears input buffer
            return False

    def memory_match(self, msg1, msg2):
        timed_print(msg1) # displays first parameter
        number = random.randint(800000, 999999) # generates random number
        timed_print(f"Quick remember the {msg2}")
        print(number)
        time.sleep(2.5)
        print("\n" * 1000) # moves terminal down to hide number

        tries = 3

        while tries > 0: # loops until user has no more tries
            try:
                guess = int(input("Enter the number: ")) # prompts user for guess
                if guess == number:
                    timed_print("Correct!")
                    return True
                else:
                    tries -= 1
                    if tries:
                        timed_print("Wrong try again!")
            except ValueError: # if user enters non integer
                timed_print("Enter a valid number.")

        timed_print(f"Out of tries! The number was: {number}")
        return False
