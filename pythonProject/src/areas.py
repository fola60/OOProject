"""
A location class for the locations, it will have left and right

"""

from abstract_classes import Location
from mini_games import MiniGames
from characters import Enemy, NPC
from mini_games import MiniGames
from config import minigame_to_map, npc_to_map
from src.inventory import Chest


class Door(Location):
    def __init__(self, door_number, chest=None):
        super().__init__(door_number)
        self.end_of_game = False # Bool for if the current locaiton is the last stage
        self.chest = chest # Chest Class attribute
        self.door_number = door_number # door number of area
        self.enemy = None # enemy for the area, Enemy Class
        self.description_stage1 = "" # description of stage 1 area
        self.description_stage2 = "" # description of stage 2 area
        self.npc = None # npc for the area, set to NPC Class
        self._minigame = None # minigame for the area set to, lambda function

    @property
    def left(self):
        """
        returns the left path of the current area
        :return: Door Class
        """
        return self._left

    @left.setter
    def left(self, area):
        """
        sets the left path of the current area
        """
        if area is not None:
            if not isinstance(area, Location):
                raise ValueError("Left must be a Location")
            area._parent = self
        self._left = area

    @property
    def right(self):
        """
        returns the right path of the current area
        :return: Door Class
        """
        return self._right

    @right.setter
    def right(self, area):
        """
        sets right path of area
        :param area: Door class
        :return: Door Class
        """
        if area is not None:
            if not isinstance(area, Location):
                raise ValueError("Right must be a Location")
            area._parent = self
        self._right = area

    def play_minigame(self):
        """
        starts minigame function and returns result
        :return: bool.
        """
        if self._minigame is None:
            return True
        return self._minigame()

    def fight_guard(self, player, enemy):
        """

        :param player: User class
        :param enemy: Enemy class
        :return: bool
        """
        from battle import Battle # to avoid circular import
        guard_fight = Battle(player, enemy)
        return guard_fight.start_battle()

    def interact_with_npc(self):
        """
        runs through interact function of npc class
        :return: Null
        """
        self.npc.interact()

    def view_chest(self, chest):
        """
        prints to output contents of chest
        :param chest: Chest Class
        :return: None
        """
        chest.display_items() # call display_items method of chest class


    @classmethod
    def decode(cls, data):
        """
        decodes json object to class Door
        :param data: json object of class Door
        :return: Door class
        """

        instance = Door(data["door_number"]) # creating door class with key "door_number" from data object
        instance._left = cls.decode(data["left"]) if data["left"] else None # creating door class for left property with key "left" if its not None
        instance._right = cls.decode(data["right"]) if data["right"] else None # creating door class for left property with key "left" if its not None
        instance._minigame = minigame_to_map[data["door_number"]] # creating mini-game function with a dict with the key of the door number mapped to premade lambda function of the minigame
        instance.npc = npc_to_map[data["door_number"]] # creating npc class with a dict with the key of the door number mapped to premade npc class
        instance.enemy = Enemy.decode(data["enemy"]) # creating enemy class by decoding with the key of "enemy" which is a json object, then converts to Enemy class
        instance.chest = Chest.decode(data["chest"]) # creating chest class with encoded chest data, decoded with class method decode from class chest
        instance.end_of_game = data["end_of_game"]
        return instance

class PyramidGame:
    """
    This class builds the game map
    """
    def __init__(self):
        self.current_location = None
        self.build_pyramid()

    def build_pyramid(self):
        """
        Create all doors (0-6 as in your example)
        Can define map properties here
        """
        doors = [Door(i) for i in range(7)]

        # Build the pyramid structure
        # Level 0 (top)
        from inventory import Chest # done here to avoid circular imports
        skeleton = Enemy("skeleton", "guard", 50, 40)
        warriors = Enemy("ancient egyptian warriors", "Grunts", 75, 50)
        mummy_guardians = Enemy("mummy guardians", "Guards", 150, 60)
        pharaoh = Enemy("the last pharaoh", "Final Boss", 800, 80)

        blacksmith = NPC("Hewg",
                          "A skilled blacksmith who has been working for centuries, crafting and maintaining tools, weapons and armour."
                             "\nHis origin is unknown, all that's known is that he is bound to the tomb and cursed to forever work on his craft ",
                          "\"Feeling challenged against the first enemy, the chest in the far corner, it should have the perfect tool\"")

        priestess = NPC("Priestess",
                         "Role: A ghost or spirit who once tended to the tomb’s rituals and now offers cryptic advice."
                            "\nShe is bound to the tomb and may offer clues to solve puzzles.",
                         "\"The answers you may come to seek will have to do with a weapon.\"")  # jumbled word will be scepter

        prisoner = NPC("The Prisoner",
                        "A former archaeologist or explorer who got trapped inside the tomb long ago."
                            "\nHe may have valuable information but is wary of helping.",
                       "\"There’s a trap ahead, step on that plate and you’ll need quick hands to survive.\"")

        spirit = NPC("Wandering Spirit",
                      "A wandering spirit trying to reclaim it's lost body.",
                      "\"To overcome the last pharaoh, you must wield the scepter of ra. Only with the aegis of anubis can you withstand the devastating might of your enemy.\"")

        games = MiniGames()
        self.root = doors[0] # sets the root to the first door
        doors[0].npc = blacksmith # interaction for blacksmith npc
        doors[0]._minigame = lambda: games.memory_match("You see symbols fading on the wall.", "hieroglyphs") # setting minigame to lamdba function of minigame
        doors[0].enemy = skeleton # setting enemy for door 0 to skeleton
        doors[0].chest = Chest(['mace', 'torch', 'jar of holding', 'chainmail', 'leather guard', 'life water', 'elixir','blue lotus']) # defining chest class for door 0

        # Level 1
        self.root.left = doors[1] # setting the roots left path to door 1
        self.root.right = doors[2] # setting the roots right path to door 2
        doors[1].npc = priestess # interaction for priestess npc
        doors[1]._minigame = lambda: games.word_jumble("scepter", "This weapon was once wielded by the powerful Ra") # setting minigame to lamdba function of minigame
        doors[1].enemy = warriors  # setting enemy for door 1 to skeleton
        doors[1].chest = Chest(['jar of holding', 'bronze sentinal', 'obsidian dagger', 'obelisk hammer','sacred lotus petal','blue lotus']) # defining chest class for door 1

        # Level 2 (bottom)
        doors[1].left = doors[3] # setting door 1 left path to door 3
        doors[1].right = doors[4] # setting door 1 right path to door 4
        doors[2].left = doors[5] # setting door 2 left path to door 5
        doors[2].right = doors[6] # setting door 2 right path to door 6
        doors[2].npc = prisoner # interaction for prisoner npc
        doors[2]._minigame = lambda: games.quick_click("You have stepped on a pressure plate causing the room to enclose rapidly", 3) # setting minigame to lamdba function of minigame
        doors[2].chest = Chest(['papyrus satchel','golden pharos','scorpion tail bow', 'obelisk hammer', 'elixir', 'energy vial','charred apple']) # defining chest class for door 3
        doors[2].enemy = mummy_guardians # setting enemy for door 2 to mummy guardians


        # level 3
        for door in range(3, 7):
            doors[door].end_of_game = True # marking these areas as the end of the game
            doors[door].npc = spirit # interaction for spirit npc
            doors[door].enemy = pharaoh # setting end of game enemy to pharaoh

        doors[3].chest = Chest(['aegis of anubis', 'scepter of ra', 'bag of duat', 'elixir', 'cleansing sand' 'energy vial']) # defining chest class for door 3
        doors[3]._minigame = lambda: games.quick_click("You have stepped on a pressure plate causing the room to enclose rapidly", 3) # setting minigame to lamdba function of minigame

        doors[4].chest = Chest(['aegis of anubis', 'elixir','scepter of ra', 'charred apple', 'sacred lotus petal', 'papyrus satchel', 'cleansing sand']) # defining chest class for door 3
        doors[4]._minigame = lambda: games.memory_match("You fall and hit your head. Strange numbers appear in your head", "combination") # setting minigame to lamdba function of minigame

        doors[5].chest = Chest(['aegis of anubis', 'elixir','scepter of ra', 'bag of duat', 'ra sun balm', 'charred apple']) # defining chest class for door 3
        doors[5]._minigame = lambda: games.quick_click("You fell over a tripwire. Spikes begin moving in from the ceiling", 3) # setting minigame to lamdba function of minigame

        doors[6].chest = Chest(['aegis of anubis', 'elixir','scepter of ra', 'elixir','papyrus satchel', 'osiris blessing', 'energy vial']) # defining chest class for door 3
        doors[6]._minigame = lambda: games.word_jumble("energy", "A strange text appears in front of you, what could it mean?") # setting minigame to lamdba function of minigame



        # Start at bottom left
        self.current_location = doors[0]

