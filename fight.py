from monster import Monster


def start_fight(player):
    monster = Monster(10, 2)
    print('--- Start fight ---')
    monster.show_stats()

    while True:
        print('Choose an action : ')
        print('Tape 1 for attack')
        print('Tape 2 for show the monster stats')
        print('Tape 3 for leave the fight')
        action = input()
        if action == '':
            continue

        if int(action) == 1:
            player.attack_monster(monster)
            print('BIM !!!')
            monster.show_stats()
            print(' --- Press enter to continue ---')
            input()

        if int(action) == 2:
            monster.show_stats()

        if int(action) == 3:
            print('Your leave the fight')
            break

        if monster.life == 0:
            print("YOU WIN !!!")
            break

    return player
