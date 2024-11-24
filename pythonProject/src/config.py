damage_map = {}
enemies = ['skeleton', 'mummy']
for enemy in enemies:
    damage_map[enemy] = {} # how this would be hard coded, damage_map = {'skeleton': {}}

damage_map['skeleton']['torch'] = 1
damage_map['skeleton']['mace'] = 3
damage_map['mummy']['torch'] = 3
damage_map['mummy']['mace'] = 1



