# choice a character from 3 character
# character files:
# Character number 1
#   name: doctor Jame Dyer
#   ability: Med Master - you can choose to heal 50 HP
#            when you are fighting with boss


#   name: Thief - Darius Pierson
#   ability: Hoarder - you will get one more weapon after you kill a boss


#   name: Soldier - Naib Collins
#   ability: Skilled - before you enter a new rooom, you can change
#            a random weapon



characters = {
    'Doctor': {
        'firstName': 'Jame',
        'lastName': 'Dyer',
        'ability': 'Med Master - you can choose to heal 50 HP when you are'
        ' fighting with boss',
        'health': '1500',
        'damage': '170',
        },
    'Thief': {
        'firstName': 'Darius',
        'lastName': 'Pierson',
        'ability': 'Hoarder - you will get one more weapon after you'
        ' kill a boss',
        'health': '1200',
        'damage': '250',
        },
    'Soldier': {
        'firstName': 'Naib',
        'lastName': 'Collins',
        'ability': 'Skilled - before you enter a new rooom, you can change a'
        ' random weapon',
        'health': '2000',
        'damage': '200',
        },

    }


for characters, characters_info in characters.items():
    print(f"\nCharacters: {characters}")
    full_name = f"{characters_info['firstName']} {characters_info['lastName']}"
    ability = characters_info['ability']
    health = characters_info["health"]
    damage = characters_info["damage"]
    print(f"\tFull name: {full_name.title()}")
    print(f"\tAblility: {ability}")
    print(f"\t{characters} has {health} health point")
    print(f"\tBasic Attack Damage: {damage}")


# commonWeapon = ['Wood Sword', 'Stone Sword', 'Bone Knife', 'Stone Knife',
#                'Wood Knife', 'Stone Hatchet', 'Wood Dragger', 'Stone Dragger'
#                'Broken Bow and Arrow - Dragon and Triger',
#                'Wood Bow and Arrow']
# a list of rare weapon in the game
# rareWeapon = ["Ice Wand - Frozen Ghost", "Wind Sword - Death Zone",
#              "Fire Dagger - Fire Punishment", "Dark Dragger - Infinite",
#              "Mechanical Umbrella - Thousands of Organ"]
# a list of epic weapon in the game
# epicWeapon = ["Star Wand - Final Justice", "Death Stone - Dark Hallow",
#              "Unknown Sword - Broken Sword from the Stone"]
# a list of legenary weapon in the game
# legendaryWeapon = "Chaos Mirror"


weaponInventory = {'Wood Sword': {'bonus attack damage': '',
                   'description': ''},
                   'Stone Sword': {'bonus attack damage': '',
                   },
                   'Stone Knife': {'bonus attack damage': '',
                   },
                   'Wood Knife': {'bonus attack damage': '',
                   },
                   'Stone Sword': {'bonus attack damage': '',
                   },
                   'Stone Hatchet': {'bonus attack damage': '',
                   },
                   'Wood Dragger': {'bonus attack damage': '',
                   },
                   'Stone Dragger': {'bonus attack damage': ',
                   '},
                   'Broken Bow and Arrow - Dragon and Triger':
                   {'bonus attack damage': '',
                   },
                   'Wood Bow and Arrow': {'bonus attack damage': '',
                   }
                   }
