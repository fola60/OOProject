# This file will contain all characters from which other files can import
from abstract_classes import Character
from game_effects import timed_print
from src.abstract_classes import Location


#User (player's character)
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
        self.__weapon = None #Equipped weapon (default: none)
        self.__armour = None #Equipped armour (default: none)

    @property
    def weapon(self):
        #Returns the equipped weapon or default 'fist' if none is equipped
        if self.__weapon is None:
            return 'fist'
        return self.__weapon

    @weapon.setter
    def weapon(self, value):
        self.__weapon = value #Sets the equipped weapon

    @property
    def armour(self):
        #Returns the equipped armour or default 'body' if none is equipped
        if self.__armour is None:
            return 'body'
        return self.__armour

    @armour.setter
    def armour(self, armour):
        self.__armour = armour #Sets the equipped weapon


    def introduction(self):
        #Introduces the player at the start of the game
        timed_print(f"{self.name} enters the world at door {self.__location.door_number}. Good luck!")


    def take_damage(self, damage):
        #Reduces health based on damage and armour negation
        import config # Done here due to circular imports
        self.__health -= damage / config.armour_negation_map[self.armour] # decrements health based on armour


    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, amount):
        #Adjusts health and updates player status if health drops below zero
        if amount <= 0:
            self.__health = 0
            self.status = False #Player is dead
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
        -if user consumers non-consumable items they lose health
        -increases health or max health based on item
        -non-consumable items cant be consumed
        """

        import config  # Done here due to circular imports
        if item not in config.consumable_item_list:
            timed_print("Cannot consume that item.")
            return

        if item in config.health_gain_list: #Health-restoring items
            self.health = self.health + config.health_gain[item]
            timed_print(f"Health increased by {config.health_gain[item]}")
            self.inventory.use_item(
                self.inventory.items.index(item)
            ) # gets the index of the item and applies the use_item function with that index
            return

        if item in config.max_health_item_list: #Max-health-boosting items
            self.max_health_size = self.max_health_size + config.health_boost[item]
            timed_print(f"Max health increased by {config.health_boost[item]}")
            self.inventory.use_item(
                self.inventory.items.index(item)
            )  # gets the index of the item and applies the use_item function with that index
            return

    def equip(self, item):
        """
        Equips a specified item
        -Adjusts player attributes based on the item type (weapon,armour, etc.)
        """
        import config  # Done here due to circular imports

        if item not in config.equippable_item_list:
            timed_print("Item not equippable")
            return

        if item in config.bag_list: #Items that increase inventory size
            self.inventory.max_inventory_size = config.inventory_size_boost[item]
            timed_print(f"Inventory size increased to {config.inventory_size_boost[item]}")
            return

        if item in config.weapon_list: #Weapons
            self.weapon = item
            timed_print(f"Equipped weapon: {item}")
            return

        if item in config.armour_list: #Armour
            self.armour = item
            timed_print(f"Equipped armour: {item}")
            return



    def check_status(self): # Checks current status of Player
         timed_print(f"Health: {self.__health},  Inventory: {self.inventory.display_items()}")

    def interact_with_chest(self):
        """
            Allows the player to interact with a chest at their location
            -Displays chest contents
            =Allows the player to choose which items to add to their inventory
        """
        self.location.chest.display_items()
        while True:
            try:
                if self.inventory.max_inventory_size - len(self.inventory.items):
                    choice = int(input("Choose ID of item you want to add to your inventory or choose -1 to exit"))
                    if choice == -1: #Exit selection
                        break
                    item = self.location.chest.pick_items(choice - 1) #Pick item from chest
                    self.inventory.items = item #Add item to inventory
                    timed_print(f"You have added {item} to your inventory {self.inventory.max_inventory_size - len(self.inventory.items)} space remaining")
                    for i, item_name in enumerate(self.location.chest.items):
                        print(f"{i + 1} {item_name}")
                else:
                    timed_print("No more inventory space.")
                    break
            except ValueError:
                timed_print("Cannot choose that item.")


    def encode(self):
        """ encodes character class to json object"""
        return {
            "name": self.name,
            "location": self.location.encode() if self.__location else None,
            "health": self.health,
            "max_health": self.max_health_size,
            "status": self.status,
            "inventory": self.inventory.encode(),
            "weapon": self.weapon,
            "armour": self.armour,
        }


    @classmethod
    def decode(cls, data=None):
        """ decodes character json object to character class"""
        if data is None:
            data = {}
        from areas import Door
        instance = User(data["name"], Door.decode(data["location"] if data["location"] else Door(6)) )
        instance.health = data["health"]
        from inventory import Inventory
        instance.inventory = Inventory.decode(data["inventory"])
        instance.weapon = data["weapon"]
        instance.armour = data["armour"]
        instance.max_health_size = data["max_health"]
        instance.status = True

        return instance


#Enemy characters
class Enemy(Character):
    def __init__(self, name, rank, health, damage):
        self.name = name #Enemy name
        self.rank = rank #Enemy rank/type
        self.__health = health #Enemy health
        self.__damage = damage #Enemy damage
        self.armour = 'body' #Default armour
        self.status = True #Alive, false for dead

    def introduction(self):
        pass

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, amount):
        #Adjusts health and updates status if health drops to zero
        if amount <= 0:
            self.__health = 0
            self.status = False
        else:
            self.__health = amount

    @property
    def damage(self):
        return self.__damage

    def take_damage(self, damage):
        #Reduces health based on received damage
        self.__health -= damage


    def encode(self):
        """encodes the enemy's data"""
        return {
            "name": self.name,
            "health": self.health,
            "rank": self.rank,
            "damage": self.damage
        }

    @classmethod
    def decode(cls, data):
        """decodes enemy data"""
        instance = Enemy(data["name"], data["rank"], data["health"], data["damage"])
        return instance

#Non-playable characters
class NPC(Character):
    def __init__(self, name, role, dialog):
        self.name = name #NPC Name
        self.role = role #NPC Role
        self.dialog = dialog #NPC Dialog
        self._interacted = False #Tracks if NPC has been interacted with


    def interact(self):
        """
        Handles interactions with NPC's
        -displays dialog
        -lets player know if NPC has already been interacted with
        """
        if not self._interacted:
            self.introduction()
            timed_print(f"{self.dialog}")
            self._interacted = True
        else:
            self.introduction()
            timed_print(f"{self.name} has already been interacted with. {self.role}")


    def introduction(self):
        timed_print(f"Hello I am {self.name}, {self.role}")