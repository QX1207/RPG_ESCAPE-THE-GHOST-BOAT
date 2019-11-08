# imnport random
import random
# print out a statement about the story
print("There are some monsters on the ship. Let us begin the adventure.")
# create a llist about the directions
playerDirections = ["North", "East", "South", "West(quit)"]


# create a definition of the function
# use for loop to print my selections
def directions(playerDirections):
    for playerDirection in playerDirections:
        print(
            f"{playerDirections.index(playerDirection) + 1}.{playerDirection}"
            )
# print out a statement that introduce the choices they face
    print("Go in one of the direction above (please enter the number):")
# after for loop, use while loop to repeat the question until it is break
while True:
    directions(playerDirections)
# create a user input
    selections = int(input("Enter choice: "))
# use if-elif-else statement to explain different movements
    if selections == 1:
        print("You are going forward to the next room.")
        print("\n")
    elif selections == 2:
        print("You are going to the right room.")
        print("\n")
    elif selections == 3:
        print("You are going backward.")
        print("\n")
    elif selections == 4:
        print("You are going to the left room. You find the monster!")
        print("\n")
        break
    else:
        print("Please enter the following number of directions to move")
        print("\n")


# 7 choice to decide your reaction, attack(make damage to the boss),
# dodge(dodge the boss's attack and make a few damage to the boss, maybe fail),
# defense(defense a part a damage from the boss), run back(),
# a choice to use your weapon, a choice to use your character ability
# (only doctor yet), and a choice to use your consumble


# print a multiple choise question about the action
print("Choose the following action to beat the boss",
      "(please enter the number): ")
# create a list about the character's actions when you meet a bosses
characterActions = ['attack', 'dodge', 'defense', 'run back(quit)',
                    'use your ability', 'use your weapon',
                    'use your consumble']


# create a definition of the function
# use for loop to print my selections
def behavior(characterActions):
    for characterAction in characterActions:
        print(
            f"{characterActions.index(characterAction) + 1}. {characterAction}"
            )
# after for loop, use while loop to repeat the question until it is break
while True:
    behavior(characterActions)
    # create a user input
    actions = int(input("You choose to "))
# use if-elif-else statement to explain different action from you character
    if actions == 1:
        print("You make damage to the boss.")
        print("\n")
    elif actions == 2:
        dodge = ("You dodge the boss's attack and make a few damage to"
                 " the boss.",
                 "Boss speed is very fast. You dodged that fail.")
        print(random.choice(dodge))
        print("\n")
    elif actions == 3:
        print("You defense a part a damage from the boss.")
        print("\n")
    elif actions == 4:
        print("You run back to the last room.")
        print("\n")
        break
    elif actions == 5:
        print("Ablility list")
        print("\n")
    elif actions == 6:
        print("Weapon Inventory")
        print("\n")
    elif actions == 7:
        print("Consumble Inventory")
        print("\n")
    else:
        print("Please enter a number to finish your action")
        print("\n")
