# property   把一个方法伪装成一个属性来调用
#  property 修饰的方法不能有参数

# property 第二个应用场景， 和私有的属性合作

#
# self.__pwd = pwd
#
# def pwd(self):
#     pass
#
#  假装为属性，只能查看不能修改


class Goods:
    discount = 0.8

    def __init__(self, name, origin_price):
        self.name = name
        self.__price = origin_price

    @property
    def display_price(self):
        return self.__price * Goods.discount

    @display_price.setter
    def display_price(self, price):
        if isinstance(price,int):
            self.__price = price


g = Goods('apple',6)

print(g.display_price)
g.display_price = 10
print(g.display_price)
