# Updated #3 about Modules and Map in the mian_game.py
# Edited person: Qian Xiang
# Last updated date: 11/15/2019


import random
from tabulate import tabulate


# create a dictionary abou my rooms
rooms = {
    'room #1': {'l1': 'Wheelhouse', 'l2': 'Level C Boss'},
    'room #2': {'l1': 'Accommodators', 'l2': 'Level C Boss'},
    'room #3': {'l1': 'Mess Area', 'l2': 'Level B Boss'},
    'room #4': {'l1': 'Preparation room', 'l2': 'Level A Boss'},
    'room #5': {'l1': 'Preparation room', 'l2': 'Level A Boss'},
    'room #6': {'l1': 'Preparation room', 'l2': 'Level A Boss'},
    'room #7': {'l1': 'Preparation room', 'l2': 'Level A Boss'},
    'room #8': {'l1': 'Preparation room', 'l2': 'Level A Boss'},
    'room #9': {'l1': 'Preparation room', 'l2': 'Level A Boss'},
    'room #10': {'l1': 'Preparation room', 'l2': 'Level A Boss'},
    'room #11': {'l1': 'Preparation room', 'l2': 'Level A Boss'},
    'room #12': {'l1': 'Preparation room', 'l2': 'Level A Boss'},
    'room #13': {'l1': 'Preparation room', 'l2': 'Level A Boss'},
    'room #14': {'l1': 'Preparation room', 'l2': 'Level A Boss'},
    'room #15': {'l1': 'Preparation room', 'l2': 'Level A Boss'},
    'room #16': {'l1': 'Preparation room', 'l2': 'Level A Boss'},
}


def print_map():
        """Print a map of the ship with directions"""
        ship_printable = """
                            North
                |          |        |            |
                |          |        |            |  
                |          |        |            |
                |          |        |            |
                        South
        """
        print(ship_printable)
