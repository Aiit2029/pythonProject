#  classmethod
# class Goods:
#     __discount = 0.8
#
#     def __init__(self):
#         self.__price = 5
#         self.price = self.__price * self.__discount
#
#     @classmethod
#     def change_discount(cls, new_discount):
#         cls.__discount = new_discount
#
#
# apple = Goods()
# print(apple.price)
# # apple.price = 8
# apple._apple__discount = 0.6
# print(apple.price)
import time
from datetime import datetime


class Date_demo():
    def __init__(self,year,month,day):
        self.year = year
        self.month=month
        self.day=day
    @classmethod
    def today(cls):
        # return datetime.date(self.year,self.month,self.day)
        return time.strftime("%Y-%m-%d",time.localtime())

date1 = Date_demo.today()
print(date1)