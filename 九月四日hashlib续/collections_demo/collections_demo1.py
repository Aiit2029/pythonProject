'''
collections模块

namedtuple():命名元组
可以使用属性的方式引用元组内的元素

defaultdict(): 默认值字典  如果你取的字典内取到了 字典内没有的键 。会返回一个默认值

Counter():  计数器

'''

from collections import namedtuple,defaultdict,Counter
# rectangle = namedtuple('Rectangle_class',('width','height'))
#
# r = rectangle(10,5)
# print(r.height)
# print(r.width)
# print(r[0])

#  什么是defaultdict

# dict1 = defaultdict(int,name = 'andy',age = 10)
# dict1['addr']
# print(dict1)
#
# def f():
#     return '上邪'
#
# dict2 = defaultdict(f,name ='andy')
# dict2['age']
# print(dict2)


# Counter  计数器
#
# c = Counter('abjalsdjhqlkhndlqhelqjhne')
#
# print(c)#Counter({'l': 4, 'h': 4, 'j': 3, 'q': 3, 'a': 2, 'd': 2, 'n': 2, 'e': 2, 'b'
#
# print(c.most_common(3))  # 前三个最多的  [('l', 4), ('h', 4), ('j', 3)]
