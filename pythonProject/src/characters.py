# This file will contain all characters from which other files can import
from abc import abstractproperty

from abstract_classes import Character
from game_effects import timed_print
from inventory import Inventory
from src.areas import PyramidGame
import json

class User(Character):
    def __init__(self, name, location):
        self.__location = location # Current player location
        self.name = name  # Player name
        self.__health = 5  # Player health
        self.inventory = Inventory()  # Player's inventory
        self.status = True  # True for alive false for dead


    def introduction(self):
        print(f"{self.name} enters the world at {self.__location}. Good luck!")


    def take_damage(self, damage):
        self.__health -= damage


    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, amount):
        if amount <= 0:  # Checks if health is zero or below
            self.__health = 0
            self.status = False
            self.process_death()  # Calls death function
        else:
            self.__health = amount


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location


    def process_death(self):
        timed_print(f"{self.name} has perished!")
        self.inventory.clear()
        # reset location back to most recent death

    def check_status(self): # Checks current status of Player
        return f"Health: {self.__health},  Inventory: {self.inventory}"


    def encode(self):
        """ encodes character class to json object"""
        return {
            "name": self.name,
            "location": self.location.encode(),
            "health": self.health,
            "status": self.status,
            "inventory": self.inventory.encode()
        }


    @classmethod
    def decode(cls, data=None):
        """ decodes character json object to character class"""
        if data is None:
            data = {}
        from areas import Door
        instance = User(data["name"], Door.decode(data["location"]) )
        instance.health = data["health"]
        instance.inventory = Inventory.decode(data["inventory"])
        instance.status = True

        return instance




class Enemy(Character):
    def __init__(self, name, rank, health, damage):
        self.name = name
        self.rank = rank
        self.__health = health
        self.__damage = damage
        self.status = True

    def introduction(self):
        pass

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, amount):
        if amount <= 0:
            self.__health = 0
            self.status = False
        else:
            self.__health = amount

    @property
    def damage(self):
        return self.__damage

    def take_damage(self, damage):
        self.__health -= damage



class NPC(Character):
    def __init__(self, name, role, dialog):
        self.name = name
        self.role = role
        self.__dialog = dialog
        self._interacted = False


    def interact(self):
        if not self._interacted:
            self.introduction()
            self._interacted = True
        else:
            timed_print("{self.name} has already been interacted with.")


    def introduction(self):
        timed_print(f"Hello my name is {self.name}")



warriors = Enemy("Ancient Egyptian Warriors", "Grunts", 3, 1)
mummy_guardians = Enemy("Mummy Guardians", "Guards", 5, 2)
warden = Enemy("Tomb Warden", "Mini Boss", 7, 3)
pharaoh = Enemy("The Last Pharaoh", "Final Boss",10, 5)
skeleton = Enemy("Skeleton", "guard", 3, 1)

blacksmith = NPC("Hewg",
                 "A skilled blacksmith who has been working for centuries, crafting and maintaining tools, weapons and armour."
                                    "His origin is unknown, all thats known is that he is bound to the tomb and cursed to forever work on his craft ",
                "I forge, for it is my purpose. What can i offer thee")

priestess = NPC("Priestess",
                "Role: A ghost or spirit who once tended to the tomb’s rituals and now offers cryptic advice."
                                        "She is bound to the tomb and may offer clues to solve puzzles.",
                "I can off thee the answer to the riddles but at a cost")

prisoner = NPC("The Prisoner",
               "A former archaeologist or explorer who got trapped inside the tomb long ago."
                                        "He may have valuable information but is wary of helping.",
               "There’s a trap ahead, step on that plate and you’ll need quick hands to survive. ")

