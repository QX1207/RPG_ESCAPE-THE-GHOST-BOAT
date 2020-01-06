# Updated #3 about Modules and Map in the mian_game.py
# Edited person: Qian Xiang
# Last updated date: 11/15/2019


import random

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


# definite the print_map and print it for player in a class
class visual_map:
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


main_map()
visual_map()


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


class CharactersI():
    """CharactersI class with characters' informations"""
    def __init__(self, x, y):
        # Player starting coordinates
        self.x = x
        self.y = y
        """initialize attributes of the parent class"""
        self.hp = 1000
        self.victory = False

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
