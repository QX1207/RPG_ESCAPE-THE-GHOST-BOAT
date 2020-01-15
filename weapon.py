# just import random to give a random weapon at the beginning of the game
import random
# a dictionary of weapon in the game
weapon = {"Common Weapon":{'Wood Sword':
                            {}
                            },
                'Stone Sword',
                'Bone Knife',
                'Stone Knife',
                'Wood Knife',
                'Stone Hatchet',
                'Wood Dragger',
                'Stone Dragger'
                'Broken Bow and Arrow - Dragon and Triger',
                'Wood Bow and Arrow'},
            {"Rare Weapon": {"Ice Wand - Frozen Ghost",
                "Wind Sword - Death Zone",
                "Fire Dagger - Fire Punishment",
                "Dark Dragger - Infinite",
                "Mechanical Umbrella - Thousands of Organ"},
            {"epicWeapon":{"Star Wand - Final Justice",
                "Death Stone - Dark Hallow",
                "Unknown Sword - Broken Sword from the Stone"},
            {"Legendar yWeapon": {"Chaos Mirror"}


def player_weapon(player, weapon):
    """Print out the inventory for the choosen character"""
    for item in weapon[player]:
        description = inventory[player][item]["description"]
        damage = inventory[player][item]["damage"]
        protection = inventory[player][item]["protection"]
        print(f"{player}'s {item} - {description}")
        print(f"damage: {damage}")
        print(f"protection: {protection}")
