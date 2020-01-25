# Updated #3 about Modules and Map in the mian_game.py
# Edited person: Qian Xiang
# Last updated date: 11/15/2019


# map tile types
map_tiles = {"Enemy": {"description": "location of an enemy",
                       "abbreviation": "ET",
                       "action": "must defeat the enemy to continue"},
             "Boss": {"description":
                          "Boss enemy location and the exit for the city",
                          "abbreviation": "BT",
                          "action":
                          "may run away or fight the boss to continue"},
             "Weapons": {"description": "location of a weapon",
                         "abbreviation": "WT",
                         "action":
                         "may pick up items or move to another location"},
             " ": {"description":
                   "location with no items",
                   "abbreviation": "BT",
                   "action": "may rest or move to another location"},
             "Start": {"description": "entrance to the city",
                       "abbreviation": "S",
                       "action": "may rest or move to another location"}
             }


class MapTile():
    """ Map with x and y coordinates"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return self.description, self.action, self.name

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):
        """Added modify_player to every tile"""
        pass


class StartTile(MapTile):
    """Player starting position"""

    def intro_text(self):
        """Descriptive text for the Start Tile"""
        return """
        """


class BoringTile(MapTile):
    """Position with no materials"""
    def intro_text(self):
        return """
        There are no boss and weapon here.
        """


class ViewMapTile(MapTile):
    """Position that prints a map"""
    def intro_text(self):
        """Descriptive text for the Viewable Map Tile"""
        return """
        You see a map on the wall.
        """

    def print_map(self):
        """Print a map of the ship with directions"""
        return """
|Officer's Quarters|Navgation   |First Mate's Quarters|Captain's Quarters|
|Ghost Door  Escape|Long Boat   |      Main-Mast      |       Wheel      |
| Fore Hold        |Cargo Access|     Capstan         |  Officer's Mess  |
| Live stock Hold  |Basement    |     Cable Stores    | Carpenter Stores |
        """


class Boss(MapTile):
    """Position that contains the main villin of the level"""
    def modify_player(self, player):
        """Player wins the level if they beat the big boss"""
        player.victory = True
        sys.exit()

    def intro_text(self):
        return """
        """

class EnemyTile(MapTile):


def append_list(dictionary, list):
    """Create a list from elements of a dictionary"""
    for x in dictionary:
        list.append(x)


def replace_tile(list, tile1, tile2):
    """Make sure that replaced tiles do not overwrite each other"""
    while random_tile(list, tile1) == random_tile(list, tile2):
            random_tile(list, tile1)
            random_tile(list, tile2)


def random_tile(list, tile):
    """Choose a random tile to replace and return the indices"""
    x = random.choice(list)
    y = random.choice(x)
    n = list.index(x)
    m = x.index(y)
    list[n][m] = tile
    return (n, m)


def generate_map(list):
    """randomly generate a 5x5 city map from tile types"""
    map = [[random.choice(list) for i in range(5)] for j in range(5)]
    # add boss and start tiles
    replace_tile(map, "Boss", "Start")
    return map


def print_map(dictionary):
    """print out each city map generated"""
    for key in dictionary:
        map = dictionary[key]
        print(f"{key}")
        # format the maps in rows and columns
        print(tabulate(map, tablefmt="plain"))
        print("\n")


def tile_at(x, y):
    """Locates the tile at a coordinate"""
    if x < 0 or y < 0:
        return None
    try:
        return map[y][x]
    except IndexError:
        return None


# game Ships
Ships = {"Ghost Ship": "First place"
          }


# generate a list of Ships
Ship_level = []
append_list(cities, city_level)
# generate a list of tile types removing the start and boss tiles
tile_types = []
append_list(map_tiles, tile_types)
tile_types.remove("Boss")
tile_types.remove("Start")

# organize each city level and its map in a dictionary
main_map = {}
for Ship in Ship_level:
    Ship_map = generate_map(tile_types)
    main_map[city] = Ship_map

# print_map(main_map)
