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
        user_name = input("Enter your player's name: ")
        self.user = User(user_name, self._current_location)
        self.checkpoint = self.user.encode()
        self.ran = False
        self.running = False
        self.stage = 1 # stage of location broken into 2 stages
        self.stage_checkpoint = self.stage



    def save_checkpoint(self):
        """ Saves current game state at each door entry """
        timed_print("Saving...")
        self.checkpoint = self.user.encode()
        self.stage_checkpoint = self.stage

    def return_to_checkpoint(self):
        """ returns game state to last checkpoint"""
        from src.characters import User
        self.user = User.decode(self.checkpoint)
        self._current_location = self.user.location
        self.stage = self.stage_checkpoint
        self.run()


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
        self.user = self.checkpoint.decode()
        self._current_location = self.user.location
        self.ran = True
        self.running = True
        self.run()


    def introduction(self):
        timed_print(f"Greetings {self.user.name}!")
        timed_print("You are a passionate archaeologist, renowned for his research of ancient Egyptian history.")
        timed_print("You have spent the last two decades studying texts, deciphering hieroglyphs, and uncovering the secrets of Egypt’s past.")
        timed_print("Lately, rumors have surfaced of a hidden treasure said to be of unimaginable power, buried deep within the tombs of to what is known now as The Last Pharaoh.")
        timed_print("Given your extensive knowledge you know of the whereabouts of his tomb, giving you a headstart from other tomb raiders")
        timed_print("Driven by a thirst for discovery and the possibility of revealing an ancient secret that could change history, you embark on this treacherous journey into the tombs")

    def run(self):
        """ runs game loop"""
        # game intro
        if not self.ran:
            while True:
                timed_print("Enter 'l' to load previous save, enter 's' to start game", delay=0.03)
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
            if self.stage == 1:
                while True:
                    choice = input("Enter 'l' to load previous save, 'r' to return to checkpoint, 'e' to explore area ",)
            # npc interaction or chest discovery or load or save
            elif self.stage == 2:
                self._current_location.play_minigame()
                self._current_location.fight_guard(self.user, self._current_location.enemy)

game = Game()
game.run()