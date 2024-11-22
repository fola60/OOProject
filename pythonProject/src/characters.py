# This file will contain all characters from which other files can import
from abc import abstractproperty

from abstract_classes import Character
from game_effects import timed_print
from inventory import Inventory

class User(Character):
    def __init__(self, name, location, damage):
        self.__location = location
        self.name = name  # player name
        self.__health = 5  # player health
        self.inventory = Inventory()  # player's inventory
        self.__damage = damage  # player damage
        self.status = True  # true for alive false for dead

    def introduction(self):
        pass

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
    def damage(self):
        return self.__damage  # Returns the player's damage value

    def process_death(self):
        timed_print(f"{self.name} has perished!")
        # clear inventory
        # reset location back to most recent death



class Enemy(Character):
    def __init__(self, name, health, damage):
        self.name = name
        self.__health = health
        self.__damage = damage
        self.status = True

    def introduction(self):
        pass

    def take_damage(self, damage):
        self.__health -= damage
        if self.__health <= 0:
            self.__health = 0
            self.status = False

    @property
    def health(self):
        return self.__health

    @property
    def damage(self):
        return self.__damage




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

class Skeleton(Enemy):
    def __init__(self):
        super().__init__(name="Skeleton", health=5, damage=2)

    def introduction(self):
        pass


class Mummy(Enemy):
    def __init__(self):
        super().__init__(name="Mummy", health=7, damage=3)

    def introduction(self):
        pass


class Pharaoh(Enemy):
    def __init__(self):
        super().__init__(name="Pharaoh", health=10, damage=5)

    def introduction(self):
        pass