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
        'ability': 'Med Master - you can choose to heal 50 HP when you are'
        'fighting with boss',
        'health': '100'
        },
    'Thief': {
        'firstName': 'Darius',
        'lastName': 'Pierson',
        'ability': 'Hoarder - you will get one more weapon after you'
        'kill a boss',
        'health': '120',
        },
    'Soldier': {
        'firstName': 'Naib',
        'lastName': 'Collins',
        'ability': 'Skilled - before you enter a new rooom, you can change a'
        'random weapon',
        'health': '200',
        },

        }


for characters, characters_info in characters.items():
    print(f"\nCharacters: {characters}")
    full_name = f"{characters_info['firstName']} {characters_info['lastName']}"
    ability = characters_info['ability']
    health = characters_info["health"]
    print(f"\tFull name: {full_name.title()}")
    print(f"\tAblility: {ability.title()}")
    print(f"\t{characters} has {health} health point")
