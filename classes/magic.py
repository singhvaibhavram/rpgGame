import random


class Spell:
    def __init__(self, name, cost, dmg, stype):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.stype = stype

    def generate_damage(self):
        mgl = self.dmg - 15
        mgh = self.dmg + 15
        return random.randrange(mgl, mgh)

    def generate_heal(self):
        return self.dmg