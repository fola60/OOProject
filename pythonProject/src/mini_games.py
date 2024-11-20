#Mini-games will be defined in this file and imported for usage

import time
import sys
import select
import random
from game_effects import timed_print


def input_with_timeout(prompt, timeout):
    print(prompt, end='', flush=True)
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
        guess = input("Rearranged word: ")
        return guess == word # checks if guess was correct return True if it is and false otherwise


    def quick_click(self, msg="", time=2):
        # game where player has to input a charcter withing {time} time
        timed_print(msg)  
        try:
            # waits for user input for {time} seconds
            user_input = input_with_timeout("Enter the letter G quick!!", timeout=time)
            return 'G' == user_input.strip()  # .strip() removes spaces around char
        except Exception as e:
            print(f"Error: {e}")
            return False


    def quiz(self, qs:str , answers:[], answer: int):
        # function that displays multiple choice question and checks for correct answer
        # Question defined in qs, multiple choices defined in answers, answer index is answer


        timed_print(qs,delay=0.2)
        timed_print("....", delay=0.2)

        for i, ans in enumerate(answers):
            # printing potential answers
            timed_print(f"{i + 1}. {ans}", delay=0.05)

        try:
            # prompting user input
            choice = int(input("Enter the number of question you think is correct."))

            # checking invalid input
            if choice > len(answers) or choice < 1:
                return False
            return choice == answer + 1  # return True if user input was correct, + 1 to make up for index
        except ValueError:
            print("invalid input")
            return False


