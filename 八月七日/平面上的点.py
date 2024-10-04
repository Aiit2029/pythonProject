class points():
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

    def movemove(self,m,n):
        x,y = self.x,self.y
        x,y = x + m,y + n
        if m > 0 and n > 0:
            print(f'x向右移动了{m}个单位，y向上移动了{n}个单位')
        if m < 0 and n < 0:
            print(f'x向左移动了{m}个单位，y向下移动了{n}个单位')
        if m > 0 and n < 0:
            print(f'x向右移动了{m}个单位，y向下移动了{n}个单位')
        if m < 0 and n > 0:
            print(f'x向左移动了{m}个单位，y向上移动了{n}个单位')

    # def distance(self):





p1 = points()
p2 = points()
p1.movemove(1,1)