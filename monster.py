class Monster:
    def __init__(self, life: int, attack: int) -> None:
        self.life = life
        self.attack = attack

    def is_alive(self) -> bool:
        if self.life == 0:
            return False
        return True

    def show_stats(self):
        print()
        print('Monster stats :')
        print('Life => ' + str(self.life))
        print('Attack => ' + str(self.attack))
        print()