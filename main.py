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


def add_action(list):
    """Unlock actions after characters and map is chosen"""
    unlock_action = ['attack', 'dodge', 'defense', 'run back',
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

import display,fight
import map
import re
print("""魔王抓走了公主，玩家要进入魔塔打败魔王，救出公主。
        魔塔由很多房间组成，房间里有物品、怪物，还要公主和魔王。
        玩家要打败怪物升级，搜索房间获得物品，让自己属性变得更强，才能打败魔王。
        要用一个引擎让这个充满房间的魔塔运行。
        """)
#游戏引擎类
class Engine(object):
    def __init__(self,tower):
        self.tower = tower
    def play(self):
#游戏介绍
        print("""
        欧洲中世纪时期，一位叫玛丽的公主被恶魔掳走了。
        国王悲痛欲绝，许下诺言说谁要是能救回公主，就把国家的国土分他一半。
        可是并没有人敢答应，因为大家都知道恶魔十分恐怖，它所住的地方--魔塔，
        更是一个阴森恐怖，极度危险的地方，到过那的人没有一个能活着回来。
        这个时候，一个叫卡尔的年轻人主动上前，表示愿意试一试。
        国王说，年轻人那就拜托你了，魔塔离这里路途遥远，不过我可以用时光之杖直接送你过去。
        只见一道白光，你被传送到了魔塔。
        """)
        raw_input('>')
        print("""
        你来到了魔塔，这里阴森恐怖，有很多怪物在这出没，也有一些地方藏着很厉害的武器，
        你要试着去找到那些武器让自己变得更加强大，挑战不同的怪物让自己升级，才能让自己
        有足够能力打败魔王！
        在游戏中，Q键可以查看你和怪物的属性，战斗预测可以告诉你打败怪物会消耗的血量。
        E键可以查看小地图，了解你在地图中的位置。
        游戏开始了，加油！
        """)
        raw_input('>')
        now_room = None
        next_room = self.tower.first_room
        while True:
            room = self.tower.enter_room(next_room,now_room)
            now_room = next_room
            next_room = room
#角色类
class Role(object):
    pass
tower = Tower("room5")
game = Engine(tower)
game.play()
