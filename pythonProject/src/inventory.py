import config
from game_effects import timed_print
from abstract_classes import Storage


class Inventory(Storage):
    def __init__(self, items=None):
        if items is None:
            items = []
        self.__items = items # User items
        self.__max_inventory_size = 3

    @property
    def max_inventory_size(self):
        return self.__max_inventory_size

    @max_inventory_size.setter
    def max_inventory_size(self, amount):
        self.__max_inventory_size = amount


    def use_item(self, index):
        return self.__items.pop(index)

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, item):
        if len(self.__items) < self.max_inventory_size:
            self.__items.append(item)
        else:
            timed_print("Inventory full cannot add item.")

    def display_items(self):
        items = self.__items
        for i, item in enumerate(items):
            timed_print(f"{i + 1}: {item}")

    def clear(self):
        self.__items = []


    def get_consumable_items(self):
        """ returns list of consumable items"""
        consumable_items = []
        for item in self.items:
            if item in config.consumable_item_list:  # check if item can be consumer and it to list
                consumable_items.append(item)

        return consumable_items

    def get_equippable_items(self):
        """ returns list of equippable items"""
        equippable_items = []
        for item in self.items:
            if item in config.equippable_item_list: # check if item can be equipped and it to list
                equippable_items.append(item)

        return equippable_items


    def encode(self):
        """ encodes inventory into json object"""
        return {
            "items": self.items
        }

    @classmethod
    def decode(cls, data):
        """ decodes json object of class inventory into class inventory"""
        instance = Inventory(data["items"])
        return instance



class Chest(Storage):
    def __init__(self, items=None):
        if items is None:
            self.__items = []
        else:
            self.__items = items


    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, item):
        self.__items.append(item)

    def display_items(self):
        for i, item in enumerate(self.__items):
            timed_print(f"{i + 1}: {item}", delay=0.01)

    def pick_items(self, index):
        if 0 <= index < len(self.__items):
            return self.__items.pop(index)
        return None

    def clear(self):
        self.__items = []



