# Updated #3 about Modules and Map in the mian_game.py
# Edited person: Qian Xiang
# Last updated date: 11/15/2019


import random
from tabulate import tabulate


currentLocations = {
    "room #1": "Officer's Quarters",
    "room #2": "Navgation",
    "room #3": "First Mate's Quarters",
    "room #4": "Captain's Quarters",
    "room #5": "Fore Castle Deck",
    "room #6": "Long Boat (Escape gate)",
    "room #7": "Main-Mast",
    "room #8": "Wheel",
    "room #9": "Fore Hold",
    "room #10": "Cargo Access",
    "room #11": "Capstan",
    "room #12": "Officer's Mess",
    "room #13": "Live stock Hold",
    "room #14": "Infirmary",
    "room #15": "Cable Stores",
    "room #16": "Carpenter Stores"
}


# create a nested list about my map
map = []

def print_map():
        """Print a map of the ghost ship with directions"""
        ship_printable = """
                            North
                |          |        |            |
                |          |        |            |
                |          |        |            |
                |          |        |            |
                            South
        """
        print(ship_printable)
