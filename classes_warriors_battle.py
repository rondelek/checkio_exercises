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

        
# return True if unit_1 wins
def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.is_attacked(unit_1)
        unit_1.is_attacked(unit_2)
    return unit_1.is_alive



# checkio test 

chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()
bob = Defender()
mike = Knight()
rog = Warrior()
lancelot = Defender()

fight(chuck, bruce) == True
fight(dave, carl) == False
chuck.is_alive == True
bruce.is_alive == False
carl.is_alive == True
dave.is_alive == False
fight(carl, mark) == False
carl.is_alive == False
fight(bob, mike) == False
fight(lancelot, rog) == True

my_army = Army()
my_army.add_units(Defender, 1)
    
enemy_army = Army()
enemy_army.add_units(Warrior, 2)

army_3 = Army()
army_3.add_units(Warrior, 1)
army_3.add_units(Defender, 1)

army_4 = Army()
army_4.add_units(Warrior, 2)

battle = Battle()

battle.fight(my_army, enemy_army) == False
battle.fight(army_3, army_4) == True
