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


# design the map in my text advanture game
if character == "1":
    print("Your ability is...")
elif choice == "2":
    print("Your ability is...")
else:
    print("Your ability is...")


# design a map for my whole game


# a chest with random weapon
import random
Weapon = ['1', '2']
print("You found a weapon in a chest.",
      f"You get a common weapon {random.choice(Weapon)}!")


# clues about the boos room's passward
if room == "1":
    print("The passward is 2_ _ _")
elif room == "2":
    print("There is not any clue in this room")
elif room == "3":
    print("The passward is _ _ 3 _")
else:
    print("The passward is _ 5 _ _")
