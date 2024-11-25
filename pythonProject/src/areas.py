"""
A location class for the locations, it will have left and right

"""

from abc import ABC, abstractmethod
from config import damage_map
from abstract_classes import Location




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
        guard_fight = Battle(player, enemy)
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


