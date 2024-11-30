from characters import User
from game_effects import timed_print
from characters import Enemy
import config
from sound import PlaySound


class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy


    def player_turn(self):
        timed_print(f"{self.player.name}'s turn!")
        timed_print("\n")
        choice = input("Do you want to attack (a) or use item (i)? ").lower()

        if choice == 'a':
            if self.attack(self.player, self.enemy):
                return True
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

        if attacker.__class__.__name__ == 'User':
            damage = config.damage_map[defender.name][attacker.weapon]
            PlaySound.playPunchSound() # Playing the sound of the player attacking
        else:
            damage = attacker.damage
        defender.take_damage(damage)
        timed_print(f"{attacker.name} attacks {defender.name} for {damage} damage!")

        if defender.health <= 0:
            return True  #end the battle
        else:
            timed_print(f"{defender.name} has {int(defender.health)} health remaining.")
        return False  #continue the battle

    def equip_item(self):
        if not self.player.inventory.get_equippable_items():
            timed_print("You have no items in your inventory!")
            return False  #continue battle if no items

        timed_print("Available items:")
        for i, item in enumerate(self.player.inventory.get_equippable_items()):
            timed_print(f"{i + 1}. {item}", delay=0.045)

        # equip armour or weapon
        while True:
            if len(self.player.inventory.get_equippable_items()) <= 0:
                timed_print("No equippable items.")
                self.player_turn()
                break
            timed_print("Enter the number of the item you want to equip")
            try:
                choice = int(input(": "))
                if 1 <= choice <= len(self.player.inventory.get_equippable_items()):
                    self.player.equip(self.player.inventory.get_equippable_items()[choice - 1])
                else:
                    timed_print("Invalid input!")
                    self.equip_item()
                break
            except ValueError:
                timed_print("Wrong input, try again.")


        self.player_turn()

    def start_battle(self):
        while True:
            #player turn and check if they won
            if self.player_turn():
                timed_print(f"{self.player.name} wins the battle!")
                PlaySound.playWinSound() # Playing the victory sound using the method in sound.py
                break  #end battle

            #enemy turn and check if they won
            if self.enemy_turn():
                timed_print(f"{self.enemy.name} wins the battle!")
                break  #end battle





#defeated enemy not working