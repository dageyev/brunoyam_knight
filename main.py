# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from random import randint


class Hero:

    def __init__(self):
        self.hp = 100
        self.maxhp = 100
        self.attack = 5
        self.defense = 1
        self.level = 1
        self.alive = True

    def levelup(self):
        self.maxhp += 20
        self.hp = self.maxhp
        self.attack += 1
        self.defense += 1
        self.level += 1

    def get_damage(self, amount):
        dmg = max(amount - self.defense, 0)
        self.hp -= dmg
        print(f'You lose {dmg} hp!')

    def hit(self):
        return max(randint(self.attack-2, self.attack+2), 1)


class Monster:

    def __init__(self):
        self.hp = 25
        self.maxhp = 25
        self.attack = 4
        self.defense = 0
        self.level = 1
        self.alive = True
        self.name = 'Skeleton'

    def get_damage(self, amount):
        dmg = max(amount - self.defense, 0)
        self.hp -= dmg
        print(f'{self.name} loses {dmg} hp!')
        if self.hp <= 0:
            print(f'{self.name} dies!')
            self.alive = False

    def hit(self):
        return max(randint(self.attack-2, self.attack+2), 1)

def main_loop():
    monsters = []
    for i in range(3):
        monsters.append(Monster())
    hero = Hero()
    while monsters and hero.alive:
        choices = f'Your hp is {hero.hp}/{hero.maxhp}.\nYou can attack:\n'
        for i in range(len(monsters)):
            m = monsters[i]
            choices += f'{i}. {m.name} ({m.hp}/{m.maxhp} hp)\n'
        num = int(input(choices))
        monsters[num].get_damage(hero.hit())
        monsters = [i for i in monsters if i.alive]
        for i in monsters:
            hero.get_damage(i.hit())
            if hero.hp <= 0:
                hero.alive = False
                print('You died!')
                break
    if hero.alive:
        print('You won!')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_loop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
