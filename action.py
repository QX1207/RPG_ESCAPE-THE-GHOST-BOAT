# print all directions what can player choose
print("1. North")
print("2. East")
print("3. South")
print("4. West")
# print out a statement that introduce the choices they face
print("Go in one of the direction above (please enter the number):")
# create a user input
questions = int(input("Enter choice: "))
# use if-elif-else statement to explain different movements
if selection == 1:
    print("You are going forward to the next room.")
elif selection == 2:
    print("You are going to the right room.")
elif selection == 3:
    print("You are going backward.")
else:
    print("You are going to the left room.")
