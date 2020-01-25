import inventory
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
