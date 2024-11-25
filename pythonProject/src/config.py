item_list = ['fist', 'body', 'JarOfHolding', 'PapyrusSatchel', 'BagOfTheDuat', 'PharaohBandolier', 'elixir', 'LifeWater', 'BlueLotus', 'charredApple', 'EnergyVial', 'CleansingSand']
equippable_item_list = ['JarOfHolding', 'PapyrusSatchel', 'BagOfTheDuat', 'PharaohBandolier'] # list of equipabble items
consumable_item_list = ['elixir', 'LifeWater', 'BlueLotus', 'charredApple', 'EnergyVial', 'CleansingSand'] # list of consumable items
armour_negation_map = {'body': 1} # maps armour to damage negation amount
health_boost = {} # maps items that increase health to the amount they increase health
inventory_size_boost = {} # maps items that increase storage size to the amount they increase storage size
damage_map = {} # maps weapons to the damage they do
enemies = ['skeleton', 'mummy']
for enemy in enemies:
    damage_map[enemy] = {} # how this would be hard coded, damage_map = {'skeleton': {}}

damage_map['skeleton']['torch'] = 1
damage_map['skeleton']['mace'] = 3
damage_map['skeleton']['fist'] = 3
damage_map['mummy']['torch'] = 3
damage_map['mummy']['mace'] = 1
damage_map['mummy']['fist'] = 3



