from setuptools.command.editable_wheel import editable_wheel

from main_game import Game


if __name__ == "__main__":
    game = Game()
    game.run()
