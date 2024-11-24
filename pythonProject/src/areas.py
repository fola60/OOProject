"""
A location class for the locations, it will have left and right

"""

from abc import ABC, abstractmethod
from src.config import damage_map


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
    def interact_with_npc(self):
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
    def view_chest(self):
        pass


class Door(Location):
    def __init__(self, door_number):
        super().__init__(door_number)
        self.end_of_game = False

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, area):
        if area is not None:
            if not isinstance(area, Location):
                raise ValueError("Left must be a Location")
            area._parent = self
        self._left = area

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, area):
        if area is not None:
            if not isinstance(area, Location):
                raise ValueError("Right must be a Location")
            area._parent = self
        self._right = area

    def play_minigame(self):
        if self._minigame is None:
            return "No minigame at this door!"
        return self._minigame.play()

    def fight_guard(self, player, enemy):
        from battle import Battle # to avoid circular import
        guard_fight = Battle(player, enemy, damage_map)
        guard_fight.start_battle()

    def interact_with_npc(self):
        pass

    def view_chest(self):
        pass


    @classmethod
    def decode(cls, data):
        """ decodes json object to Class location"""
        instance = Door(data["door_number"])
        instance._left = cls.decode(data["left"]) if data["left"] else None
        instance._right = cls.decode(data["right"]) if data["right"] else None
        instance._minigame = data["mini_game"]
        return instance

class PyramidGame:
    def __init__(self):
        self.current_location = None
        self.build_pyramid()

    def build_pyramid(self):
        # Create all doors (0-6 as in your example)
        doors = [Door(i) for i in range(7)]

        # Build the pyramid structure
        # Level 0 (top)
        self.root = doors[0]

        # Level 1
        self.root.left = doors[1]
        self.root.right = doors[2]

        # Level 2 (bottom)
        doors[1].left = doors[3]
        doors[1].right = doors[4]
        doors[2].left = doors[5]
        doors[2].right = doors[6]

        for door in range(3, 7):
            doors[door].end_of_game = True


        # Start at bottom left
        self.current_location = doors[0]


