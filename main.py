from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 7, "dmg": 50},
         {"name": "Thunder", "cost": 10, "dmg": 60},
         {"name": "Blizzard", "cost": 15, "dmg": 70}]

player = Person(460, 45, 20, 34, magic)
enemy = Person(1200, 20, 10, 7, magic)

run = True
i = 0

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

while run:
    print("======================================")
    player.choose_action()
    choice = input(bcolors.BOLD + "Choose your attack type: " + bcolors.ENDC)

    index = int(choice) - 1

    if index == 0:
        print(bcolors.ATTACKCHOSEN + bcolors.BOLD + "You chose Melee Attack!", str(index) + bcolors.ENDC)
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print(bcolors.ATTACKGIVETAKE + bcolors.BOLD + "You attacked for", str(dmg), "damage!", "Enemy HP reduced to",
              str(enemy.get_hp()) + bcolors.ENDC)

    elif index == 1:
        print(bcolors.ATTACKCHOSEN + bcolors.BOLD + "You chose Magic Attack!", str(index) + bcolors.ENDC)

    else:
        print(bcolors.FAIL + bcolors.BOLD + "No such attack exists!" + bcolors.ENDC)

    enemy_choice = 1

    if enemy_choice == 1:
        print(bcolors.ATTACKCHOSEN + bcolors.BOLD + "Enemy chose Melee Attack!", str(index) + bcolors.ENDC)
        dmg = enemy.generate_damage()
        player.take_damage(dmg)
        print(bcolors.ATTACKGIVETAKE + bcolors.BOLD + "You were attacked for", str(dmg), "damage!", "Your HP reduced to",
              str(player.get_hp()) + bcolors.ENDC)
