import weapon
import map
import random

class Player:
    """Player class with inventory and weapon"""
    def __init__(self):
        # begining weapon in inventory
        self.weapons = [random.commonWeapon())]
        # player starting coordinates
        self.x = ship.start_tile_location[0]
        self.y = ship.start_tile_location[4]
        # self.x = 1
        # self.y = 2
        self.hp = 100
        self.victory = False

    def is_alive(self):
        """The player is alive if they have at least 1 HP"""
        return self.hp > 0

    def print_inventory(self):
        """Print the inventory of items and the best weapon"""
        print("Inventory:")
        for item in self.inventory:
            print("* " + str(item))
        best_weapon = self.most_powerful_weapon()
        print("Your best weapon is your {}".format(best_weapon))

    def most_powerful_weapon(self):
        """Determine the most power weapon in the inventory"""
        max_damage = 0
        best_weapon = None
        # check the damage of each weapon in the inventory
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass
        return best_weapon

    def move(self, dx, dy):
        """Define player movement"""
        self.x += dx
        self.y += dy

    def move_upstairs(self):
        """Define upstairs movement"""
        self.move(dx=0, dy=-1)

    def move_downstairs(self):
        """Define downstairs movement"""
        self.move(dx=0, dy=1)

    def move_forward(self):
        """Define forward movement"""
        self.move(dx=1, dy=0)

    def move_afterward(self):
        """Define afterward movement"""
        self.move(dx=-1, dy=0)

    def attack(self):
        """Attack the enemy by removing health points"""
        # always use the best weapon in the inventory
        best_weapon = self.most_powerful_weapon()
        # define the enemy's poition in the ship
        position = ship.tile_at(self.x, self.y)
        enemy = position.enemy
        # declare which weapon is used and change the value of the enemy's hp
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        # print out if the enemy is alive and how many hps remain
        if not enemy.is_alive():
            print("You killed a {}".format(enemy.name))
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))

    def add_supplies(self):
        """Add supplies to the player's inventory when supplies are found"""
        # define the position in the ship
        position = ship.tile_at(self.x, self.y)
        # add the inventory from the supply tile to the player's inventory
        current_inventory = self.inventory
        position.add_inventory(current_inventory)

import copy
u"""
本模块用于配置玩家和怪物的属性，提供战斗函数。另外提供一个物品使用函数。
"""
#配置玩家属性
player_property = {u"名字":u"卡尔",u"生命值":100,u"攻击力":10,u"护甲":10,u"经验":0,u"符号":"(^_^)"}
##配置怪物属性
Slime_property = {u"名字":u"史莱姆",u"生命值":25,u"攻击力":15,u"护甲":15,u"符号":"~0Y0~"}
wizard_property = {u"名字":u"巫师",u"生命值":50,u"攻击力":40,u"护甲":10,u"符号":">@Y@<"}
knight_property = {u"名字":u"骑士",u"生命值":350,u"攻击力":30,u"护甲":50,u"符号":"\OYO/"}
s_devil_property = {u"名字":u"小魔王",u"生命值":400,u"攻击力":100,u"护甲":100,u"符号":"~/-Y-\~"}
g_devil_property = {u"名字":u"大魔王",u"生命值":3000,u"攻击力":300,u"护甲":300,u"符号":"~~//-Y-\\\~~"}
princess_property = {u"名字":u"公主",u"符号":"^o^"}
def fight(monster):
    u"""
    函数功能：让玩家和怪物进行战斗，若玩家胜利，则设置玩家剩余生命值，若失败，则退出游戏。
    输入参数：monster--怪物，有效的值：u"史莱姆"，u"巫师"，u"骑士"，u"小魔王"，u"大魔王"
    """
    global player_property,Slime_property,wizard_property
    global knight_property,s_devil_property,g_devil_property
    #判断是什么怪物
    if monster == Slime_property[u"名字"]:
        monster_property = copy.deepcopy(Slime_property)
    elif monster == wizard_property[u"名字"]:
        monster_property = copy.deepcopy(wizard_property)
    elif monster == knight_property[u"名字"]:
        monster_property = copy.deepcopy(knight_property)
    elif monster == s_devil_property[u"名字"]:
        monster_property = copy.deepcopy(s_devil_property)
    elif monster == g_devil_property[u"名字"]:
        monster_property = copy.deepcopy(g_devil_property)
    elif monster == princess_property[u"名字"]:
        print u"是不是傻！公主你也杀。"
        exit()
    else:
        print u"怪物名字输入错误！"
        exit()
#开始战斗
    who_round = "player"
    while player_property[u"生命值"] > 0 and monster_property[u"生命值"] > 0:
        if who_round == "player":
            monster_property[u"生命值"] -= (player_property[u"护甲"] + player_property[u"攻击力"])
            who_round = "monster"
        else:
            player_property[u"生命值"] -= (monster_property[u"护甲"] + monster_property[u"攻击力"])
            who_round = "player"
#战斗结果处理
    if player_property[u"生命值"] <= 0:
        print u'"不自量力的家伙，哼!"  怪物将你大卸八块，吃掉了！'
        print u"你被打败了，游戏结束！"
        exit()
    else:
        print u"你打败了怪物，赢得了胜利，获得25点经验！"
        player_property[u"经验"] += 25
#打败小魔王升3级
    if monster == s_devil_property[u"名字"]:
            print u"打败小魔王，连升3级!生命值+300，攻击力加30，护甲加30！"
            player_property[u"生命值"] += 300
            player_property[u"攻击力"] += 30
            player_property[u"护甲"] += 30
#打败大魔王游戏结束
    if monster == g_devil_property[u"名字"]:
            print u"""
            "啊~不，不可能！我竟然被打败了！"，大魔王怒吼道,
            "既然你打败了我，那么我就要你陪葬，你们谁都跑不了，哈哈哈哈哈~"
            这时地动山摇，墙壁开裂，屋顶的石头不断落下，魔塔开始坍塌。
            你趁机从墙壁的裂缝里溜了出去，救出了公主。
            从此，英雄卡尔的名字成了一个传说~
            恭喜你，通关！
            """
            exit()
#经验达到100升级属性
    if player_property[u"经验"] == 100:
        print u"恭喜你，升了1级，生命值+100，攻击力加10，护甲加10！"
        player_property[u"生命值"] += 100
        player_property[u"攻击力"] += 10
        player_property[u"护甲"] += 10
        player_property[u"经验"] = 0
def forecast_fight(monster):
    u"""
    函数功能：预测玩家和怪物战斗需要的生命值
    输入参数：monster--怪物名字，有效的值：u"史莱姆"，u"巫师"，u"骑士"，u"小魔王"，u"大魔王"
    返回参数：health--消耗玩家的生命值
    """
    global player_property,Slime_property,wizard_property
    global knight_property,s_devil_property,g_devil_property
    #判断是什么怪物
    if monster == Slime_property[u"名字"]:
        monster_property = copy.deepcopy(Slime_property)
    elif monster == wizard_property[u"名字"]:
        monster_property = copy.deepcopy(wizard_property)
    elif monster == knight_property[u"名字"]:
        monster_property = copy.deepcopy(knight_property)
    elif monster == s_devil_property[u"名字"]:
        monster_property = copy.deepcopy(s_devil_property)
    elif monster == g_devil_property[u"名字"]:
        monster_property = copy.deepcopy(g_devil_property)
    else:
        print u"怪物名字输入错误！"
        exit()
    player_health =  player_property[u"生命值"]
#模拟战斗
    who_round = "player"
    while monster_property[u"生命值"] > 0:
        if who_round == "player":
            monster_property[u"生命值"] -= (player_property[u"护甲"] + player_property[u"攻击力"])
            who_round = "monster"
        else:
            player_health -= (monster_property[u"护甲"] + monster_property[u"攻击力"])
            who_round = "player"
#计算消耗的血量
    health = player_property[u"生命值"] - player_health
    return health
def find_goods(goods):
    u"""
    函数功能：搜索物品
    输入参数：goods--物品，类型--列表
    """
    if goods == []:
        print u"什么都没找到！"
    else:
        for good in goods:
            if good == u"小血瓶":
                print u"你获得一个小血瓶，生命值增加100点！"
                player_property[u"生命值"] += 100
            elif good == u"中血瓶":
                print u"你获得一个中血瓶，生命值增加200点！"
                player_property[u"生命值"] += 200
            elif good == u"大血瓶":
                print u"你获得一个大血瓶，生命值增加400点！"
                player_property[u"生命值"] += 400
            elif good == u"超大血瓶":
                print u"你获得一个超大血瓶，生命值增加600点！"
                player_property[u"生命值"] += 600
            elif good == u"圣水":
                print u"你获得一瓶圣水，生命值增加一倍！攻击力增加一倍！护甲增加一倍！"
                player_property[u"生命值"] *= 2
                player_property[u"攻击力"] *= 2
                player_property[u"护甲"] *= 2
            elif good == u"圣剑":
                print u"你获得一把圣剑，攻击力增加100！"
                player_property[u"攻击力"] += 100
            elif good == u"圣盾":
                print u"你获得一个圣盾，护甲增加100！"
                player_property[u"护甲"] += 100
            elif good == u"钥匙":
                print u"你获得一把钥匙！"
            else:
                print u"物品名称错误！"
