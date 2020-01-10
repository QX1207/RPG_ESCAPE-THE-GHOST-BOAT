# a list of common weapon in the game
commonWeapon = ['Wood Sword', 'Stone Sword', 'Bone Knife', 'Stone Knife',
                'Wood Knife', 'Stone Hatchet', 'Wood Dragger', 'Stone Dragger'
                'Broken Bow and Arrow - Dragon and Triger',
                'Wood Bow and Arrow']
# a list of rare weapon in the game
rareWeapon = ["Ice Wand - Frozen Ghost", "Wind Sword - Death Zone",
              "Fire Dagger - Fire Punishment", "Dark Dragger - Infinite",
              "Mechanical Umbrella - Thousands of Organ"]
# a list of epic weapon in the game
epicWeapon = ["Star Wand - Final Justice", "Death Stone - Dark Hallow",
              "Unknown Sword - Broken Sword from the Stone"]
# a list of legenary weapon in the game
legendaryWeapon = "Chaos Mirror"


class Weapon():
    """Weapon Class to raise errors and return the weapon's name"""
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects")

    def __str__(self):
        return "{} (+ {} Damage)".format(self.name, self.damage)


class Wood_Sword(Weapon):
    """Wood Sword weapon class with description and damage"""
    def __init__(self):
        self.name = "Wood Sword"
        self.description = """
                            A Wood Sword for damaging boss
                            """
        self.damage = 5
