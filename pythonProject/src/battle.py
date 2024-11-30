from game_effects import timed_print
import config
from sound import PlaySound


class Battle:
    def __init__(self, player, enemy):
        #Initiliase battle with player and enemy
        self.player = player
        self.enemy = enemy


    def player_turn(self): #Handles the player's turn in battle
        timed_print(f"{self.player.name}'s turn!")
        timed_print("\n")
        choice = input("Do you want to attack (a) or use item (i)? ").lower() #Prompt user to pick between attacking or using an item

        if choice == 'a':
            if self.attack(self.player, self.enemy): #Attacks enemy
                return True #Returns true to continue onto enemies turn
        elif choice == 'i': #Allows user to pick an item from inventory
             if self.equip_item(): #Equips item
                 return self.player_turn() #Returns to player's turn
        else:
            timed_print("Invalid choice. You can only attack or use an item.") #Invalid choice prompts user to try again
            return self.player_turn()  #Prompt user with another turn

    def enemy_turn(self): #Enemy's turn
        timed_print(f"{self.enemy.name}'s turn!")
        return self.attack(self.enemy, self.player) #Enemy attacks player

    def attack(self, attacker, defender):
        """
        Executes an attack from player to enemy
        -Calculates damage based on attacker's class (Player or Enemy)
        - Applies damage to enemy
        - Checks if defender (enemy) is defeated
        """
        #get basic damage from the attacker

        if attacker.__class__.__name__ == 'User': #Checks if attacker is a player
            damage = config.damage_map[defender.name][attacker.weapon] #Gets weapon specific damage from damage map in config
            PlaySound.playPunchSound() # Playing the sound of the player attacking
        else:
            damage = attacker.damage #Use the enemy's default damage value

        defender.take_damage(damage) #Enemy takes damage
        timed_print(f"{attacker.name} attacks {defender.name} for {damage} damage!")

        if defender.health <= 0: #Checks if enemy is dead
            return True  #If dead, end the battle
        else:
            timed_print(f"{defender.name} has {int(defender.health)} health remaining.") #Prints enemies remaining health
        return False  #continue the battle

    def equip_item(self):
        """
        Allows the player to equip an item from their inventory
        -Displays all equippable items
        -Lets the player choose an item by its index
        -Equips the chosen item and ends the turn if successful
        """
        equippable_items = self.player.inventory.get_equippable_items() #Retrieve equippable items
        if not equippable_items: #If the inventory is empty
            timed_print("You have no items in your inventory!")
            return False  # Player turn ends without an action

        timed_print("Available items:")
        for i, item in enumerate(equippable_items):
            timed_print(f"{i + 1}. {item}", delay=0.045) #Shows players inventory

        while True: #Keep prompting player until a valid choice is made
            try:
                choice = int(input("Enter the number of the item you want to equip: "))
                if 1 <= choice <= len(equippable_items): #Checks for valid input range
                    self.player.equip(equippable_items[choice - 1]) #Equip selected item
                    timed_print(f"{self.player.name} equipped {equippable_items[choice - 1]}.")
                    return True  # Successfully equipped item
                else:
                    timed_print("Invalid input!") #Out of range input message
            except ValueError: #Error for non-numeric inputs
                timed_print("Wrong input, try again.")

    def start_battle(self):
        """
        The main loop for the battle
        -Switches between enemy and player turns
        -Ends when either the player or the enemy is dead
        """
        while True:
            #player turn and check if they won
            if self.player_turn():
                timed_print(f"{self.player.name} wins the battle!")
                PlaySound.playWinSound() # Playing the victory sound using the method in sound.py
                return True  #end battle with player win

            #enemy turn and check if they won
            if self.enemy_turn():
                timed_print(f"{self.enemy.name} wins the battle!")
                return False  #end battle with enemy win