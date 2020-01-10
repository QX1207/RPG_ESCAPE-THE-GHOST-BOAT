import weapon
import map

class Player:
    """Player class with inventory and weapon"""
    def __init__(self):
        # begining weapon in inventory
        self.inventory = [weapon.Wood_Sword())]
        # player starting coordinates
        self.x = ship.start_tile_location[0]
        self.y = ship.start_tile_location[1]
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

    def move_forward(self):
        """Define forward movement"""
        self.move(dx=0, dy=-1)

    def move_aftward(self):
        """Define aftward movement"""
        self.move(dx=0, dy=1)

    def move_starboard(self):
        """Define movement towards the starboard side"""
        self.move(dx=1, dy=0)

    def move_port(self):
        """Define movement towards the port side"""
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

    def heal(self):
        """Check and use consumables for healing"""
        # add consumables from the inventory
        consumables = [item for item in self.inventory
                       if isinstance(item, items.Consumable)]

        # print a message if there are no consumables
        if not consumables:
            print("You do not have any items to heal you!")
            return

        # print out a list of available consumables
        print("Choose an item to use to heal yourself: ")
        for i, item in enumerate(consumables, 1):
            print("{}. {}".format(i, item))

        # choose a consumable from the list and use it
        valid = False
        while not valid:
            choice = input("")
            try:
                to_use = consumables[int(choice) - 1]
                # cap player's health points to 100
                self.hp = min(100, self.hp + to_use.healing_value)
                # remove the used item from the inventory
                # and print current health points
                self.inventory.remove(to_use)
                print("Current HP: {}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("Invalid choice, try again.")

    def protect(self):
        """Check and use items for protection"""
        # add protection items from Inventory
        protection = [item for item in self.inventory
                      if isinstance(item, items.Protection)]
        # print a message if there are no protection items
        if not protection:
            print("You do not have any items to protect you!")
            return
        position = ship.tile_at(self.x, self.y)
        enemy = position.enemy
        # bread = items.CrustyBread()
        if enemy.name == "Flock of Blue Space Ducks":
            print("Bread protection value against ducks is -100 Damage")
        # print out a list of available protection items
        print("Choose an item to use to protect yourself: ")
        for i, item in enumerate(protection, 1):
            print("{}. {}".format(i, item))
        # choose a protection item from the list and use it
        valid = False
        while not valid:
            choice = input("")
            try:
                to_use = protection[int(choice) - 1]
                # remove used item from the inventory
                self.inventory.remove(to_use)
                if enemy.name == "Flock of Blue Space Ducks":
                    if to_use.name == "Crusty Bread":
                        to_use.protect_value = 100
                else:
                    if to_use.name == "Crusty Bread":
                        to_use.protect_value = 0

                # decrease damage by using a protection item
                # limit enemy damage to not drop below 0
                enemy.damage = enemy.damage - to_use.protect_value
                if enemy.damage > 0:
                    return enemy.damage
                else:
                    enemy.damage = 0
                    return enemy.damage
                print("Potential Damage: {}".format(enemy.damage))
                valid = True
            except (ValueError, IndexError):
                print("Invalid choice, try again.")

    def add_supplies(self):
        """Add supplies to the player's inventory when supplies are found"""
        # define the position in the ship
        position = ship.tile_at(self.x, self.y)
        # add the inventory from the supply tile to the player's inventory
        current_inventory = self.inventory
        position.add_inventory(current_inventory)
