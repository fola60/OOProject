#WEAPONS
from characters import NPC, Enemy

weapon_list = ['fist', 'mace', 'torch', 'scepter of ra', 'obsidian dagger', 'obelisk hammer', 'scorpion tail bow'] # list of equippable weapons

#INVENTORY
inventory_size_boost = {'jar of holding' : 4, 'papyrus satchel' : 5, 'bag of duat' : 6} # maps items that increase storage size to the amount they increase storage size
bag_list = ['jar of holding', 'papyrus satchel', 'bag of the duat'] # list of equipabble items that increases inventory size
bag_size_map = {'jar of holding': 4, 'papyrus satchel': 5, 'bag of duat': 6} # maps bags to increased size


#ARMOUR
armour_list = ['body','chainmail', 'leather guard','bronze sentinal','golden pharos', 'aegis of anubis'] # list of equippable armours
armour_negation_map = {'body': 1, 'leather guard': 1.2, 'chainmail': 1.4, 'bronze sentinal': 1.6, 'golden pharos': 1.8, 'aegis of anubis': 2} # maps armour to damage negation amount

#HEALING
consumable_item_list = [] # list of consumable items
max_health_item_list = ['life water', 'blue lotus', 'charred apple', 'energy vial', 'cleansing sand'] # list of items that increase max health
health_gain_list = ['elixir', 'sacred lotus petal', 'ra sun balm', 'osiris blessing'] # list of items that heal the player
health_boost = {'life water': 50, 'blue lotus': 60, 'charred apple': 70, 'energy vial': 80, 'cleansing sand': 100} # maps items that increase health to the amount they increase health
health_gain = {'elixir': 20, 'sacred lotus petal': 75, 'ra sun balm': 150, 'osiris blessing': 300} # maps items that heal the player
consumable_item_list.extend(max_health_item_list)
consumable_item_list.extend(health_gain_list)

item_list = [] # List containing all items
item_list.extend(weapon_list)
item_list.extend(bag_list)
item_list.extend(armour_list)
item_list.extend(consumable_item_list)


equippable_item_list = [] # List containing all equippable items
for item in bag_list:
    equippable_item_list.append(item)
for item in armour_list:
    equippable_item_list.append(item)
for item in weapon_list:
    equippable_item_list.append(item)



enemies = ['skeleton', 'ancient egyptian warriors', 'mummy guardians', 'the last pharaoh']

#DAMAGE MAP
damage_map = {} # maps weapons to the damage they do
for enemy in enemies:
    damage_map[enemy] = {} # how this would be hard coded, damage_map = {'skeleton': {}}

damage_map['skeleton']['fist'] = 10
damage_map['skeleton']['mace'] = 50
damage_map['skeleton']['torch'] = 10
damage_map['skeleton']['scorpion tail bow'] = 40
damage_map['skeleton']['obsidian dagger'] = 40
damage_map['skeleton']['obelisk hammer'] = 70
damage_map['skeleton']['scepter of ra'] = 100

damage_map['ancient egyptian warriors']['fist'] = 10
damage_map['ancient egyptian warriors']['mace'] = 20
damage_map['ancient egyptian warriors']['torch'] = 10
damage_map['ancient egyptian warriors']['scorpion tail bow'] = 40
damage_map['ancient egyptian warriors']['obsidian dagger'] = 25
damage_map['ancient egyptian warriors']['obelisk hammer'] = 30
damage_map['ancient egyptian warriors']['scepter of ra'] = 100

damage_map['mummy guardians']['fist'] = 10
damage_map['mummy guardians']['mace'] = 20
damage_map['mummy guardians']['torch'] = 100
damage_map['mummy guardians']['scorpion tail bow'] = 40
damage_map['mummy guardians']['obsidian dagger'] = 60
damage_map['mummy guardians']['obelisk hammer'] = 70
damage_map['mummy guardians']['scepter of ra'] = 100

damage_map['the last pharaoh']['fist'] = 10
damage_map['the last pharaoh']['mace'] = 20
damage_map['the last pharaoh']['torch'] = 10
damage_map['the last pharaoh']['scorpion tail bow'] = 40
damage_map['the last pharaoh']['obsidian dagger'] = 60
damage_map['the last pharaoh']['obelisk hammer'] = 70
damage_map['the last pharaoh']['scepter of ra'] = 150



