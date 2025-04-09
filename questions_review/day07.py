# v1 = [1,2,3,4,5]
# v2 = [v1,v1,v1]
# v1.append(6)
# print(v1)
# print(v2)


##  什么是浅拷贝和深拷贝
"""
深拷贝 是 重新开辟一个新的内存空间 ,将原对象的所有内容复制一份
浅拷贝 是重新开辟一个新的内存空间 将原对象第一层的内容复制一份 ,如果有第二层 将第二层引用过来
赋值 ,如果修改任意可变对象 都会影响所有的引用 而不可变对象因为不可修改所以都会重新开辟一块内存空间 将值付给他


"""
#
#
# v1 = [1,2,3,4,5]
# v2 = [v1,v1,v1]
# v2[1][0] = 111
# v2[2][0] = 222
# print(v1)
# # print(v2)
# v1 = [1,2,3,4,5,6,7,8,9]
# v2 = {}
# for item in v1:
#     if item < 6:
#         continue
#     if 'k1' in v2:
#         v2['k1'].append(item)
#     else:
#         v2['k1'] = [item ]
# print(v2)
# import copy
# v1 = "alex"
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
# print(v1 is v2)
# print(v1 is v3)
# import copy
# v1 = [1,2,3,4,5]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
# print(v1 is v2)
# print(v1 is v3)

# import copy
# v1 = [1,2,3,4,5]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1[0] is v2[0])
# print(v1[0] is v3[0])
# print(v2[0] is v3[0])


# import copy
#
# v1 = [1,2,3,4,[11,22]]
# v2 = copy.copy(v1)
# v3 = copy.deepcopy(v1)
#
# print(v1[-1] is v2[-1])
# print(v1[-1] is v3[-1])
# print(v2[-1] is v3[-1])

#
#
# a = ("太白金星")
# b = (1,)
# c ={"name":"alex"}
#
# print(type(a))
# print(type(b))
# print(type(c))

# l1 = [1,3,6,7,9,8,5,4,2]
# l1.sort()
#
# # l1.sort(reverse=True)
# print(l1)
# l = []
# l1 = ['_',"_","_"]
# for item in range(3):
#     l.append(l1)
# print(l)


# l1 = [1,2,]
# # l1 += [3,4]
# # print(l1)
# print(type(l1))
# print(len(l1))

# dic = dict.fromkeys('abc',[])
# dic['a'].append(666)
# dic['b'].append(111)
# print(dic)


# l1 = [11,22,33,44,55]
# l1 = l1[::2]
# print(l1)

# dic = {'k1':'太白','k2':'barry','k3': '白白', 'age': 18}
# for key,val in dic.items():
#     if "k" in key:
#         key_list.append(key)
# for key in key_list:
#     del dic[key]
# print(dic)
# dic = {k:v for k,v in dic.items() if "k" not in k}
# print(dic)
#
# s1 = "太白金星"
# s1 = s1.encode("utf-8")
#
# print(s1)
# s1 = s1.decode("utf-8")
# print(s1)
# # s1 = s1.encode("gbk")
#
# ls5 = ["周老二","周老三","周老四","周老五","马星星"]
# ls5[:] = [k for k in ls5 if not k.startswith("周")]
# print(ls5)

cars = ['鲁A32444','鲁B12333','京B8989M','⿊C49678','⿊C46555','沪 B25041']
locals = {'沪':'上海', '⿊':'⿊⻰江', '鲁':'⼭东', '鄂':'湖北', '湘':'湖南'}
result = {}

for car in cars:
    province_short = car[0]
    if province_short in locals:
        province = locals[province_short]
        result[province] = result.get(province,0) + 1
print(result)










