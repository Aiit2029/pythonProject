# 用map来处理字符串列表,把列表中所有人都变成sb,比方alex_sb
# l=[{'name':'alex'},{'name':'y'}]
# # for i in l:
# #      for x in i.keys():
# #          i[x] = f'{i[x]}_sb'
# # print(l)
# ret = map(lambda item:{k:f'{v}_sb' for k,v in item.items()},l)
# print(list(ret))

# 用filter来处理,得到股票价格大于20的股票名字
# shares={
#  'IBM':36.6,
#  'Lenovo':23.2,
#  'oldboy':21.2,
#  'ocean':10.2,
#          }
# for x in shares:
#     print(x)
# ret = filter(lambda x:shares[x]>20, shares)
# print(list(ret))

# 有下面字典，得到购买每只股票的总价格，并放在一个迭代器中。
# portfolio = [
#   {'name': 'IBM', 'shares': 100, 'price': 91.1},
#     {'name': 'AAPL', 'shares': 50, 'price': 543.22},
#     {'name': 'FB', 'shares': 200, 'price': 21.09},
#     {'name': 'HPQ', 'shares': 35, 'price': 31.75},
#     {'name': 'YHOO', 'shares': 45, 'price': 16.35},
# {'name': 'ACME', 'shares': 75, 'price': 115.65}]

# lst1 = []
# for i in portfolio:
#    ret = i['shares']*i['price']
#    lst1.append(ret)
# print(lst1)
# ret = (i['shares']*i['price'] for i in portfolio)
# print(list(ret))
# ret = filter(lambda x:x['price']>100,portfolio)
# print(list(ret))

# 写代码，最终得到的是（每个元祖第一个元素>2,第三个*至少是4个。）
# l1 = [1, 2, 3, 4, 5, 6]
# l2 = ['oldboy', 'alex', 'wusir', '太白', '日天']
# tu = ('**', '***', '****', '*******')

# ret = [zip((x for x in l1 if x > 2 ) ,(y for y in l2) ,(z for z in tu if len(z) >= 4)) ]
# print(list(ret))
# print(ret)

# ret = filter(lambda x:x[0]>2 and len(x[2]) >= 4, zip(l1, l2, tu))
# print(list(ret))
#
# l1 = [ {'sales_volumn': 0},
#        {'sales_volumn': 108},
#        {'sales_volumn': 337},
#        {'sales_volumn': 475},
#        {'sales_volumn': 396},
#        {'sales_volumn': 172},
#        {'sales_volumn': 9},
#        {'sales_volumn': 58},
#        {'sales_volumn': 272},
#        {'sales_volumn': 456},
#        {'sales_volumn': 440},
#        {'sales_volumn': 239}]
# # 将l1按照列表中的每个字典的values大小进行排序，形成一个新的列表。
# l2 = sorted(l1, key=lambda x:x['sales_volumn'])
# print(l2)

# .有如下列表,按照元素的长度进行升序
#
# lst = ['天龙八部','西游记','红楼梦','三国演义']
#
# lst1 = sorted(lst,key=lambda x:len(x))
# print(lst1)


# 看代码，叙说 reverse 和  reversed 的区别

# lst = [1,2,3,5,9,12,4]
# lst.reverse()
# print(lst)
#
# print(list(reversed(lst)))
# reverse会对原有列表进行修改，反转列表中元素的顺序


# 而reversed  不会对原有的列表进行修改，而是生成一个迭代器对象，
# 其中包含着反转顺序以后的元素

#
# # .有如下数据,按照元素的年龄进行升序
# lst = [{'id':1,'name':'alex','age':18},
#     {'id':2,'name':'wusir','age':17},
#     {'id':3,'name':'taibai','age':16},]
# lst.reverse('age')
# print(lst)
# lst2 = reversed(lst,key=lambda x:x['age'])
# print(lst2)
# lst.sort(key=lambda x:x['age'])
# print(lst)
# lst2 = sorted(lst,key=lambda x:x['age'])
# print(lst2)

# v = [lambda: x for x in range(10)]
# # print(v[0])
# # # print(v[0]())
# # print((v[2]()))
# k = (lambda: x for x in range(10))
# print(k)
# print(next(k))
# print(next(k)())

# ret = map(str,[1,2,3,4,5,6,7,8,9])
# # 输出是什么? (面试题)
# print(list(ret))


#
# def num():
#   def create_function(i):
#     # 使用局部变量来保存当前的 i 值
#     current_i = i
#
#     def multiplier(x):
#       return current_i * x
#
#     return multiplier
#
#   result = []
#   for i in range(4):
#     result.append(create_function(i))
#   return result
#
#
# print([m(2) for m in num()])