#Main game will be in this file
import json

from game_effects import timed_print
from src.areas import PyramidGame


class Game:
    def __init__(self, user):
         # initializes game variables
        self._current_location = PyramidGame().current_location
        self._user = user

    def save_checkpoint(self):
        """ Saves current game state at each door entry """
        pass

    def return_to_checkpoint(self):
        """ returns game state to last checkpoint"""
        pass

    @classmethod
    def save(cls, user):
        """ Saves current game
            Areas, user"""
        try:
            choice = int(input("Choose save file, from 1 - 3"))
            if 1 <= choice <= 4:
                with open(f"./Saves/save_{choice}.json", 'w') as json_file:
                    json.dump(user.encode(), indent=4)
            else:
                with open(f"./Saves/save_3.json", 'w') as json_file:
                    json.dump(user.encode(), indent=4)
        except ValueError:
            timed_print("Invalid input.")


    @classmethod
    def load(self):
        """ Loads previous saves """


    def initialize(self):
        """initalizes game variables"""
        pass

    def run(self):
        pass