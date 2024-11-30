#All abstract classes will be defined in this file and other files will import for usage
from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self):
        self.interacted = False # Checks whether the character has been interacted with.


    @abstractmethod
    def introduction(self): # Character introduction
        pass


class Location(ABC):
    def __init__(self, door_number):
        self._left = None # left location
        self._right = None # right location
        self._door_number = door_number # Unique door number for this location
        self._minigame = None # Associated minigame for this location
        self.enemy = None # Enemy at this location
        self.chest = None # Chest at this location
        self.end_of_game = False

    @property
    @abstractmethod
    def left(self):
        """Property that gets the left location"""
        pass

    @property
    @abstractmethod
    def right(self):
        """Property that gets the right location"""
        pass

    @left.setter
    @abstractmethod
    def left(self, area):
        """Setter that sets left area"""
        pass

    @right.setter
    @abstractmethod
    def right(self, area):
        """Setter that sets right area"""
        pass

    @abstractmethod
    def play_minigame(self):
        """Method to play the minigame at this location"""
        pass

    @abstractmethod
    def fight_guard(self, player, enemy):
        """ Before player can choose room they must fight and defeat the enemy"""
        pass

    @abstractmethod
    def interact_with_npc(self):
        """ Gain information from local npc"""
        pass

    def encode(self):
        """ encodes class into json object"""

        return {
            "door_number": self._door_number,
            "left": self._left.encode() if self._left else None,
            "right": self._right.encode() if self._right else None,
            "enemy": self.enemy.encode(),
            "chest": self.chest.encode(),
            "end_of_game": self.end_of_game
        }

    @abstractmethod
    def view_chest(self, chest): # Handles the viewing of a chest at this location
        pass



class Storage(ABC):
    @abstractmethod
    def items(self): # Abstact method to get items in storage
        pass

    @abstractmethod
    def clear(self): # Abstract method to clear all items from storage
        pass