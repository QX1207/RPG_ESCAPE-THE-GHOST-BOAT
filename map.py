# Updated #3 about Modules and Map in the mian_game.py
# Edited person: Qian Xiang
# Last updated date: 11/15/2019


import random
import sys

# create a list about area in my game
rooms = [["Officer's Quarters", "Navgation", "First Mate's Quarters",
          "Captain's Quarters"],
         ["Fore Castle Deck", "Long Boat (Escape gate)",
          "Main-Mast", "Wheel"],
         ["Fore Hold", "Cargo Access", "Capstan", "Officer's Mess"],
         ["Live stock Hold", "Infirmary", "Cable Stores", "Carpenter Stores"]]


# definite the main_map in my game
def main_map():
    """print out the map about the boat generated"""
    for room in rooms:
        print(room)


class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 10


class MapCoordinates():
    """ Map with x and y coordinates"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_alive(self):
        """player is alive if they have at least 1 HP"""
        return self.hp > 0

    def __str__(self):
        return self.inventory

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        """Added modify_player to every tile"""
        pass


class StartTile(MapCoordinates):
    """Player starting position"""

    def intro_text(self):
        """Descriptive text for the Start Tile"""
        return """

        """


class ViewMapTile(MapTile):
    """Position that prints a map"""
    def intro_text(self):
        """Descriptive text for the Viewable Map Tile"""
        return """
        You see a map on the wall.
        """

    def print_map():
        """Print a map of the ghost ship with directions"""
        print_map = """
                                North
    |Officer's Quarters|Navgation   |First Mate's Quarters|Captain's Quarters|
    | Fore Castle Deck |Long Boat   |      Main-Mast      |       Wheel      |
    | Fore Hold        |Cargo Access|     Capstan         |  Officer's Mess  |
    | Live stock Hold  |Infirmary   |     Cable Stores    | Carpenter Stores |
                                South
    """
    print(print_map)


class ForeHold(MapCoordinates):
    """Position that contains the Fore Hold"""
    def modify_player(self, player):
        """Player wins the game if they reach the Fore Hold"""
        player.victory = True
        sys.exit()

    def intro_text(self):
        return """
        You found the Fore Hold! You can leave the ghost ship SV Mary Celeste.
        """


class Monster(object):
    """Monster"""
    def __init__(self,name,level):
        self.name = name
        self.level = level

# Monsters
Monster_a = Monster("a","1")
Monster_b = Monster("b","2")
Monster_c = Monster("c","3")
Monster_d = Monster("d","4")
Monster_e = Monster("e","5")
def make_monster():
        # 2 = monster in room; else, no monster
        monster_in = random.randrange(3)
        if monster_in == (0 or 1):
                return 0
        monster = random.randrange(5)
        if monster == 0:
                monster = a
        elif monster == 1:
                monster = b
        elif monster == 2:
                monster = c
        elif monster == 3:
                monster = d
        elif monster == 4:
                monster = e
        return monster
