# This file will contain all characters from which other files can import
from abc import abstractproperty

from abstract_classes import Character
from game_effects import timed_print
from inventory import Inventory

class User(Character):
    def __init__(self, name, location, damage):
        self.__location = location
        self.name = name # player name
        self.__health = 5 # player health
        self.inventory = Inventory() # player's inventory
        self.__damage = damage
        self.status = True # true for alive false for dead

    def take_damage(self, damage): #
        self.__health -= damage

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, amount):
        if amount <= 0: # Checks if health is zero or below
            self.__health = 0
            self.status = False
            self.process_death() # Calls death function
        else:
            self.__health = amount

    def process_death(self):
        timed_print(f"{self.name} has perished!")
        #clear inventory
        #reset location back to most recent death



class Enemy(Character):
    def __init__(self, dmg, name, health):
        self.name = name
        self.__health = health
        self.__damage = dmg
        self.status = True

    def battle(self, User):

        timed_print(f"{self.name} attacks {User.name} for {self.__damage} damage!")




class NPC(Character):
    def __init__(self, name, dialog):
        self.name = name
        self.__dialog = dialog
        self._interacted = False


    def interact(self):
        if not self._interacted:
            interaction = f"{self._name}: {self._dialog}"
            self._interacted = True

        return interaction
    # npc advises you on which path to take and what items to take, the npc can lie to you aswell

"""SKELETON,MUMMY,PHAROAH(boss),TOMB WARDEN(mini-boss)""" #enemies
"""SHADOW SCRIBE,FRIENDLY SPIRIT(tells truth), EVIL SPIRIT(lies), SPIRIT(sometimes lies)""" #npcs
