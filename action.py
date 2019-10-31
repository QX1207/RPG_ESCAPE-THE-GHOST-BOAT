# imnport random
import random
# print all directions what can player choose
print("1. North")
print("2. East")
print("3. South")
print("4. West")
# print out a statement that introduce the choices they face
print("Go in one of the direction above (please enter the number):")
# create a user input
selections = int(input("Enter choice: "))
# use if-elif-else statement to explain different movements
if selections == 1:
    print("You are going forward to the next room.")
elif selections == 2:
    print("You are going to the right room.")
elif selections == 3:
    print("You are going backward.")
else:
    print("You are going to the left room.")


# 7 choice to decide your reaction, attack(make damage to the boss),
# dodge(dodge the boss's attack and make a few damage to the boss, maybe fail),
# defense(defense a part a damage from the boss), run back(),
# a choice to use your weapon, a choice to use your character ability
# (only doctor yet), and a choice to use your consumble
# print a multiple choise question about the action
print("Choose the following action to beat the boss",
      "(please enter the number): ")
# create a list about the character's actions when you meet a bosses
characterActions = ['attack', 'dodge', 'defense', 'run back',
                    'use your ability', 'use your weapon',
                    'use your consumble']
# use for loop to print my selections
for characterAction in characterActions:
    print(f"{characterActions.index(characterAction) + 1}, {characterAction}")
# create a user input
actions = int(input("You choose to "))
# use if-elif-else statement tp explain different acton from you character
if actions == 1:
    print("You make damage to the boss.")
elif actions == 2:
    dodge = ("You dodge the boss's attack and make a few damage to the boss.",
             "Boss speed is very fast. You dodged that fail.")
    print(random.choice(dodge))
elif actions == 3:
    print("You defense a part a damage from the boss.")
elif actions == 4:
    print("You run back to the last room.")
elif actions == 5:
    print("Ablility list")
elif actions == 6:
    print("Weapon Inventory")
else:
    print("Consumble Inventory")
