#All abstract classes will be defined in this file and other files will import for usage
from abc import ABC, abstractmethod


class Character(ABC):
    def __init__(self):
        self.interacted = False

    @abstractmethod
    def introduction(self):
        pass


class Location(ABC):
    # abstract class for each section in the maze/tunnel


    @property
    @abstractmethod
    def left(self):
        """property that gets the left location"""
        pass

    @property
    @abstractmethod
    def right(self):
        """property that gets the right location"""
        pass

    @left.setter
    @abstractmethod
    def left(self, area=None):
        """setter that sets left area"""
        pass

    @right.setter
    @abstractmethod
    def right(self, area=None):
        """setter that sets right area"""
        pass

    @abstractmethod
    def mini_game(self):
        """plays mini_game and returns a bool"""
        pass

