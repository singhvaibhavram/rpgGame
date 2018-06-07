from classes.game import Person, bcolors
from classes.magic import Spell

# Attack Magic
fire = Spell("Fire Heat", 7, 150, "Elemental")
thunder = Spell("Thunder", 10, 160, "Elemental")
blizzard = Spell("Blizzard", 15, 170, "Elemental")
quake = Spell("Quake", 20, 180, "Ground")
meteor = Spell("Meteor", 23, 190, "Rock")
crunch = Spell("Crunch", 25, 200, "Dark")
darkpulse = Spell("Dark Pulse", 27, 210, "Dark")
shadowball = Spell("Shadow Ball", 30, 220, "Ghost")
destinybond = Spell("Destiny Bond", 33, 230, "Ghost")

# Heal magic
cure = Spell("Recover", 20, 300, "Healing")
cure2 = Spell("Regenerator", 25, 350, "Healing")

player = Person(1550, 45, 20, 34, [fire, thunder, blizzard, quake, meteor, crunch, darkpulse, shadowball, destinybond,
                                   cure, cure2])
enemy = Person(1200, 20, 10, 7, [])

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
        # Magic damage done
        enemy.take_damage(magic_dmg)
        print(bcolors.ATTACKGIVETAKE + bcolors.BOLD + "You attacked for", str(magic_dmg),
              "spell damage!" + bcolors.ENDC)

    # Quit Game
    elif index == 2:
        print(bcolors.FAIL + bcolors.BOLD + "You Quit!" + bcolors.ENDC)
        break

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
