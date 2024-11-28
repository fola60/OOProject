#All abstract classes will be defined in this file and other files will import for usage
from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self):
        self.interacted = False

    @abstractmethod
    def introduction(self):
        pass


class Location(ABC):
    def __init__(self, door_number):
        self._left = None
        self._right = None
        self._door_number = door_number
        self._minigame = None

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
    def interact_with_npc(self, npc):
        """ Gain information from local npc"""
        pass

    def encode(self):
        """ encodes class into json object"""
        return {
            "door_number": self._door_number,
            "left": self._left.encode() if self._left else None,
            "right": self._right.encode() if self._right else None,
            "mini_game": self._minigame,
        }

    @abstractmethod
    def view_chest(self, chest):
        pass



class Storage(ABC):

    @abstractmethod
    def items(self):
        pass

    @abstractmethod
    def clear(self):
        pass