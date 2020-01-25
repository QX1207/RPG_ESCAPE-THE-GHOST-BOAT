# Updated #3 about Modules and Map in the mian_game.py
# Edited person: Qian Xiang
# Last updated date: 11/15/2019


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
