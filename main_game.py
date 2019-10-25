# Basic information about updated #1 in the mian_game.py
# Edited person: Qian Xiang
# Last updated date: 10/25/2019


# create a nested dictionary (a dictionary in a dictionary) for the characters
characters = {
    'Doctor': {
        'number': '#1',
        'firstName': 'Jame',
        'lastName': 'Dyer',
        'ability': 'Med Master - you can choose to heal 50 HP when you are'
        ' fighting with boss',
        'health': '1500',
        'damage': '170',
    },
    'Thief': {
        'number': '#2',
        'firstName': 'Darius',
        'lastName': 'Pierson',
        'ability': 'Hoarder - you will get one more weapon after you'
        ' kill a boss',
        'health': '1200',
        'damage': '250',
    },
    'Soldier': {
        'number': '#3',
        'firstName': 'Naib',
        'lastName': 'Collins',
        'ability': 'Skilled - before you enter a new rooom, you can change a'
        ' random weapon',
        'health': '2000',
        'damage': '200',
    },

}


# use for-loop to print out my statement about characters line by line
for characters, characters_info in characters.items():
    number = characters_info["number"]
    print(f"\nCharacters {number}: {characters}")
    full_name = f"{characters_info['firstName']} {characters_info['lastName']}"
    ability = characters_info['ability']
    health = characters_info["health"]
    damage = characters_info["damage"]
    print(f"\tFull name: {full_name.title()}")
    print(f"\tAblility: {ability}")
    print(f"\t{characters} has {health} health point")
    print(f"\tBasic Attack Damage: {damage}")


# print two empty line that make it easy to read
print("\n")


# create a nested dictionary (a dictionary in a dictionary) for the inventories
weaponInventory = {
    'Wood Sword': {
                  'bonusAttackDamage': '25',
                  'description': 'A common sword made by wood',
                  'attackRanges': '5m',
                  'attackSpeed': '15%'
    },
    'Stone Sword': {
                   'bonusAttackDamage': '40',
                   'description': 'A common sword made by stone',
                   'attackRanges': '5m',
                   'attackSpeed': '10%'
    },
    'Stone Knife': {
                   'bonusAttackDamage': '30',
                   'description': 'A common knife made by stone',
                   'attackRanges': '60',
                   'attackSpeed': '10%'
    }
}


# print out the name of this inventory
print(f"\nInventory(common weapon):")


# use for-loop to print out my statement about inventories line by line
for weaponInventory, weaponInventory_info in weaponInventory.items():
    print(f"\n*{weaponInventory}")
    bonusAttackDamage = weaponInventory_info['bonusAttackDamage']
    description = weaponInventory_info["description"]
    attackRanges = weaponInventory_info["attackRanges"]
    attackSpeed = weaponInventory_info["attackSpeed"]
    print(f"\tBonus Attack Damage: {bonusAttackDamage}")
    print(f"\tDescription: {description}")
    print(f"\tAttack Range: {attackRanges}")
    print(f"\tAttack Speed: {attackSpeed}")


# print two empty line that make it easy to read
print("\n")


# create a nested dictionary (a dictionary in a dictionary) for the locations
currentLocations = {
    'room #1': {'l1': 'Wheelhouse', 'l2': 'Level C Boss'},
    'room #2': {'l1': 'Accommodators', 'l2': 'Level C Boss'},
    'room #3': {'l1': 'Mess Area', 'l2': 'Level B Boss'},
    'room #4': {'l1': 'Preparation room', 'l2': 'Level A Boss'},
}


# use for-loop to print out my statement about locations line by line
for name, currentlocations_info in currentLocations.items():
    l1 = currentlocations_info["l1"]
    l2 = currentlocations_info["l2"]
    print(f"\n{name.title()} is {l1} on the ship. There is"
          f" a {l2} in this area")
