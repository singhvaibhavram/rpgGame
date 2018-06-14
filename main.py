from classes.game import Person
from classes.magic import Spell
from classes.colors import bcolors
from classes.inventory import Item

# Attack Magic
fire = Spell("Fire Heat", 7, 150, "Dark")
thunder = Spell("Thunder", 10, 160, "Dark")
blizzard = Spell("Blizzard", 15, 170, "Dark")
quake = Spell("Quake", 20, 180, "Dark")
meteor = Spell("Meteor", 23, 190, "Dark")
crunch = Spell("Crunch", 25, 200, "Dark")
dark_pulse = Spell("Dark Pulse", 27, 210, "Dark")
shadow_ball = Spell("Shadow Ball", 30, 220, "Dark")
destiny_bond = Spell("Destiny Bond", 33, 230, "Dark")

# Heal magic
cure = Spell("Recover", 20, 300, "Healing")
cure2 = Spell("Regenerator", 25, 350, "Healing")

# Usables
heal_potion1 = Item("Heal Potion(Low)", "potion", "Heals 50 HP", 50)
heal_potion2 = Item("Hi-Heal Potion", "potion", "Heals 100 HP", 100)
heal_potion3 = Item("Super Heal Potion", "potion", "Heals 500 HP", 500)
heal_elixir = Item("Elixir", "elixir", "Heals full HP/MP of one member", 99999)
heal_mega_elixir = Item("Mega elixir", "elixir", "Heals full HP/MP of the whole team", 999999)

# Damage Items
grenade = Item("Grenade", "throwable", "Deals 500 damage", 500)

# Players
player = Person(1500, 45, 20, 34,
                [fire, thunder, blizzard, quake, meteor, crunch, dark_pulse, shadow_ball, destiny_bond,
                 cure, cure2], [heal_potion1, heal_potion2, heal_potion3, heal_elixir, heal_mega_elixir])
enemy = Person(1200, 50, 100, 7, [], [])

run = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

# Choose the type of attack
while run:
    print("======================================")
    player.choose_action()
    choice = input(bcolors.BOLD + "Choose your attack type: " + bcolors.ENDC)

    index = int(choice) - 1

    # Melee Attack (1)
    if index == 0:
        print(bcolors.ATTACKCHOSEN + bcolors.BOLD + "You chose Melee Attack!", str(index) + bcolors.ENDC)
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(bcolors.ATTACKGIVETAKE + bcolors.BOLD + "You attacked for", str(dmg), "damage!" + bcolors.ENDC)

    # Magic Attack (2)
    elif index == 1:
        print(bcolors.ATTACKCHOSEN + bcolors.BOLD + "You chose Magic Attack!", str(index) + bcolors.ENDC)
        player.choose_magic()
        magic_choice = input(bcolors.BOLD + "Choose your Magic attack: " + bcolors.ENDC)
        magic_index = int(magic_choice) - 1

        spell = player.magic[magic_index]
        magic_dmg = spell.generate_damage()
        magic_heal = spell.generate_heal()

        # Verify if Magic Points Available
        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + bcolors.BOLD + "\nNot enough Magic Points\n" + bcolors.ENDC)
            continue

        # Magic points reduced
        player.reduce_mp(spell.cost)

        # Spell Choice
        print(bcolors.ATTACKCHOSEN + bcolors.BOLD + "You chose", spell.name + "!" +
              bcolors.ENDC)

        # healing
        if spell.stype == "Healing":
            player.heal(magic_heal)
            print(bcolors.ATTACKGIVETAKE + bcolors.BOLD + "You healed yourself for", str(magic_heal),
                  "HP!" + bcolors.ENDC)
        # Dark magic damage done
        elif spell.stype == "Dark":
            enemy.take_damage(magic_dmg)
            print(bcolors.ATTACKGIVETAKE + bcolors.BOLD + "You attacked for", str(magic_dmg),
                  "spell damage!" + bcolors.ENDC)

    # Usable and Items
    elif index == 2:
        print(bcolors.ATTACKCHOSEN + bcolors.BOLD + "You chose Items!", str(index) + bcolors.ENDC)
        player.choose_items()
        items_choice = input(bcolors.BOLD + "Choose Item: " + bcolors.ENDC)
        items_index = int(items_choice) - 1

        item = player.items[items_index]
        item_dmg = item.generate_damage()
        item_heal = item.generate_heal()

        if item.itype == "potion":
            player.heal(item_heal)
            print(bcolors.ATTACKGIVETAKE + bcolors.BOLD + "You healed yourself for", str(item_heal),
                  "HP!" + bcolors.ENDC)

        elif item.itype == "throwable":
            enemy.take_damage(item_dmg)
            print(bcolors.ATTACKGIVETAKE + bcolors.BOLD + "You attacked for", str(item_dmg), "damage!" + bcolors.ENDC)

    # Quit Game
    elif index == 3:
        print(bcolors.FAIL + bcolors.BOLD + "You Quit!" + bcolors.ENDC)
        break

    else:
        print("Such choice does not exists!!")
        continue

    enemy_choice = 1

    if enemy_choice == 1:
        print(bcolors.ATTACKCHOSEN + bcolors.BOLD + "Enemy chose Melee Attack!", str(index) + bcolors.ENDC)
        dmg = enemy.generate_damage()
        player.take_damage(dmg)
        print(bcolors.ATTACKGIVETAKE + bcolors.BOLD + "You were attacked for", str(dmg), "damage!" + bcolors.ENDC)

    # Player and Enemy HP
    print("======================================")
    print(bcolors.BOLD + "Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)
    print("")
    print(bcolors.BOLD + "Player HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + "    "
          + bcolors.ENDC + bcolors.BOLD + "MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp())
          + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + bcolors.BOLD + "You Won!!" + bcolors.ENDC)
        break
    elif player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD + "You Lost!!" + bcolors.ENDC)
        break
