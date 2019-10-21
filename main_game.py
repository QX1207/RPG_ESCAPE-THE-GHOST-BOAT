# choice a character from 3 character
# character files:
# Character number 1
#   name: doctor Jame Dyer
#   ability: Med Master - you can choose to heal 50 HP
#            when you are fighting with boss


#   name: Thief - Darius Pierson
#   ability: Hoarder - you will get one more weapon after you kill a boss


#   name: Soldier - Naib Collins
#   ability: Skilled - before you enter a new rooom, you can change
#            a random weapon


characters = {
    'Doctor': {
        'firstName': 'Jame',
        'lastName': 'Dyer',
        'ability': 'Med Master - you can choose to heal 50 HP when you are',
        ' fighting with boss',
        },
    'Thief': {
        'firstName': 'Darius',
        'lastName': 'Pierson',
        'ability': 'Hoarder - you will get one more weapon after you',
        'kill a boss',
        },
    'Soldier': {
        'firstName': 'Naib',
        'lastName': 'Collins',
        'ability': 'Skilled - before you enter a new rooom, you can change',
        'a random weapon',
        }

}


for characters, characters_info in characters.items():
v print(f"\nCharacters: {characters}")
w full_name = f"{characters_info['firstName']} {characters_info['lastName']}"
location = characters_info['ability']
x print(f"\tFull name: {full_name.title()}")
print(f"\tLocation: {ability.title()}")
