# print(divmod(10, 3))  # 10除3 的结果， 商3余1
#
# print(round(3.1415926,2))#保留两位小数
#
# print(pow(2,3))  ## 2的三次方、
#
# print(pow(2,3,3)) #二的三次方对3取余
#
# s1 = '太白'
#
# b = s1.encode('utf-8')
# print(b)
#
# n = bytes(s1,encoding='utf-8')
# print(n)
#
# s = ord('刘')
# d = ord('政')
# print(s)
# print(d)
#
# s3 = chr(22421)  # 输入位置数字，找出其对应的字符
# print(s3)
#
#

# s1 = '2014'
# print(s1)
# print(repr(s1))
#
# l1 = [('太白',18),('alex',73),('wusir',35),('无挑五',41)]
#
# print(min(l1,key=lambda x: x[1] ))
#
# l1 = [2,3,4,5,6,7,1]
# ret = filter(lambda x: x > 2, l1)
# # for i in ret:
# #     print(i)
# print(list(ret))

#列表推导式返回的是列表，filter返回的是一个迭代器

#map    列表推导式的循环模式
print([i**2 for i in range (1,6)])
ret = map(lambda x: x ** 2, range(1, 6))
print(ret)
print(list(ret))


