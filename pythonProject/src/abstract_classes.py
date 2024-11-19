#All abstract classes will be defined in this file and other files will import for usage
from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self):
        self.interacted = False

    @abstractmethod
    def introduction(self):
        pass

class Game(ABC):
    # abstract class for mini-games

    @abstractmethod
    def run(self):
        pass

class Location(ABC):
    # abstract class for each section in the maze/tunnel
    def choose_room(self):
        pass

