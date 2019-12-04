# Updated #1 about basic information (characters...) in the mian_game.py
# Edited person: Qian Xiang
# Last updated date: 10/25/2019


# imnport random
# this module used on line 203, 209, 214
import random

# create a nested dictionary (a dictionary in a dictionary) for the characters
# number of character is use to count the # of character we have and help us
# to create other code easier
# https://www.daniweb.com/programming/software-development/
# threads/334354/rpg-class-attributes-stats
class people:
    characters = {
                  'Doctor': {
                  'number': '#1',
                  'firstName': 'Jame',
                  'lastName': 'Dyer',
                  'ability': 'Med Master - you can choose '
                  'to heal 50 HP when you are fighting with boss',
                  'health': '1500',
                  'damage': '170',
                 },
                 'Thief': {
                 'number': '#2',
                 'firstName': 'Darius',
                 'lastName': 'Pierson',
                 'ability': 'Hoarder - you will get one more weapon after you',
                 ' kill a boss',
                 'health': '1200',
                 'damage': '250',
                 },
                 'Soldier': {
                 'number': '#3',
                 'firstName': 'Naib',
                 'lastName': 'Collins',
                 'ability': 'Skilled - before you enter a new rooom,',
                 ' you can change your to be a random weapon',
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


# print two empty line that make it easy to read
print("\n")


# print out a statement about the story
print("There are some monsters on the ship. Let us begin the adventure.")
# create a llist about the directions
playerDirections = ["North", "East", "South", "West(quit)"]


# Updated #2 about the definitions of function in the mian_game.py
# Edited person: Qian Xiang
# Last updated date: 11/7/2019


# create a definition of the function
# use for loop to print my selections
def directions(playerDirections):
    for playerDirection in playerDirections:
        print(
            f"{playerDirections.index(playerDirection) + 1}.{playerDirection}"
            )
# print out a statement that introduce the choices they face
    print("Go in one of the direction above (please enter the number):")
# after for loop, use while loop to repeat the question until it is break
while True:
    directions(playerDirections)
# create a user input
    selections = int(input("Enter choice: "))
# use if-elif-else statement to explain different movements
    if selections == 1:
        print("You are going forward to the next room.")
        print("\n")
    elif selections == 2:
        print("You are going to the right room.")
        print("\n")
    elif selections == 3:
        print("You are going backward.")
        print("\n")
    elif selections == 4:
        print("You are going to the left room. You find the monster!")
        print("\n")
        break
    else:
        print("Please enter the following number of directions to move")
        print("\n")


# 7 choice to decide your reaction, attack(make damage to the boss),
# dodge(dodge the boss's attack and make a few damage to the boss, maybe fail),
# defense(defense a part a damage from the boss), run back(),
# a choice to use your weapon, a choice to use your character ability
# (only doctor yet), and a choice to use your consumble


# print a multiple choise question about the action
print("Choose the following action to beat the boss",
      "(please enter the number): ")
# create a list about the character's actions when you meet a bosses
characterActions = ['attack', 'dodge', 'defense', 'run back(quit)',
                    'use your ability', 'use your weapon',
                    'use your consumble']


# create a definition of the function
# use for loop to print my selections
def behavior(characterActions):
    for characterAction in characterActions:
        print(
            f"{characterActions.index(characterAction) + 1}. {characterAction}"
            )
# after for loop, use while loop to repeat the question until it is break
while True:
    behavior(characterActions)
    # create a user input
    actions = int(input("You choose to "))
# use if-elif-else statement to explain different action from you character
    if actions == 1:
        attack = ("You make damage to the boss.", "Missing!!!")
        print(random.choice(attack))
        print("\n")
    elif actions == 2:
        dodge = ("You dodge the boss's attack and make a few damage to"
                 " the boss.",
                 "Boss's speed is very fast. You dodged that fail.")
        print(random.choice(dodge))
        print("\n")
    elif actions == 3:
        defense = ("You defense     a   part of damage.",
                   "You defense the attack fail.")
        print(random.choice(defense))
        print("\n")
    elif actions == 4:
        print("You run back to the last room.")
        print("\n")
        break
    elif actions == 5:
        print("Ablility list")
        print("\n")
    elif actions == 6:
        print("Weapon Inventory")
        print("\n")
    elif actions == 7:
        print("Consumble Inventory")
        print("\n")
    else:
        print("Please enter a number to finish your action")
        print("\n")
