import random


class Item:
    def __init__(self, name, itype, desc, value):
        self.name = name
        self.itype = itype
        self.desc = desc
        self.value = value

    def generate_damage(self):
        idmgl = self.value - 15
        idmgh = self.value + 15
        return random.randrange(idmgl, idmgh)

    def generate_heal(self):
        return self.value
