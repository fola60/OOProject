from abstract_classes import Character
from game_effects import timed_print
from inventory import Inventory
from characters import User, Skeleton
from game_effects import timed_print


class Battle:
    def __init__(self, player, enemy, damage_map):
        self.player = player
        self.enemy = enemy
        self.damage_map = damage_map  #map of weapon damage against enemies

    def player_turn(self):
        print(f"{self.player.name}'s turn!")
        choice = input("Do you want to attack (a) or use item (i)? ").lower()

        if choice == 'a':
            return self.attack(self.player, self.enemy)
        elif choice == 'i':
            return self.use_item()
        else:
            print("Invalid choice. You can only attack or use an item.")
            return self.player_turn()  #retry the player's turn

    def enemy_turn(self):
        print(f"{self.enemy.name}'s turn!")
        return self.attack(self.enemy, self.player)

    def attack(self, attacker, defender):
        #get basic damage from the attacker
        damage = attacker.damage
        defender.take_damage(damage)
        print(f"{attacker.name} attacks {defender.name} for {damage} damage!")

        if defender.health <= 0:
            print(f"{defender.name} has been defeated!")
            return True  #end the battle
        else:
            print(f"{defender.name} has {defender.health} health remaining.")
        return False  #continue the battle

    def use_item(self):
        if not self.player.inventory.items:
            print("You have no items in your inventory!")
            return False  #continue battle if no items

        print("Available items:")
        self.player.inventory.display_items()

        try:
            item_choice = int(input("Choose an item by number: ")) - 1  #adjust for 0 indexing
            if 0 <= item_choice < len(self.player.inventory.items):
                item = self.player.inventory.items[item_choice]  #get selected item
                #looks up the damage for the selected item from the damage_map
                damage = self.damage_map.get(self.enemy.name.lower(), {}).get(item, 0)

                if damage > 0:
                    print(f"You used {item} against {self.enemy.name}, dealing {damage} damage!")
                    self.enemy.take_damage(damage)
                    #remove the item from the player's inventory after use
                    self.player.inventory.use_item(item_choice)

                    #check if the enemy is defeated
                    if self.enemy.health <= 0:
                        print(f"{self.enemy.name} has been defeated!")
                        return True  #end battle
                    else:
                        print(f"{self.enemy.name} has {self.enemy.health} health remaining.")
                else:
                    print(f"{item} is ineffective against {self.enemy.name}!")
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except IndexError:
            print("Invalid item choice.")

        return False  #continue battle if no valid item used

    def start_battle(self):
        while True:
            #player turn and check if they won
            if self.player_turn():
                print(f"{self.player.name} wins the battle!")
                break  #end battle

            #enemy turn and check if they won
            if self.enemy_turn():
                print(f"{self.enemy.name} wins the battle!")
                break  #end battle

damage_map = {}

#initialize skeleton's damage map
damage_map['skeleton'] = {}
damage_map['skeleton']['torch'] = 1
damage_map['skeleton']['mace'] = 3

#initialize mummy's damage map
damage_map['mummy'] = {}
damage_map['mummy']['torch'] = 3
damage_map['mummy']['mace'] = 1


if __name__ == "__main__":
    player = User(name="Hero", location=None, damage=3)  # Instantiate the User
    enemy = Skeleton()  # Instantiate the Skeleton
    battle = Battle(player, enemy, damage_map)# Initialize the battle with the player and enemy
    player.inventory.items = 'torch' #add items to inventory for testing
    player.inventory.items = 'mace'
    battle.start_battle()  # Start the battle loop
