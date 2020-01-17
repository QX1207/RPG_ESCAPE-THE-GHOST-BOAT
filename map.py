# Updated #3 about Modules and Map in the mian_game.py
# Edited person: Qian Xiang
# Last updated date: 11/15/2019


import random
import sys
import boss

# create a list about area in my game
rooms = [["Officer's Quarters", "Navgation", "First Mate's Quarters",
          "Captain's Quarters"],
         ["Escape Pod", "Long Boat",
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


class ViewMapTile(MapCoordinates):
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
    | Escape Boat      |Long Boat   |      Main-Mast      |       Wheel      |
    | Fore Hold        |Cargo Access|     Capstan         |  Officer's Mess  |
    | Live stock Hold  |Infirmary   |     Cable Stores    | Carpenter Stores |
                                South
    """
    print(print_map)


class EscapeBoat(MapCoordinates):
    """Position that contains the Escape Boat"""
    def modify_player(self, player):
        """Player wins the game if they reach the Escape Boat"""
        player.victory = True
        sys.exit()

    def intro_text(self):
        return """
        You found the Escape Boat! You can leave the ghost ship SV Mary
        Celeste.
        """


class Monster(object):
    """Monster"""
    def __init__(self,name,level):
        self.name = name
        self.level = level

# Monsters
Monster_Goblin = Monster("Goblin","0")
Monster_Tiger = Monster("Tiger","1")
Monster_Dragon = Monster("Dragon","2")
Monster_Dark_Turtle = Monster("Dark Turtle","3")
Monster_Phoenix = Monster("Phoenix","4")
Monster_Ripper = Monster("Ripper","5")
Monster_Ghoul = Monster("Ghoul","6")
Monster_Gold_Monkey = Monster("Gold_Monkey","7")
Monster_Gluttonous = Monster("Gluttonous","8")
Monster_White_Fox = Monster("White_Fox","9")
Monster_Goblin_Archer = Monster("Goblin_Archer","10")
Monster_Void_Emperor = Monster("Void_Emperor","11")
def make_monster():
        # 2 = monster in room; else, no monster
        monster_in = random.randrange(3)
        if monster_in == (0 or 1):
                return 0
        monster = random.randrange(5)
        if monster == 0:
                monster = Goblin
        elif monster == 1:
                monster = Tiger
        elif monster == 2:
                monster = Dragon
        elif monster == 3:
                monster = Dark_Turtle
        elif monster == 4:
                monster = Phoenix
        elif monster == 5:
                monster = Ripper
        elif monster == 6:
                monster = Ghoul
        elif monster == 7:
                monster = Gold_Monkey
        elif monster == 8:
                monster = Gluttonous
        elif monster == 9:
                monster = White_Fox
        elif monster == 10:
                monster = Goblin_Archer
        elif monster == 11:
                monster = Void_Emperor
        return monster


# defining the layout of the ghost ship
# ship_map = [
# |Officer's Quarters|Navgation   |First Mate's Quarters|Captain's Quarters|
# | Escape room      |Long Boat   |      Main-Mast      |       Wheel      |
# | Fore Hold        |Cargo Access|     Capstan         |  Officer's Mess  |
# | Live stock Hold  |Infirmary   |     Cable Stores    | Carpenter Stores |
# ]
# initialize the ship's map
ship_map = []


def tile_at(x, y):
    """Locates the tile at a coordinate"""
    if x < 0 or y < 0:
        return None
    try:
        return ship_map[y][x]
    except IndexError:
        return None


# ship's map
ship_dsl = """
|A0|A1|A2|A3|
|B0|B1|B2|B3|
|C0|C1|C2|C3|
|D0|D1|D2|D3|
"""


def is_dsl_valid(dsl):
    """
    Check to make sure there is only one start tile and escape pod.
    Also check that each row has the same number of columns
    """
    if dsl.count("|A0|") != 1:
        return False
    if dsl.count("|B0|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False
    return True


# key to the ship's map
tile_type_dict = {"B0": EscapeBoat,
                  "A3": StartTile,
                  "A1": Monster,
                  "A2": Monster,
                  "A3": Monster,
                  "B1": Monster,
                  "B3": Monster,
                  "C0": Monster,
                  "C2": Monster,
                  "D0": Monster,
                  "D1": Monster,
                  "D2": Monster,
                  "D3": Monster,
                  "D0": Monster,
                  "C3": ViewMapTile,
                  "": None}
# initialize the start tile
start_tile_location = None

# game place
places = {"Ghost Ship": "SV Mary Celeste"}
