from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 7, "dmg": 150},
         {"name": "Thunder", "cost": 10, "dmg": 160},
         {"name": "Blizzard", "cost": 15, "dmg": 170}]

player = Person(1550, 45, 20, 34, magic)
enemy = Person(1200, 20, 10, 7, magic)

run = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

while run:
    print("======================================")
    player.choose_action()
    choice = input(bcolors.BOLD + "Choose your attack type: " + bcolors.ENDC)

    index = int(choice) - 1

    # Melee Attack
    if index == 0:
        print(bcolors.ATTACKCHOSEN + bcolors.BOLD + "You chose Melee Attack!", str(index) + bcolors.ENDC)
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(bcolors.ATTACKGIVETAKE + bcolors.BOLD + "You attacked for", str(dmg), "damage!", "Enemy HP reduced to",
              str(enemy.get_hp()) + bcolors.ENDC)

    # Magic Attack
    elif index == 1:
        print(bcolors.ATTACKCHOSEN + bcolors.BOLD + "You chose Magic Attack!", str(index) + bcolors.ENDC)
        player.choose_magic()
        magic_choice = input(bcolors.BOLD + "Choose your Magic attack: " + bcolors.ENDC)
        magic_index = int(magic_choice) - 1
        if magic_index == 0:
            print(bcolors.ATTACKCHOSEN + bcolors.BOLD + "You chose", player.get_spell_name(magic_index) + "!" +
                  bcolors.ENDC)
        elif magic_index == 1:
            print(bcolors.ATTACKCHOSEN + bcolors.BOLD + "You chose", player.get_spell_name(magic_index) + "!" +
                  bcolors.ENDC)
        elif magic_index == 2:
            print(bcolors.ATTACKCHOSEN + bcolors.BOLD + "You chose", player.get_spell_name(magic_index) + "!" +
                  bcolors.ENDC)

        magic_dmg = player.generate_spell_damage(magic_index)
        enemy.take_damage(magic_dmg)
        print(bcolors.ATTACKGIVETAKE + bcolors.BOLD + "You attacked for", str(magic_dmg), "damage!",
              "Enemy HP reduced to", str(enemy.get_hp()) + bcolors.ENDC)

    # Quit Game
    elif index == 2:
        print(bcolors.FAIL + bcolors.BOLD + "You Quit!" + bcolors.ENDC)
        break

    enemy_choice = 1

    if enemy_choice == 1:
        print(bcolors.ATTACKCHOSEN + bcolors.BOLD + "Enemy chose Melee Attack!", str(index) + bcolors.ENDC)
        dmg = enemy.generate_damage()
        player.take_damage(dmg)
        print(bcolors.ATTACKGIVETAKE + bcolors.BOLD + "You were attacked for", str(dmg), "damage!",
              "Your HP reduced to",
              str(player.get_hp()) + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + bcolors.BOLD + "You Won!!" + bcolors.ENDC)
        break
    elif player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD + "You Lost!!" + bcolors.ENDC)
        break
