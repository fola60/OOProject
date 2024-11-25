from abstract_classes import Character
from game_effects import timed_print
from inventory import Inventory
from characters import User
from game_effects import timed_print
from characters import Enemy
import config

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
            return self.equip_item()
        else:
            timed_print("Invalid choice. You can only attack or use an item.")
            return self.player_turn()  #retry the player's turn

    def enemy_turn(self):
        timed_print(f"{self.enemy.name}'s turn!")
        return self.attack(self.enemy, self.player)

    def attack(self, attacker, defender):
        #get basic damage from the attacker
        damage = attacker.damage
        defender.take_damage(damage)
        timed_print(f"{attacker.name} attacks {defender.name} for {damage} damage!")

        if defender.health <= 0:
            timed_print(f"{defender.name} has been defeated!")
            return True  #end the battle
        else:
            timed_print(f"{defender.name} has {defender.health} health remaining.")
        return False  #continue the battle

    def equip_item(self):
        if not self.player.inventory.get_equippable_items():
            timed_print("You have no items in your inventory!")
            return False  #continue battle if no items

        timed_print("Available items:")
        for i, item in self.player.inventory.get_equippable_items():
            timed_print(f"{i + 1}. {item}")

        while True:
            timed_print("Enter the number of the item you want to equip")
            try:
                choice = int(input(": "))
                self.player.equip(self.player.inventory.get_equippable_items()[choice - 1])
                
                break
            except ValueError:
                timed_print("Wrong input try again.")

        # equip armour or weapon


        self.attack(self.player, self.enemy)

    def start_battle(self):
        while True:
            #player turn and check if they won
            if self.player_turn():
                timed_print(f"{self.player.name} wins the battle!")
                break  #end battle

            #enemy turn and check if they won
            if self.enemy_turn():
                timed_print(f"{self.enemy.name} wins the battle!")
                break  #end battle





if __name__ == "__main__":
    player = User(name="Hero", location=None)  # Instantiate the User
    enemy = Enemy(name='skeleton', rank='Guard', health=3, damage=1)  # Instantiate the Skeleton
    battle = Battle(player, enemy)# Initialize the battle with the player and enemy
    player.inventory.items = 'torch' #add items to inventory for testing
    player.inventory.items = 'mace'
    battle.start_battle()  # Start the battle loop
