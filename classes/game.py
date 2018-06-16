import random
from classes.colors import bcolors


class Person:
    def __init__(self, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Melee Attack", "Magic Attack", "Items", "Quit"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_action(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "Actions" + bcolors.ENDC)
        for item in self.actions:
            print("    ", bcolors.BOLD + bcolors.ATTACKTYPE + str(i) + ".", item + bcolors.ENDC)
            i += 1

    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "Magic" + bcolors.ENDC)
        for spell in self.magic:
            print("    ", bcolors.BOLD + bcolors.ATTACKTYPE + str(i), ".", spell.name, "(cost:", str(spell.cost) + ")" +
                  bcolors.ENDC)
            i += 1

    def choose_items(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "Items" + bcolors.ENDC)
        for item in self.items:
            print("    ", bcolors.BOLD + bcolors.ATTACKTYPE + str(i) + ".", item["item"].name + ":", item["item"].desc,
                  "(x" + str(item["quantity"]) + ")" + bcolors.ENDC)
            i += 1
