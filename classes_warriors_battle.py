
class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    def is_attacked(self, other):
        if other.is_alive:
            self.health -= other.attack
    
    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self):
        self.health = 50
        self.attack = 7

class Defender(Warrior):
    def __init__(self):
        self.health = 60
        self.attack = 3
        self.defense = 2

    def is_attacked(self, other):
        if other.is_alive:
            self.health -= max(0, other.attack - self.defense)


class Army:
    def __init__(self):
        self.soldiers = []

    def add_units(self, unit, number):
        for n in range(number):
            self.soldiers.append(unit())
        

    def is_dead(self):
        self.soldiers.pop()

class Battle:
    
    def fight(self, army_1, army_2):

        while len(army_1.soldiers) > 0:
            if fight(army_1.soldiers[-1], army_2.soldiers[-1]):
                army_2.is_dead()
            else:
                army_1.is_dead()
            if len(army_2.soldiers) == 0:
                return True
        return False

        

def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.is_attacked(unit_1)
        unit_1.is_attacked(unit_2)
    return unit_1.is_alive





chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()

army_1 = Army()
army_2 = Army()
army_1.add_units(Warrior, 1)
army_2.add_units(Warrior, 2)
battle = Battle()
battle.fight(army_1, army_2)

print(battle.fight(army_1, army_2))

  