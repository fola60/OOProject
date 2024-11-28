# This file will contain all characters from which other files can import

from abstract_classes import Character
from game_effects import timed_print




class User(Character):


    def __init__(self, name, location):
        super().__init__()
        self.__location = location # Current player location
        self.name = name  # Player name
        self.__health = 100  # Player health
        self.max_health_size = 100
        from inventory import  Inventory # Done here to avoid circular imports
        self.inventory = Inventory()  # Player's inventory
        self.status = True  # True for alive false for dead
        self.__weapon = None
        self.__armour = None

    @property
    def weapon(self):
        if self.__weapon is None:
            return 'fist'

        return self.__weapon

    @weapon.setter
    def weapon(self, value):
        self.__weapon = value

    @property
    def armour(self):
        if self.__armour is None:
            return 'body'

    @armour.setter
    def armour(self, armour):
        self.__armour = armour


    def introduction(self):
        timed_print(f"{self.name} enters the world at door {self.__location.door_number}. Good luck!")


    def take_damage(self, damage):
        import config # Done here due to circular imports
        self.__health -= damage / config.armour_negation_map[self.armour] # decrements health based on armour


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
            if 0 < amount < self.max_health_size + 1:
                self.__health = amount


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, location):
        self.__location = location

    def consume(self, item):
        """
        consume item from inventory
        if user consumers non-consumable items they lose health
        """

        import config  # Done here due to circular imports

        if item not in config.consumable_item_list:
            timed_print("Cannot consume that item.")
            return

        if item in config.health_gain_list:
            self.health = self.health + config.health_gain[item]
            timed_print(f"Health increased by {config.health_gain[item]}")
            return

        if item in config.max_health_item_list:
            self.max_health_size = self.max_health_size + config.health_boost[item]
            timed_print(f"Max health increased by {config.health_boost[item]}")
            return

    def equip(self, item):
        import config  # Done here due to circular imports

        if item not in config.equippable_item_list:
            timed_print("Item not equippable")
            return

        if item in config.bag_list:
            self.inventory.max_inventory_size = config.inventory_size_boost[item]
            timed_print(f"Inventory size increased by {config.inventory_size_boost[item]}")
            return

        if item in config.weapon_list:
            self.weapon = item
            timed_print(f"Equipped weapon: {item}")
            return

        if item in config.armour_list:
            self.armour = item
            timed_print(f"Equipped armour: {item}")
            return


    def process_death(self):
        timed_print(f"{self.name} has perished!")


    def check_status(self): # Checks current status of Player
        return f"Health: {self.__health},  Inventory: {self.inventory}"

    def interact_with_chest(self):
        chest = self.location.chest
        chest.display_items()
        while True:
            try:
                if self.inventory.max_inventory_size - len(self.inventory.items):
                    choice = int(input("Choose number of item you want to add to your inventory."))
                    item = chest.pick_items(choice - 1)
                    self.inventory.items = item
                    timed_print(f"You have added {item} to your inventory {self.inventory.max_inventory_size - len(self.inventory.items)} space remaining")
                else:
                    timed_print("No more inventory space.")
                    break
            except ValueError:
                timed_print("Cannot choose that item.")


    def encode(self):
        """ encodes character class to json object"""
        return {
            "name": self.name,
            "location": self.location.encode(),
            "health": self.health,
            "status": self.status,
            "inventory": self.inventory.encode(),
            "weapon": self.weapon,
            "armour": self.armour
        }


    @classmethod
    def decode(cls, data=None):
        """ decodes character json object to character class"""
        if data is None:
            data = {}
        from areas import Door
        instance = User(data["name"], Door.decode(data["location"]) )
        instance.health = data["health"]
        from inventory import Inventory
        instance.inventory = Inventory.decode(data["inventory"])
        instance.armour = data["armour"]
        instance.weapon = data["weapon"]
        instance.status = True

        return instance



class Enemy(Character):
    def __init__(self, name, rank, health, damage):
        self.name = name
        self.rank = rank
        self.__health = health
        self.__damage = damage
        self.armour = 'body'
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
        self.dialog = dialog
        self._interacted = False


    def interact(self):
        if not self._interacted:
            self.introduction()
            timed_print(f"{self.dialog}")
            self._interacted = True
        else:
            self.introduction()
            timed_print(f"{self.name} has already been interacted with. {self.role}")


    def introduction(self):
        timed_print(f"Hello I am {self.name}, {self.role}")



