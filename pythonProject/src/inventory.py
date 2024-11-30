import config
from game_effects import timed_print
from abstract_classes import Storage


class Inventory(Storage): # player inventory class
    def __init__(self, items=None): # Initialises inventory
        if items is None:
            items = []
        self.__items = items # User items
        self.__max_inventory_size = 3 # Default maximum inventory size

    @property
    def max_inventory_size(self):
        # Getter for the maximum inventory size.
        return self.__max_inventory_size

    @max_inventory_size.setter
    def max_inventory_size(self, amount):
        # Setter for the maximum inventory size.
        self.__max_inventory_size = amount

    def remove_item(self, item): # Removes a specific item from the inventory by finding its index.
        self.__items.pop(self.items.index(item))

    def use_item(self, index): # Removes and returns an item from the inventory by index.
        return self.__items.pop(index)

    @property
    def items(self): # Getter for the list of inventory items.
        return self.__items

    @items.setter
    def items(self, item): # Adds an item to the inventory if space is available.
        if len(self.__items) < self.max_inventory_size:
            self.__items.append(item)
        else:
            timed_print("Inventory full cannot add item.")

    def display_items(self): # Displays the inventory items

        for i, item in enumerate(self.items):
            timed_print(f"{i + 1}: {item}")

    def clear(self): # Clears all items from the inventory
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
            "items": self.items,
            "max_inventory_size": self.max_inventory_size
        }

    @classmethod
    def decode(cls, data):
        """ decodes json object of class inventory into class inventory"""
        instance = Inventory(data["items"])
        instance.max_inventory_size = data["max_inventory_size"]
        return instance



class Chest(Storage):
    """ Represents a chest that can store items"""
    def __init__(self, items=None):
        if items is None:
            self.__items = []
        else:
            self.__items = items


    @property
    def items(self): # Getter for a list of items
        return self.__items

    @items.setter
    def items(self, item): # Adds an item to the chest
        self.__items.append(item)


    def display_items(self): # Displays the items in the chest with their index
        for i, item in enumerate(self.__items):
            timed_print(f"{i + 1}: {item}", delay=0.01)

    def pick_items(self, index): #Removes and returns an item from the chest
        if 0 <= index < len(self.__items):
            return self.__items.pop(index)
        return None

    def clear(self): #Clears all items from the chest
        self.__items = []

    def encode(self): # Encodes the chest into a JSON-compatible object.
        """ encodes chest into json object"""
        return {
            "items": self.items
        }

    @classmethod
    def decode(cls, data): # Decodes a JSON-compatible object into a Chest instance.
        """ decodes json object of class inventory into class inventory"""
        instance = Chest(data["items"])
        return instance



