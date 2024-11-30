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
        timed_print("Etching hieroglyphs to mark the passage and seal our fate...")
        self.checkpoint = self.user.encode()
        self.stage_checkpoint = self.stage

    def return_to_checkpoint(self):
        """ returns game state to last checkpoint"""
        from characters import User
        self.user = User.decode(self.checkpoint)
        self._current_location = self.user.location
        self.stage = self.stage_checkpoint
        self.run()



    @classmethod
    def save(cls, user):
        """ Saves current game
            Areas, user"""
        try:
            choice = int(input("Choose save file, from 1 - 3: "))
            if 1 <= choice <= 4:
                with open(f"./Saves/save_{choice}.json", 'w') as json_file:
                    json.dump(user.encode(), json_file, indent=4)
            else:
                with open(f"./Saves/save_3.json", 'w') as json_file:
                    json.dump(user.encode(), json_file, indent=4)
            timed_print("Saving Game.....", delay=0.1)
        except ValueError:
            timed_print("Invalid input.")



    def load(self, load_data):
        """ Loads previous saves """
        load_data = json.load(load_data)
        self.user = User.decode(load_data)
        self._current_location = self.user.location
        self.ran = True
        self.running = True
        self.run()


    def introduction(self):
        timed_print(f"Greetings {self.user.name}!")
        timed_print("You are a passionate archaeologist, renowned for his research of ancient Egyptian history.")
        timed_print("You have spent the last two decades studying texts, deciphering hieroglyphs, and uncovering the secrets of Egypt’s past.", delay=0.015)
        timed_print("Lately, rumors have surfaced of a hidden treasure said to be of unimaginable power, buried deep within the tombs of to what is known now as The Last Pharaoh.", delay=0.015)
        timed_print("Given your extensive knowledge you know of the whereabouts of his tomb, giving you a headstart from other tomb raiders", delay=0.015)
        timed_print("Driven by a thirst for discovery and the possibility of revealing an ancient secret that could change history, you embark on this treacherous journey into the tombs", delay=0.015)

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
                        continue
                    while True: # loop until user enters correct save number
                        try:
                            timed_print("Available saves: ")
                            for filename in os.listdir("./Saves"):
                                print(filename)
                            save_choice = int(input("Enter save number: "))
                            if not (os.path.isfile(f"./Saves/save_{save_choice}.json")):
                                timed_print("Save doesnt exist, try a different save.")
                                continue
                            else:
                                with open(f"./Saves/save_{save_choice}.json", 'r') as json_obj:
                                    self.load(json_obj)
                                return

                        except ValueError:
                            timed_print("Incorrect input, loading first save")
                            save_choice = 1
                            with open(f"./Saves/save_{save_choice}.json", 'r') as json_obj:
                                self.load(json_obj)
                            return


                elif choice == 's':
                    self.ran = True
                    self.running = True
                    self.introduction()
                    self.run()
                    return
                else:
                    timed_print("Invalid input, try again")
        # game running
        else:
            if self.stage == 1:
                while True:
                    choice = input("Enter 'l' to load previous save, 't' to check status,'r' to return to checkpoint,\n 'i' to investigate area, 's' to save the current game, 'c' to consume items and 'e' to equip items.",)
                    if choice == 'l':
                        if len(os.listdir("./Saves")) < 1:  # if no save exists start game from beginning
                            timed_print("No available saves.")
                            continue
                        timed_print("Available saves: ")
                        for filename in os.listdir("./Saves"):
                            print(filename)
                        try:
                            save_choice = int(input("Enter save number: "))
                            if not (os.path.isfile(f"./Saves/save_{save_choice}.json")):
                                timed_print("Save doesnt exist, try a different save.")
                            else:
                                with open(f"./Saves/save_{save_choice}.json", 'r') as json_obj:
                                    self.load(json_obj)
                                return
                        except ValueError:
                            print("Cant load that save.")
                            continue
                    elif choice == 'e':
                        if not self.user.inventory.get_equippable_items():
                            timed_print("No equipabble items in inventory.")
                            continue

                        for i, item in enumerate(self.user.inventory.get_equippable_items()):
                            timed_print(f"{i + 1} {item}")

                        try:
                            item_id = int(input("Choose ID of item you want to equip."))

                        except ValueError:
                            timed_print("Cant choose that item")
                            continue
                        self.user.equip(self.user.inventory.get_equippable_items()[item_id - 1])
                        continue
                    elif choice == 'c':
                        if not self.user.inventory.get_consumable_items():
                            timed_print("No consumable items in inventory.")
                            continue

                        for i, item in enumerate(self.user.inventory.get_consumable_items()):
                            timed_print(f"{i + 1} {item}")

                        try:
                            item_id = int(input("Choose ID of item you want to consume."))

                        except ValueError:
                            timed_print("Cant choose that item")
                            continue
                        self.user.equip(self.user.inventory.get_consumable_items()[item_id - 1])
                        continue


                    elif choice == 'r':
                        self.return_to_checkpoint()
                        return
                    elif choice == 'i':
                        timed_print(self._current_location.description_stage1)
                        choice = input(f"Enter 'i' to interact with {self._current_location.npc.name}, 'd' to explore the the chest ,'a' to advance on to the next stage")
                        if choice == 'i':
                            self._current_location.interact_with_npc()
                            continue
                        elif choice == 'd':
                            self.user.interact_with_chest()
                            continue
                        elif choice == 'a':
                            timed_print(f"{self.user.name} continues on to the next stage!")
                            self.stage = 2
                            self.run()
                            return

                    elif choice == 's':
                        Game.save(self.user)
                        continue

                    elif choice == 't':
                        self.user.check_status()
                        continue
                    else:
                        timed_print("You cant do that!")
                        continue
            # npc interaction or chest discovery or load or save
            elif self.stage == 2:
                self.save_checkpoint()
                timed_print(self._current_location.description_stage2)
                if not self._current_location.play_minigame():
                    timed_print("You have failed and your remains will be transported to the previous carvings.")
                    self.return_to_checkpoint()
                    return

                time.sleep(2)
                timed_print(f"To advance to the next stage you must face {self._current_location.enemy.name}")

                if not self._current_location.fight_guard(self.user, self._current_location.enemy):
                    timed_print("You have failed and your remains will be transported to the previous carvings.")
                    self.return_to_checkpoint()
                    return

                if not self._current_location.end_of_game:
                    choice = input("Enter 'l' to go to the left path and 'r' to go to the right path.")
                    if choice == 'l':
                        timed_print("User goes down the left path.")
                        self.user.location = self.user.location.left
                        self._current_location = self.user.location
                        self.stage = 1
                        self.save_checkpoint()
                        self.run()
                        return
                    elif choice == 'r':
                        timed_print("User goes down the right path.")
                        self.user.location = self.user.location.right
                        self._current_location = self.user.location
                        self.stage = 1
                        self.save_checkpoint()
                        self.run()
                        return
                    else:
                        timed_print("User goes down the right path.")
                        self.user.location = self.user.location.right
                        self._current_location = self.user.location
                        self.stage = 1
                        self.save_checkpoint()
                        self.run()
                        return
                else:
                    # End game win message
                    timed_print("The last Pharaoh collapses to his knees in defeat. His body turns into a swirling cloud of dust."
                                "\nFrom the remnants, a magnificent key tumbles to the ground, crafted of pure gold"
                                "\nAt the far end of the tomb, you discover a keyhole embedded in a massive stone door."
                                "\nWith a deep, resonant click, the key unlocks the ancient mechanism."
                                "\nThe heavy door groans open, revealing a chamber bathed in ethereal light."
                                "\nBefore you lies the Fountain of Eternal Power—a shimmering pool said to grant unimaginable strength and wisdom to those who drink from it. "
                                "\nAround the chamber are treasures beyond measure: golden artifacts, bejeweled relics, and scrolls containing secrets lost to time. "
                                "\nBut the fountain’s glow pulls at your very soul, offering a choice that could change the fate of kingdoms", delay=0.015)
                    return

game = Game()
game.run()