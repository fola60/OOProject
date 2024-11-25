#WEAPONS
weapon_list = ['fist', 'mace', 'torch', 'scepter of ra', 'obsidian dagger', 'obelisk hammer', 'scorpion tail bow'] # list of equippable weapons

#INVENTORY
inventory_size_boost = {'jar of holding' : 4, 'papyrus satchel' : 5, 'bag of duat' : 6} # maps items that increase storage size to the amount they increase storage size
bag_list = ['jar of holding', 'papyrusSatchel', 'bagOfTheDuat'] # list of equipabble items that increases inventory size

#ARMOUR
armour_list = ['body','chainmail', 'leather guard','bronze sentinal','golden pharos', 'aegis of anubis'] # list of equippable armours
armour_negation_map = {'body': 1, 'leather guard': 1.2, 'chainmail': 1.4, 'bronze sentinal': 1.6, 'golden pharos': 1.8, 'cleansing sand': 2} # maps armour to damage negation amount

#HEALING
health_item_list = ['elixir'] # list of items that heal
max_health_item_list = ['life water', 'blue lotus', 'charred apple', 'energy vial', 'cleansing sand'] # list of items that increase max health
health_boost = {'life water': 50, 'blue lotus': 60, 'charred apple': 70, 'energy vial': 80, 'cleansing sand': 100} # maps items that increase health to the amount they increase health
health_gain = {'elixir': 20} #maps items that heal the player

item_list = [] # List containing all items
item_list.extend(weapon_list)
item_list.extend(bag_list)
item_list.extend(health_item_list)
item_list.extend(armour_list)
item_list.extend(max_health_item_list)

equippable_item_list = [] # List containing all equippable items
for item in bag_list:
    equippable_item_list.append(item)
for item in armour_list:
    equippable_item_list.append(item)
for item in weapon_list:
    equippable_item_list.append(item)


consumable_item_list = ['elixir', 'life water', 'blue lotus', 'charred apple', 'energy vial', 'cleansing sand'] # list of consumable items

enemies = ['skeleton', 'warriors', 'mummy', 'pharaoh']

#DAMAGE MAP
damage_map = {} # maps weapons to the damage they do
for enemy in enemies:
    damage_map[enemy] = {} # how this would be hard coded, damage_map = {'skeleton': {}}

damage_map['skeleton']['fist'] = 10
damage_map['skeleton']['mace'] = 30
damage_map['skeleton']['torch'] = 10
damage_map['skeleton']['scorpion tail bow'] = 40
damage_map['skeleton']['obsidian dagger'] = 40
damage_map['skeleton']['obelisk hammer'] = 70
damage_map['skeleton']['scepter of ra'] = 100

damage_map['warriors']['fist'] = 10
damage_map['warriors']['mace'] = 20
damage_map['warriors']['torch'] = 10
damage_map['warriors']['scorpion tail bow'] = 60
damage_map['warriors']['obsidian dagger'] = 60
damage_map['warriors']['obelisk hammer'] = 70
damage_map['warriors']['scepter of ra'] = 100

damage_map['mummy']['fist'] = 10
damage_map['mummy']['mace'] = 20
damage_map['mummy']['torch'] = 50
damage_map['mummy']['scorpion tail bow'] = 40
damage_map['mummy']['obsidian dagger'] = 60
damage_map['mummy']['obelisk hammer'] = 70
damage_map['mummy']['scepter of ra'] = 100

damage_map['pharaoh']['fist'] = 10
damage_map['pharaoh']['mace'] = 20
damage_map['pharaoh']['torch'] = 10
damage_map['pharaoh']['scorpion tail bow'] = 40
damage_map['pharaoh']['obsidian dagger'] = 60
damage_map['pharaoh']['obelisk hammer'] = 70
damage_map['pharaoh']['scepter of ra'] = 100



