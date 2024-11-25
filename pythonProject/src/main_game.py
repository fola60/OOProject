#Main game will be in this file
import json
import os
import time
from game_effects import timed_print
from areas import PyramidGame
from characters import User


class Game:
    def __init__(self):
         # initializes game variables
        self._current_location = PyramidGame().current_location
        user_name = input("Enter name: ")
        self.user = User(user_name, self._current_location)
        self.checkpoint = self.user.encode()
        self.ran = False
        self.running = False



    def save_checkpoint(self):
        """ Saves current game state at each door entry """
        self.checkpoint = self._user.encode()


    def return_to_checkpoint(self):
        """ returns game state to last checkpoint"""
        from src.characters import User
        self._user = User.decode(self.checkpoint)
        self._current_location = self._user.location


    @classmethod
    def save(cls, user):
        """ Saves current game
            Areas, user"""
        try:
            choice = int(input("Choose save file, from 1 - 3"))
            if 1 <= choice <= 4:
                with open(f"./Saves/save_{choice}.json", 'w') as json_file:
                    json.dump(user.encode(), json_file, indent=4)
            else:
                with open(f"./Saves/save_3.json", 'w') as json_file:
                    json.dump(user.encode(), json_file, indent=4)
            timed_print("Saving Game.....", delay=0.3)
        except ValueError:
            timed_print("Invalid input.")



    def load(self, load_data):
        """ Loads previous saves """
        self.ran = True
        self.running = True


    def introduction(self):
        pass

    def run(self):
        """ runs game loop"""
        # game intro
        if not self.ran:
            while True:
                timed_print("Enter 'l' to load previous save, enter 's' to start game")
                choice = input(": ").lower()
                if choice == 'l':
                    if len(os.listdir("./Saves")) < 1: # if no save exists start game from beginning
                        timed_print("No available saves.")
                        self.introduction()
                        self.ran = True
                        self.running = True
                        break
                    while True: # loop until user enters correct save number
                        try:
                            print("Available saves: ")
                            for filename in os.listdir("./Saves"):
                                timed_print(filename)
                            save_choice = int(input("Enter save number: "))
                            if not (os.path.isfile(f"./Saves/save_{save_choice}.json")):
                                timed_print("Save doesnt exist, try a different save.")
                            else:
                                with open(f"./Saves/save_{save_choice}.json", 'r') as json_obj:
                                    self.load(json_obj)
                                break

                        except ValueError:
                            timed_print("Incorrect input, loading first save")
                            save_choice = 1
                            with open(f"./Saves/save_{save_choice}.json", 'r') as json_obj:
                                self.load(json_obj)
                            break

                    break
                elif choice == 's':
                    self.ran = True
                    self.running = True
                    break
                else:
                    timed_print("Invalid input, try again")
        # game running
        else:
            print("empty")

game = Game()
game.run()