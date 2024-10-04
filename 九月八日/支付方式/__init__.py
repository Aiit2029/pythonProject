#  约束力强，依赖abc模块
from abc import ABCMeta, abstractmethod


class Software(metaclass=ABCMeta):
    def __init__(self, username):
        self.username = username

    @abstractmethod
    def pay(self, money):
        raise ValueError('请重写一个同名pay方法')


class Wechat(Software):
    def __init__(self, username):
        super().__init__(username)
        self.softname = '微信'

    def pay(self, money):
        dic = {'username': self.username, 'money': money}
        print(f'{self.username}使用{self.softname}支付了{money}元')


class Alipay(Software):
    def __init__(self, username):
        super().__init__(username)
        self.softname = '支付宝'

    def pay(self, money):
        dic = {'uname': self.username, 'price': money}
        print(f'{self.username}使用{self.softname}支付了{money}元')


class ApplePay(Software):
    def __init__(self, username):
        super().__init__(username)
        self.softname = '苹果'

    def pay(self, money):
        dic = {'name': self.username, 'num': money}
        print(f'{self.username}使用{self.softname}支付了{money}元')


def payment(username, money, software):
    if hasattr(software, 'pay'):
        ret = getattr(software, 'pay')
        obj = software(username)
        obj.pay(money)
    else:
        print('没有这个方法')


payment('Alipay', 100, Wechat)
payment('aelx', 200, Alipay)
payment('tom', 300, ApplePay)
