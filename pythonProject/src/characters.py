# This file will contain all characters from which other files can import
import config
from abstract_classes import Character
from game_effects import timed_print
from inventory import Inventory



class User(Character):


    def __init__(self, name, location):
        self.__location = location # Current player location
        self.name = name  # Player name
        self.__health = 100  # Player health
        self.max_health_size = 100
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
        print(f"{self.name} enters the world at {self.__location}. Good luck!")


    def take_damage(self, damage):
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

        if item not in config.consumable_item_list:
            timed_print("Cannot consume that item.")
            return

        if item in config.health_item_list:
            self.health = self.health + config.health_gain[item]
            timed_print(f"Health increased by {config.health_gain[item]}")
            return

        if item in config.max_health_item_list:
            self.max_health_size = self.max_health_size + config.health_boost[item]
            timed_print(f"Max health increased by {config.health_boost[item]}")
            return

    def equip(self, item):
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
        self.__dialog = dialog
        self._interacted = False


    def interact(self):
        if not self._interacted:
            self.introduction()
            self._interacted = True
        else:
            timed_print("{self.name} has already been interacted with.")


    def introduction(self):
        timed_print(f"Hello my name is {self.name}")


skeleton = Enemy("Skeleton", "guard", 50, 10)
warriors = Enemy("Ancient Egyptian Warriors", "Grunts", 75, 20)
mummy_guardians = Enemy("Mummy Guardians", "Guards", 150, 30)
pharaoh = Enemy("The Last Pharaoh", "Final Boss",500, 40)

blacksmith = NPC("Hewg",
                 "A skilled blacksmith who has been working for centuries, crafting and maintaining tools, weapons and armour."
                                    "His origin is unknown, all thats known is that he is bound to the tomb and cursed to forever work on his craft ",
                "I forge, for it is my purpose. What can i offer thee")

priestess = NPC("Priestess",
                "Role: A ghost or spirit who once tended to the tomb’s rituals and now offers cryptic advice."
                                        "She is bound to the tomb and may offer clues to solve puzzles.",
                "I can off thee the answer to the riddles but at a cost")

prisoner = NPC("The Prisoner",
               "A former archaeologist or explorer who got trapped inside the tomb long ago."
                                        "He may have valuable information but is wary of helping.",
               "There’s a trap ahead, step on that plate and you’ll need quick hands to survive. ")

