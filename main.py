import sys

from player import Player
import fight

print('Enter your player name:')
playerName = input()
print('Hi ' + playerName + '!')
player = Player(playerName)

while True:
    print('Choose an action : ')
    print('Tape 1 for start a fight')
    print('Tape 2 for show your player stats')
    print('Tape 3 for leave the game')
    action = input()
    if action == '':
        continue

    if int(action) == 1:
        player = fight.start_fight(player)
        continue

    if int(action) == 2:
        player.show_stats()

    if int(action) == 3:
        print(' --- End game ---')
        print()
        print('Bye !')
        sys.exit()

    print(' --- Press enter to continue ---')
    input()
