# v1 = {'郭宝元','李杰','太白','梦鸽'}
# v2 = {'李杰','景女神'}
# print(v1 & v2)  # 交集
# print(v1 | v2)  # 并集
# print(v1 - v2)  # 差集
# print(v2 - v1)  # 差集
# print(v1 ^ v2)  ## 对称差集

# is 和 == 的区别
# is 判断内存地址是否一样
# == 判断值是否一样
'''
    is 判断两个对象的身份是否相同
    本质是判断两个对象的id是否相同
    is 是指针比较 时间复杂度为O(1)
    == 是值比较 可能出发__eq__方法 
    不可变类型的is 不一定为True
    因为只有小整数(-5-256)和短字符串(字母数字下划线)才会被缓存
    当超出范围或者含有特殊字符时 会重新开辟内存空间
    is 可能为 False
    ###
    is: 是不是同一个东西 (内存地址相同)
    ==: 是不是一样的东西 (值相同，不论是否是同一个)
    
'''

## 深浅拷贝
"""
    
"""
import copy
# v1 = [1,[2,5],3,4]
# v2 = v1.copy()
# v2[1] = 2
# print(v1)
# print(v2)
# v2[1][0] = 7
# print(v1)
# print(v2)

# a = 5
# b = a.copy()
# print(id(a))
# print(id(b))

# list2 = [1,2,3,4,5,[6,7,8]]
# list3 = copy.deepcopy(list2)
# print((list2[5] is list3[5]))
# list2[5][0] = 9
# print((list2[5][0] is list3[5][0]))
# print(list2)
# print(list3)


# v1 = {'k1':'v1','k2':[1,2,3]}
# v2 = {'k1':'v1','k2':[1,2,3]}
#
# result1 = v1 == v2
# result2 = v1 is v2
# print(result1)
# print(result2)

# v1 = {'k1':'v1','k2':[1,2,3]}
# v2 = v1
# v1['k1'] = 'wupeiqi'
# print(v2)

# info = [1,2,3]
# userinfo = {"account":info,"num":info,"money":info}
# info.append(9)
# print(userinfo)
# info = "题目怎么这么多"
# print(userinfo)

#
# info = [1,2,3]
# userinfo = [info,info,info]
# info[0] = "不仅多还难"
# print(info,userinfo)
#
# userinfo[2][0] = "闭嘴"
# print(info,userinfo)

# user_list = []
# for item in range(10):
#     user_list.append(info)
#
# info[1] = "???"
# print(user_list)


# data = {}
# for i in range(10):
#     data["user"] = i
# print(data)

# data_list = []
# data = {}
# for i in range(10):
#     data['user'] = i
#     data_list.append(data)
# print(data_list)
#
# data_list = []
# for i in range(10):
#     data = {}
#     data['user'] = i
#     data_list.append(data)
# print(data_list)