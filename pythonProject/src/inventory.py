from game_effects import timed_print
from abstract_classes import Storage


class Inventory(Storage):
    def __init__(self, items=None):
        if items is None:
            items = []
        self.__items = items # User items

    def use_item(self, index):
        return self.__items.pop(index)

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, item):
        self.__items.append(item)

    def display_items(self):
        items = self.__items
        for i, item in enumerate(items):
            timed_print(f"{i + 1}: {item}")

    def encode(self):
        """ encodes inventory into json object"""
        return {
            "items": self.items
        }

    @classmethod
    def decode(self, data):
        """ decodes json object of class inventory into class inventory"""
        instance = Inventory(data["items"])
        return instance


class Chest(Storage):
    def __init__(self):
        self.__items = []

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, item):
        self.__items.append(item)

    def display_items(self):
        for i, item in enumerate(self.__items):
            timed_print(f"{i + 1}: {item}")

    def pick_items(self, index):
        if 0 <= index < len(self.__items):
            return self.__items.pop(index)
        return None

"""chest = Chest()
chest.items = "NUKE"

chest.display_items()
item = chest.pick_items(0)
if item:
    Inventory.items = item"""

"""TORCH (can light mummy on fire),"""


