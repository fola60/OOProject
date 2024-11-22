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
    def __init__(self, User):
        self.__left = None
        self.__right = None

    @property
    @abstractmethod
    def left(self):
        """property that gets the left location"""
        return self.__left


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
    def mini_game(self, func):
        """plays mini_game and returns a bool"""
        pass

    def chest(self):
        """import from inventory """
        pass

    def interaction(self):
        """inport charcter from characters """
        pass








class Storage(ABC):

    @abstractmethod
    def items(self):
        pass

