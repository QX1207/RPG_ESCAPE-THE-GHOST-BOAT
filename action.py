# a list for directions
directions = ['North', 'East', 'South', 'West']
# use for loop to print the list directions one by one
for direction in directions:
    print(direction)
# a statement to explain the choices what do player have
move = "Go in one of the following direction: "
# create a user input 
name = input(move)
# print the statement that explain the characters' action
print(f"\nGo {name}.")
