import random
from classes.colors import bcolors


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
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
        print("\n" + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "    Actions" + bcolors.ENDC)
        for item in self.actions:
            print("        ", bcolors.BOLD + bcolors.ATTACKTYPE + str(i) + ".", item + bcolors.ENDC)
            i += 1

    def choose_magic(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "        Magic" + bcolors.ENDC)
        for spell in self.magic:
            print("            ", bcolors.BOLD + bcolors.ATTACKTYPE + str(i), ".", spell.name, "(cost:", str(spell.cost)
                  + ")" + bcolors.ENDC)
            i += 1

    def choose_items(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "        Items" + bcolors.ENDC)
        for item in self.items:
            print("            ", bcolors.BOLD + bcolors.ATTACKTYPE + str(i) + ".", item["item"].name + ":",
                  item["item"].desc, "(x" + str(item["quantity"]) + ")" + bcolors.ENDC)
            i += 1

    def get_enemy_stats(self):
        hp_display = str(self.hp) + "/" + str(self.maxhp)

        healthbar = ""

        health_bar = (self.hp / self.maxhp) * 100 / 2

        while health_bar > 0:
            healthbar += "█"
            health_bar -= 1

        while len(healthbar) < 50:
            healthbar += " "

        current_hp = ""

        if len(hp_display) < 11:
            decreased = 11 - len(hp_display)
            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_display

        else:
            current_hp = hp_display

        print("                        __________________________________________________")
        print(bcolors.BOLD + self.name + "    " + current_hp + " |" + bcolors.FAIL + healthbar + bcolors.ENDC + "|")

    def get_player_stats(self):
        hp_display = str(self.hp) + "/" + str(self.maxhp)
        mp_display = str(self.mp) + "/" + str(self.maxmp)

        healthbar = ""
        mpbar = ""

        health_bar = (self.hp / self.maxhp) * 100 / 4
        mp_bar = (self.mp / self.maxmp) * 100 / 10

        while health_bar > 0:
            healthbar += "█"
            health_bar -= 1

        while len(healthbar) < 25:
            healthbar += " "

        while mp_bar > 0:
            mpbar += "█"
            mp_bar -= 1

        while len(mpbar) < 10:
            mpbar += " "

        current_hp = ""
        current_mp = ""

        if len(hp_display) < 9:
            decreased = 9 - len(hp_display)
            while decreased > 0:
                current_hp += " "
                decreased -= 1

            current_hp += hp_display

        else:
            current_hp = hp_display

        if len(mp_display) < 7:
            decreased = 7 - len(mp_display)
            while decreased > 0:
                current_mp += " "
                decreased -= 1

            current_mp += mp_display

        else:
            current_mp = mp_display

        print("                        _________________________               __________")
        print(bcolors.BOLD + self.name + "    " + current_hp + "   |" + bcolors.OKGREEN + healthbar + bcolors.ENDC
              + bcolors.BOLD + "|    " + current_mp + "  |" + bcolors.OKBLUE + mpbar + bcolors.ENDC + bcolors.BOLD
              + "|" + bcolors.ENDC)
