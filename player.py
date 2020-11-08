from monster import Monster


class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.life = 10
        self.attack = 2

    def attack_monster(self, monster: Monster) -> Monster:
        monster.life = monster.life - self.attack

        if monster.life < 0:
            monster.life = 0

        return monster

    def show_stats(self):
        print()
        print(' --- Your player stats ---')
        print('Name => ' + str(self.name))
        print('Life => ' + str(self.life))
        print('Attack => ' + str(self.attack))
        print()
