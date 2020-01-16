# Updated #1 about basic information (characters...) in the mian_game.py
# Edited person: Qian Xiang
# Last updated date: 10/25/2019


# imnport
import random
import sys
import character
import map
from tabulate import tabulate
import weapon
# create a nested dictionary (a dictionary in a dictionary) for the characters
# number of character is use to count the # of character we have and help us
# to create other code easier
# https://www.daniweb.com/programming/software-development/
# threads/334354/rpg-class-attributes-stats
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
              'ability': 'Hoarder - you will get one more weapon after you'
              ' kill a boss',
              'health': '1200',
              'damage': '250',
              },
              'Soldier': {
              'number': '#3',
              'firstName': 'Naib',
              'lastName': 'Collins',
              'ability': 'Skilled - before you enter a new rooom,'
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


def play():
    """Print an action menu and allow for continous game play"""
    # print title of game
    # intro_text()
    # valid directions and actions for the characters
    action = ["quit", "characters"]
    directions = ["north", "south", "east", "west"]
    # print a list a valid actions before user input. Organized according to
    # possible direction and actions
    print("\n")
    print_actions(action)
    while True:
        # after user input, print out the action choosen by the user
        action_input = get_player_command("Action: ")
        if action_input in action:
            print(f"{action_input.title()}!")
            if action_input == "quit":
                sys.exit()
            # after the character is choosen, player chooses the map to play
            elif action_input == "characters":
                choose_people()
                choose_map()
                add_action(action)
            elif action_input == "move":
                # directions menu and options appear when move is choosen
                for d in directions:
                    print(d)
                user_direction = get_player_command("What direction?")
                if user_direction in directions:
                    print(f"Moving {user_direction}")
                    print("\n")
                else:
                    print("Invalid direction")
                    print("\n")
        else:
            print("Invalid action!")
            print("\n")


def get_player_command(message):
    """Get user input and convert the string to lowercase"""
    action_input = input(message)
    return action_input.lower()


def choose_people():
    """User chooses which hero they wish to play as"""
    print("Possible Characters:")
    people = character.characters
    for characters in people:
        print(characters)
    while True:
        input = get_player_command("What character would you like to play?")
        player = input.title()
        # prevent input error if the user does not input The Thief
        if player == "Thief":
            player = "Thief"
        # print the choosen character with characteristics and weapon
        if player in character.characters:
            print(f"Welcome, {player}!")
            character.character_check(player)
            weapon.level_weapon("Common Weapon", weapon.weapon)
            print("\n")
            break
        else:
            print("Invalid Character")
            print("\n")


def choose_map():



def add_action(list):
    """Unlock actions after characters and map is chosen"""
    unlock_action = ['attack', 'dodge', 'defense', 'run back(quit)',
                     'use your ability']
    list.remove("map")
    list.remove("characters")
    print_actions(list)
    print("\n")


def print_actions(action):
    print(f"Complete one of the following actions:")
    for user_action in action:
        print(f"* {user_action}")
    print("\n")


play()
