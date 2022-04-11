class Warrior:
    def __init__(self, name):
        self.health = 50
        self.attack = 5
        self.name = name

    def is_attacked(self, other):
        if other.is_alive:
            self.health -= other.attack

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    def __init__(self, name):
        self.health = 50
        self.attack = 7
        self.name = name
    

def fight(unit_1, unit_2):
    while unit_1.is_alive and unit_2.is_alive:
        unit_2.is_attacked(unit_1)
        print(f'{unit_2.name} is attacked. Health: {unit_2.health} (-{unit_1.attack})')
        unit_1.is_attacked(unit_2)
        print(f'{unit_1.name} is attacked. Health: {unit_1.health} (-{unit_2.attack})')
    if unit_1.is_alive:
        return f'The winner is {unit_1.name}!'
    else:
        return f'The winner is {unit_2.name}!'


chuck = Warrior('Chuck')
bruce = Warrior('Bruce')
carl = Knight('Carl')
dave = Warrior('Dave')
mark = Warrior('Mark')

print(fight(chuck, carl))