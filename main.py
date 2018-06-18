from classes.game import Person
from classes.magic import Spell
from classes.colors import bcolors
from classes.inventory import Item

# Attack Magic
fire = Spell("Fire Heat", 27, 150, "Dark")
thunder = Spell("Thunder", 30, 160, "Dark")
blizzard = Spell("Blizzard", 35, 170, "Dark")
quake = Spell("Quake", 40, 180, "Dark")
meteor = Spell("Meteor", 43, 190, "Dark")
crunch = Spell("Crunch", 45, 200, "Dark")
dark_pulse = Spell("Dark Pulse", 47, 210, "Dark")
shadow_ball = Spell("Shadow Ball", 50, 220, "Dark")
destiny_bond = Spell("Destiny Bond", 53, 230, "Dark")

# Heal magic
cure = Spell("Recover", 20, 300, "Healing")
cure2 = Spell("Regenerator", 25, 350, "Healing")

# Usables
heal_potion1 = Item("Heal Potion(Low)", "potion", "Heals 50 HP", 150)
heal_potion2 = Item("Hi-Heal Potion", "potion", "Heals 100 HP", 200)
heal_potion3 = Item("Super Heal Potion", "potion", "Heals 500 HP", 600)
heal_elixir = Item("Elixir", "elixir", "Heals full HP/MP of one member", 99999)
heal_mega_elixir = Item("Mega Elixir", "elixir", "Heals full HP/MP of the whole team", 999999)

# Damage Items
grenade = Item("Grenade", "throwable", "Deals 500 damage", 500)

# Used by player
player_magic = [fire, thunder, blizzard, quake, meteor, crunch, dark_pulse, shadow_ball, destiny_bond, cure, cure2]
player_usables = [{"item": heal_potion1, "quantity": 50}, {"item": heal_potion2, "quantity": 20},
                  {"item": heal_potion3, "quantity": 3}, {"item": heal_elixir, "quantity": 2},
                  {"item": heal_mega_elixir, "quantity": 2}, {"item": grenade, "quantity": 2}]

# Players
player1 = Person("Albus :", 4567, 245, 80, 34, player_magic, player_usables)
player2 = Person("RJoule:", 3647, 245, 100, 34, player_magic, player_usables)
player3 = Person("Bunny :", 4125, 245, 120, 34, player_magic, player_usables)
enemy = Person("Thanos:", 12000, 245, 300, 7, [], [])

players = [player1, player2, player3]

run = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

# Choose the type of attack
while run:
    print("======================================")
    print("\n")

    for player in players:
        player.get_player_stats()
    print("\n")

    enemy.get_enemy_stats()
    print("\n")

    for player in players:

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

            if magic_index == -1:
                continue

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
            print(bcolors.ATTACKCHOSEN + bcolors.BOLD + "You chose", spell.name + "!" + bcolors.ENDC)

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

            if items_index == -1:
                continue

            item = player.items[items_index]["item"]

            if player.items[items_index]["quantity"] == 0:
                print(bcolors.FAIL + bcolors.BOLD + "\nNot enough", item.name, "\n" + bcolors.ENDC)
                continue

            item_dmg = item.generate_damage()
            player.items[items_index]["quantity"] -= 1

            # Item Choice
            print(bcolors.ATTACKCHOSEN + bcolors.BOLD + "You chose", item.name + "!" + bcolors.ENDC)

            if item.itype == "potion":
                player.heal(item.value)
                print(bcolors.ATTACKGIVETAKE + bcolors.BOLD + "You healed yourself for", str(item.value),
                      "HP!" + bcolors.ENDC)

            elif item.itype == "elixir":
                if item.name == "Mega Elixir":
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print(bcolors.ATTACKGIVETAKE + bcolors.BOLD + "You fully restored your Team's HP and MP!" + bcolors.ENDC)

                else:
                    player.hp = player.maxhp
                    player.mp = player.maxmp
                    print(bcolors.ATTACKGIVETAKE + bcolors.BOLD + "You fully restored your HP and MP!" + bcolors.ENDC)

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

    if index == 3:
        break

    enemy_choice = 1

    if enemy_choice == 1:
        print(bcolors.ATTACKCHOSEN + bcolors.BOLD + "Enemy chose Melee Attack!" + bcolors.ENDC)
        dmg = enemy.generate_damage()

        for player in players:
            player.take_damage(dmg)
            
        print(bcolors.ATTACKGIVETAKE + bcolors.BOLD + "You were attacked for", str(dmg), "damage!" + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + bcolors.BOLD + "You Won!!" + bcolors.ENDC)
        break
    elif player1.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD + "You Lost!!" + bcolors.ENDC)
        break
