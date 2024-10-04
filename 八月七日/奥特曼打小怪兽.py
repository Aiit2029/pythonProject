import random
from abc import ABCMeta, abstractmethod


class fighter(object, metaclass=ABCMeta):
    def __init__(self,name,hp):
        self._name = name
        self._hp = hp
        # self._mp = mp

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name = name
    @property
    def hp(self):
        return self._hp
    @hp.setter
    def hp(self,hp):
        self._hp = hp
    # @property
    # def mp(self,mp):
    #     return self._mp
    # @mp.setter
    # def mp(self, mp):
    #     self._mp = mp

    @abstractmethod
    def attack_body(self,other):
        pass

    def end_skill(self):
        pass
    @property
    def alive(self):
        return self._hp > 0

class UltimateFighter(fighter):
    def __init__(self,name,hp,mp):
        super().__init__(name,hp)
        self._mp = mp

    def attack_body(self,other):
        self._hp  -= random.randint(15,25)
    def end_skill(self, other=None, ):
        if self._mp >= 50:
            self._mp -= 50
            injury -= other.hp * 3//4
            injury = injury if injury > 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack_body(other)
            return False

    def magic_attack(self,others):
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive :
                    temp.hp -= random.randint(15,25)

                return True
            else:
                return False

    def resume_magic(self):
        increase_point = random.randint(10,15)
        self._mp += increase_point
        return increase_point

    def __str__(self):
        print(f'~~~~~凹凸曼{self._name}还有{self._hp}生命值~~~{self._mp}法力值')


class Monster(fighter):
    def __init__(self,name,hp):
        super().__init__(name,hp)

    def attack_body(self,other):
        other._hp -= random.randint(1,10)

    def __str__(self):
        print(f'~~~~~小怪兽{self._name}还有{self._hp}生命值~~~')

    def monster_is_any_alive(monsters):
        for monster in monsters:
            if monster.alive > 0:
                return True
        return False

    def select_a_monster(monsters):
        monster_len = len(monsters)
        while True:
            index = random.ramdrange(monster_len)
            monster =  monsters[index]
            if monster.alive > 0:
                return monster
     