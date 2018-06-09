import random
from classes.colors import bcolors


class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def generate_damage(self):
        mgl = self.dmg - 15
        mgh = self.dmg + 15
        return random.randrange(mgl, mgh)

    def generate_heal(self):
        return self.dmg

    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "Magic" + bcolors.ENDC)
        for spell in self.magic:
            print(bcolors.BOLD + bcolors.ATTACKTYPE + str(i), ":", spell.name, "(cost:", str(spell.cost) + ")" +
                  bcolors.ENDC)
            i += 1

