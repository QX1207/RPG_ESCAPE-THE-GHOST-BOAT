# Updated #3 about Modules and Map in the mian_game.py
# Edited person: Qian Xiang
# Last updated date: 11/15/2019


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


# definite the print_map and print it for player
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
print_map()


class CharactersI():
    """CharactersI class with characters' informations"""
    def__init__(self):
        # Player starting coordinates
        self.x =
        self.y =
        """initialize attributes of the parent class"""
        self.hp = 1000
        self.victory =False


    def is_alive(self):
        """player is alive if they have at least 1 HP"""
        return self.hp > 0


    def 
