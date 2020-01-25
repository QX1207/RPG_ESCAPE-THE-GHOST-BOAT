# Updated #3 about Modules and Map in the mian_game.py
# Edited person: Qian Xiang
# Last updated date: 11/15/2019


import random
import sys
import boss

class MapTile():
    """ Map with x and y coordinates"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

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


class ViewMapTile(MapTile):
    """Position that prints a map"""
    def intro_text(self):
        """Descriptive text for the Viewable Map Tile"""
        return """
        You see a map on the wall.
        """

    def print_map(self):
        """Print a map of the ghost ship with directions"""
        print_map = """
                                North
    |Officer's Quarters|Navgation   |First Mate's Quarters|Captain's Quarters|
    | Escape Boat      |Long Boat   |      Main-Mast      |       Wheel      |
    | Fore Hold        |Cargo Access|     Capstan         |  Officer's Mess  |
    | Live stock Hold  |Infirmary   |     Cable Stores    | Carpenter Stores |
                                South
    """
    print(self.ship_printable)


class EnemyTile(MapTile):
    """Enemy position and messages"""
    def __init__(self, x, y):
        # Indices j, k for switching alive_text and dead_text messages
        self.j = 0
        self.k = 0
        # generate a random number to estabilish a random enemy
        r = random.random()
        # encounter Drones about 50% of the time
        if r < 0.50:
            self.enemy = enemies.Drone()
            alive_start = """
            """
            alive_attack = "The drone attacks."
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            """
            dead_return = ""
            self.dead_text = [dead_start, dead_return]
            # print(r)
        else:
            self.enemy = enemies.SpaceDucks()
            alive_start = """
            """
            alive_attack = ""
            self.alive_text = [alive_start, alive_attack]
            dead_start = """
            """
            dead_return = ""
            self.dead_text = [dead_start, dead_return]
        super().__init__(x, y)

        def intro_text(self):
        """Intro message dependent on enemy health points"""
        if self.enemy.is_alive():
            # Switch from the intro message after the player starts attacking
            if self.j == 0:
                self.j += 1
                return self.alive_text[0]
            else:
                return self.alive_text[1]
        # switch from the intro message if the player returns to the tile
        # where there is a dead enemy
        else:
            if self.k == 0:
                self.k += 1
                return self.dead_text[0]
            else:
                return self.dead_text[1]

    def modify_player(self, player):
        """
        Checks the enemy's current strength so it can respond to the player
        """
        if self.enemy.is_alive():
            # continue play if there's enough health points
            if player.hp > self.enemy.damage:
                player.hp -= self.enemy.damage
                print("The {} does {} damage. You have {} HP remaining".
                      format(self.enemy.name,
                             self.enemy.damage,
                             player.hp))
            # end the game if the player runs out of health points
            elif player.hp <= self.enemy.damage:
                print("The {} causes mortal damage. You die.".
                      format(self.enemy.name))
                sys.exit()


# defining the layout of the space ship
# ship_map = [
#     [EnemyTile(0, 0), SuppliesTile(1, 0), BoringTile(2, 0)],
#     [BoringTile(0, 1), BoringTile(1, 1), BoringTile(2, 1)],
#     [EnemyTile(0, 2), StartTile(1, 2), EnemyTile(2, 2)],
#     [EscapePod(0, 3), BoringTile(1, 3), BoringTile(2, 3)]
# ]
# initialize the ship's map
ship_map = []


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

def parse_ship_dsl():
    """Taking the ship map as a string and returning a list"""
    if not is_dsl_valid(ship_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = ship_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]
    # Iterate over each line in the DSL.
    for y, dsl_row in enumerate(dsl_lines):
        # Create an object to store the tiles
        row = []
        # Split the line into abbreviations
        dsl_cells = dsl_row.split("|")
        # The split method includes the beginning
        # and end of the line so we need to remove
        # those nonexistent cells
        dsl_cells = [c for c in dsl_cells if c]
        # Iterate over each cell in the DSL line
        for x, dsl_cells in enumerate(dsl_cells):
            # Look up the abbreviation in the dictionary
            tile_type = tile_type_dict[dsl_cells]
            # set the start tile location
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            # If the dictionary returned a valid type, create
            # a new tile object, pass it the X-Y coordinates
            # as required by the tile __init__(), and add
            # it to the row object. If None was found in the
            # dictionary, we just add None.
            row.append(tile_type(x, y) if tile_type else None)
        # Add the whole row to the ship_map
        ship_map.append(row)

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
# |Ghost Door  Escape|Long Boat   |      Main-Mast      |       Wheel      |
# | Fore Hold        |Cargo Access|     Capstan         |  Officer's Mess  |
# | Live stock Hold  |Basement   |     Cable Stores    | Carpenter Stores |
# ]
# initialize the ship's map
# Ship
class Ship(object):
    def __init__(self,first_room):
        self.room = {"Officer's Quarters":Room1(),
                     "Navgation":Room2(),
                     "First Mate's Quarters":Room3(),
                     "Captain's Quarters":Room4(),
                     "Long Boat":Room5(),
                     "Main-Mast":Room6(),
                     "Wheel":Room7(),
                     "Fore Hold":Room8(),
                     "Cargo Access":Room9(),
                     "Capstan":Room10(),
                     "Officer's Mess":Room11(),
                     "Live stock Hold":Room12(),
                     "Cable Stores":Room13(),
                     "Carpenter Stores":Room14(),
                     "Basement":basement(),
                     "Ghost Door":palace()}
        self.first_room = first_room
    def enter_room(self,next_room,now_room):
        next_room = self.room.get(next_room)
        return next_room.enter(now_room)
# Room
class Room(object):
    room_dict = {'room1':1, 'room2':2, 'room3':3, 'room4':4,
                'room5':5, 'room6':6, 'room7':7, 'room8':8,
                'room9':9,'room10':10, 'room11':11, 'room12':12,
                'room13':13, 'room14':14, 'palace':-1,'basement':11}
    toward_dict = {"w":"up","s":"down",
                   "a":"left","d":"right","f":"middle"}
    open_flag = 0
    def enter(self,last_room):
# show the plot in room
        print("---------------------------------------------\n")
        num = re.findall(r"\d",self.room_name)
        if num == []:
            if self.room_name == "palace":
                print("Ghost Door")
            else:
                print("Basement")
        else:
            print("Enter the room" % num[0])
        print(self.words)
# Find the location of player
        self.player_pos = self.get_playerpos(last_room)
# Show the Rooom
        display.display_room(self.player_pos,self.monster,self.monster_pos,
        self.door_pos,self.goods)
# If you went to basement and find the key, you can go to the Ghost Door
        if self.room_name == "basement":
            Room.open_flag = 1
# Enter player loop
        while True:
            print ("Select the following action please: ",
                    "1、Research Goods  2、Fight with Boss  3、Leave the Room")
            print ("'Q' key to show your character attributes ",
                    "'E' key to show the little map")
            choose0 = raw_input('>')
            if choose0 == "q":
                display.display_property(self.monster)
            elif choose0 == "e":
                display.display_pos(self.room_name)
            elif choose0 == "1":
                fight.find_goods(self.goods)
                self.goods = []
            elif choose0 == "2":
                print("Select the Boss：W = W = up, S = down, A = left, ",
                        "D = right, F = Middle, R = Return")
                choose1 = raw_input('>')
                if choose1 == "r":
                    continue
                monster_toward = Room.toward_dict.get(choose1)
                if monster_toward not in self.monster_pos:
                    print("No Boss here ! ! !")
                    continue
                fight.fight(self.monster)
                self.monster_pos.remove(monster_toward)
            elif choose0 == "3":
                print("Select the Room：W = up, S = down, A = left, ",
                        "D = right, R = Return")
                choose2 = raw_input('>')
                if choose2 == "r":
                    continue
                door_toward = Room.toward_dict.get(choose2)
                if door_toward not in self.door_pos:
                    print("That is a wall.")
                    continue
                if door_toward in self.monster_pos:
                    print("You must to beat the boss ",
                            "before you enter the room")
                    continue
                # Base on the direction you will get the next room's name
                num_dict = {"up":-3,"down":3,
                               "left":-1,"right":1}
                next_roomnum = Room.room_dict.get(self.room_name)
                next_roomnum += num_dict.get(door_toward)
                for key,value in Room.room_dict.items():
                    if value == next_roomnum:
                        next_room =  key
                        break
                if next_room == "palace" and Room.open_flag == 0:
                    print("This place is lock. You should find the key first.")
                    continue
                return next_room
            else:
                print("Error。")
    def get_playerpos(self,last_room):
        if last_room == None:
            return "middle"
        last_roomnum = Room.room_dict.get(last_room)
        now_roomnum = Room.room_dict.get(self.room_name)
        num = now_roomnum - last_roomnum
        if num == 3:
            return "up"
        elif num == 1:
            return "left"
        elif num == -1:
            return "right"
        elif num == -3:
            return "down"
        else:
            print("Lose the player's location！")
#Room 1
class Room1(Room):
    def __init__(self):
        self.room_name = "room1"
        self.goods = [u"Holy Sword",u"Middle Hp Medicine"]
        self.monster = ""
        self.monster_pos = []
        self.door_pos = ["right"]
        self.words = "This is a room for storing things, ",
                        "maybe there is something good hidden!"
#房间2
class Room2(Room):
    def __init__(self):
        self.room_name = "room2"
        self.goods = []
        self.monster = u"巫师"
        self.monster_pos = ["left","middle","up","right"]
        self.door_pos = ["left","up","down"]
        self.words = ""
#房间3
class Room3(Room):
    def __init__(self):
        self.room_name = "room3"
        self.goods = [u"圣盾",u"超大血瓶"]
        self.monster = ""
        self.monster_pos = []
        self.door_pos = ["down"]
        self.words = ""
#房间4
class Room4(Room):
    def __init__(self):
        self.room_name = "room4"
        self.goods = []
        self.monster = u"史莱姆"
        self.monster_pos = ["left","middle","up","down"]
        self.door_pos = ["right","down"]
        self.words = ""
#房间5
class Room5(Room):
    def __init__(self):
        self.room_name = "room5"
        self.goods = []
        self.monster = ""
        self.monster_pos = []
        self.door_pos = ["left","right","up","down"]
        self.words = ""
#房间6
class Room6(Room):
    def __init__(self):
        self.room_name = "room6"
        self.goods = []
        self.monster = u"小魔王"
        self.monster_pos = ["up"]
        self.door_pos = ["left","up"]
        self.words = ""
#房间7
class Room7(Room):
    def __init__(self):
        self.room_name = "room7"
        self.goods = [u"小血瓶"]
        self.monster = ""
        self.monster_pos = []
        self.door_pos = ["up"]
        self.words = ""
#房间8
class Room8(Room):
    def __init__(self):
        self.room_name = "room8"
        self.goods = []
        self.monster = u"骑士"
        self.monster_pos = ["left","down","right","middle"]
        self.door_pos = ["down","up","right"]
        self.words = ""
class Room9(Room):
    def __init__(self):
        self.room_name = "room9"
        self.goods = [u"大血瓶",u"圣水"]
        self.monster = ""
        self.monster_pos = []
        self.door_pos = ["left"]
        self.words = ""
#地下室
class basement(Room):
    def __init__(self):
        self.room_name = "basement"
        self.goods = []
        self.monster = u"公主"
        self.monster_pos = ["middle"]
        self.door_pos = ["up"]
        self.words = u"""
        这是一个的地下室，有个人被囚禁在其中。原来是公主！
        你叫醒了公主，说到"公主，我是你父王派来救你的，快跟我走吧！"
        公主揉了揉眼睛，说："非常感谢你英雄，可是我被魔王用法术禁锢在这里了，
        只有打败大魔王，才能离开。大魔王的位置在地图最上边的神秘房间里，
        那个地方十分危险，在进去之前一定要做好充分的准备！"
        "恩，等我的好消息吧！"，你说到。
        """
""
#魔王宫殿
class palace(Room):
    def __init__(self):
        self.room_name = "palace"
        self.goods = []
        self.monster = u"大魔王"
        self.monster_pos = ["middle"]
        self.door_pos = []
        self.words = u"""你走进了大魔王的宫殿。
        "年轻人，你终于来了，我等你很久了。我要告诉你一个不幸的消息，这个房子不打败我
        是无法离开的。哈哈哈，乖乖受死吧！"
        """
