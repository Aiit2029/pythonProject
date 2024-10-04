class Soldier(object):
    def __init__(self):
        self.name = '许三多'
        self.gun = Gun('Ak47')

    def fire(self):
        self.gun.shoot()
        print('~~~tututu~~~')


class Gun(object):
    def __init__(self, model):
        self.model = model
        self.bullet_count = 10

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        while self.bullet_count > 0:
            print("~~~piapiapia~~~")
            self.bullet_count -= 1
            if self.bullet_count == 0:
                print("~~~换弹啦~~~")
                self.add_bullet(30)
            continue





soldier = Soldier()
print(soldier.gun.model)
soldier.fire()

