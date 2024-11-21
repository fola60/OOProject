# This file will contain all characters from which other files can import
from abc import abstractproperty

from abstract_classes import Character
from game_effects import timed_print

class User(Character):
    def __init__(self):
        pass

class Enemy(Character):
    def __init__(self):
        pass

class NPC(Character):
    def __init__(self):
        pass
    # npc advises you on which path to take and what items to take, the npc can lie to you aswell



