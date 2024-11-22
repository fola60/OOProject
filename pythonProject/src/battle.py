from abstract_classes import Character
from game_effects import timed_print
from inventory import Inventory
from characters import User, Skeleton
from game_effects import timed_print

class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def player_turn(self):
        timed_print(f"{self.player.name}'s turn!")
        choice = input("Do you want to attack (a) or use item (i)? ").lower()

        if choice == 'a':
            return self.attack(self.player, self.enemy)
        elif choice == 'i':
            timed_print("Using item is not implemented yet.")
            return False  # Continue the battle after item choice
        else:
            timed_print("Invalid choice. You can only attack or use an item.")
            return self.player_turn()  # Retry the player's turn

    def enemy_turn(self):
        timed_print(f"{self.enemy.name}'s turn!")
        return self.attack(self.enemy, self.player)

    def attack(self, attacker, defender):
        damage = attacker.damage  # Get the attacker's damage
        defender.take_damage(damage)  # Apply damage to the defender
        timed_print(f"{attacker.name} attacks {defender.name} for {damage} damage!")

        # Check if the defender is dead
        if defender.health <= 0:
            timed_print(f"{defender.name} has been defeated!")
            return True  # Battle is over, return True
        else:
            timed_print(f"{defender.name} has {defender.health} health remaining.")
        return False  # Continue the battle

    def start_battle(self):
        while True:
            # Player's turn
            if self.player_turn():
                timed_print(f"{self.player.name} wins the battle!")
                break  # End the battle

            # Enemy's turn
            if self.enemy_turn():
                timed_print(f"{self.enemy.name} wins the battle!")
                break  # End the battle


if __name__ == "__main__":
    player = User(name="Hero", location=None, damage=3)  # Instantiate the User
    enemy = Skeleton()  # Instantiate the Skeleton
    battle = Battle(player, enemy)  # Initialize the battle with the player and enemy
    battle.start_battle()  # Start the battle loop
