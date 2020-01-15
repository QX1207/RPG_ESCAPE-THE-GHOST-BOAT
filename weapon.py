# just import random to give a random weapon at the beginning of the game
import random
# a dictionary of weapon in the game
weapon = {"Common Weapon": {'Wood Sword':
                           {'description': "",
                            'damage': 10,
                            'protection':0 },
                           'Stone Sword':
                           {'description': "",
                            'damage': 0,
                            'protection': 0},
                           'Bone Knife':
                           {'description': "",
                            'damage': 0,
                            'protection': 0},
                           'Stone Knife':
                           {'description': "",
                            'damage': 0,
                            'protection': 0},
                           'Wood Knife':
                           {'description': "",
                            'damage': 0,
                            'protection': 0},
                           'Stone Hatchet':
                           {'description': "",
                            'damage': 0,
                            'protection': 0},
                           'Wood Dragger':
                           {'description': "",
                            'damage': 0,
                            'protection': 0},
                           'Stone Dragger':
                           {'description': "",
                            'damage': 0,
                            'protection': 0},
                           'Broken Bow and Arrow - Dragon and Triger':
                           {'description': "",
                            'damage': 0,
                            'protection': 0},
                           'Wood Bow and Arrow':
                           {'description': "",
                            'damage': 0,
                            'protection': 0}},
        "Rare Weapon": {"Ice Wand - Frozen Ghost":
                        {'description': "",
                         'damage': 0,
                         'protection': 0},
                        "Wind Sword - Death Zone":
                        {'description': "",
                         'damage': 0,
                         'protection': 0},
                        "Fire Dagger - Fire Punishment":
                        {'description': "",
                         'damage': 0,
                         'protection': 0},
                        "Dark Dragger - Infinite":
                        {'description': "",
                         'damage': 0,
                         'protection': 0},
                        "Mechanical Umbrella - Thousands of Organ":
                        {'description': "",
                         'damage': 0,
                         'protection': 0},
                        },
        "epicWeapon": {"Star Wand - Final Justice":
                       {'description': "",
                        'damage': 0,
                        'protection': 0},
                       "Death Stone - Dark Hallow":
                       {'description': "",
                        'damage': 0,
                        'protection': 0},
                       "Unknown Sword - Broken Sword from the Stone":
                       {'description': "",
                        'damage': 0,
                        'protection': 0},
        "Legendar yWeapon": {"Chaos Mirror":
                             {'description': "",
                              'damage': 0,
                              'protection': 0}
        }


def player_weapon(player, weapon):
    """Print out the inventory for the choosen character"""
    for item in weapon[player]:
        description = inventory[player][item]["description"]
        damage = inventory[player][item]["damage"]
        protection = inventory[player][item]["protection"]
        print(f"{player}'s {item} - {description}")
        print(f"damage: {damage}")
        print(f"protection: {protection}")
