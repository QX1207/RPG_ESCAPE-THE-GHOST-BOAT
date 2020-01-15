class Character():
    def __init__(self):
        raise NotImplementedError("Do not create raw character objects")

    def __str__(self):
        return self.name, self.identity, self.ability, self.hp

    def is_alive(self):
        return self.hp > 0


class Doctor(Character):
    """Doctor's name, identity and characteristics """
    def __init__(self):
        self.name = "Doctor"
        self.identity = "Jame Dyer"
        self.power = "ability: Med Master - you can choose",
        "to heal 50 HP when you are fighting with boss"
        self.hp = 1000


class Thief(Character):
    """Thief's name, idenity and characteristics"""
    def __init__(self):
        self.name = "Thief"
        self.identity = "Darius Pierson"
        self.power = "Hoarder - you will get one more weapon after you"
        "kill a boss"
        self.hp = 1200


class Soldier(Character):
    """The Soldier's name, idenity and characteristics"""
    def __init__(self):
        self.name = "Soldier"
        self.identity = "Naib Collins"
        self.power = "Skilled - you has 50% to attack the boss twice in a time"
        self.hp = 1500


# assign variables to hero classes and put them in a list
Doctor = Doctor()
Thief = Thief()
Soldier = Soldier()
characters = [Doctor.name, Thief.name, Soldier.name]


def character_check(character):
    """Checks which character was chosen and prints out the characteristics"""
    if character == "Doctor":
        character_characteristics(Doctor)
    elif character == "Thief":
        character_characteristics(Thief)
    else:
        character_characteristics(Soldier)


def character_characteristics(character):
    """Prints out the hero's characteristics"""
    print(f"{character.name}'s true identy is {character.identity}")
    print(f"{character.name}'s super power is {character.power}")
    print(f"{character.name} has {character.hp} health points")
