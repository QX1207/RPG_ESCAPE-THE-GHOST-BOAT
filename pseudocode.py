 Course: CS 30
# Period: 1
# Date create: 19/10/01
# Date last modified: 19/10/02
# Name: Qian Xiang
# Description: psceudocodes for my text-based adventure game


# print a statement to welcome player
print('Here is a place that you begin your adventure. Enjoy your time.')


# input the player name
playerName = input("Enter name")


# a selection before player enter the game
if choice == "Begin":
    print("Welcome to Final Tempo")
elif choice == "Imformation":
    print("...")
else:
    print("Closed")


# print the rules



# choice a character from 3 character
if character == "1":
    print("Your ability is...")
elif character == "2":
    print("Your ability is...")
else:
    print("Your ability is...")

# character appear in a random room (empty room)



# get three choices of common Weapon


# show your inventory and weapon bonus


# design a map for my whole game


# design a map for chests


# design a map for monsters and bosses


# 4 choices to go to other room


# find a monster or boss


# show your HP and monster(boss)'s HP


# 4 choice to decide your reaction, a choice to use your weapon, a choice
# to use your character ability, and a choice to use your consumble


# if the character die, it will have two choice 1. 'encourge you and end
# the game' or 2. 'refresh and fight with the monster in that rooom again'


# kill the monster or boss, you will get a passward or the special key


# find a chest and open it


# find a random weapon from chest
import random
Weapon = ['1', '2']
print("You found a weapon in a chest.",
      f"You get a common weapon {random.choice(Weapon)}!")


# find a random consumble from chest


# clues about the boos room's passward
if room == "1":
    print("The passward is 2_ _ _")
elif room == "2":
    print("There is not any clue in this room")
elif room == "3":
    print("The passward is _ _ 3 _")
else:
    print("The passward is _ 5 _ _")


# make a lock on the door to escape(two way to open the door)


# use the special key what did you got from the special chest to open the door


# if you did not get the chest, input passward to escape


# if passward is incorrect, you can type the passward again or continus your
# adventure


# door was open, you success to escape and end the game
