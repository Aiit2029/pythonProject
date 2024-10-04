#  只有字符串类型可以和bytes可以互换
# dict,list ..... >>>str  <......>  bytes
# 数据存储在文件中 str（bytes形式存储）
# 将数据结构转化成特殊的字符串，并且可以反转回 数据结构
# 两对 四种方法

#第一对 dumps loads
#第二对 dump load  只能写入文件，只能写入一个数据结构

import json

# dic  = {'username':'太白', 'password':123,'status':True}
# # dumps loads
# st = json.dumps(dic,ensure_ascii=False)
# print(type(st))
# print(st)
#
# #
# dic1 = json.loads(st)
# print(type(dic1),dic1)

# l1 = [1,2,3,{'username':'太白', 'password':123}]
# with open('test.json','w',encoding='utf-8') as f1:
#     st1 = json.dumps(l1,ensure_ascii=False)
#     # st1 = json.dumps(l1)
#     f1.write(st1)


# with open('test.json','r+',encoding='utf-8') as f2:
#     st = f2.read()
#     print(st)
#     print(type(st))
#     l1 = json.loads(st)
#     print(type(l1))


# dump写入文件
# l1 = [1,23,3]
# with open('json1.json','w+',encoding='utf-8') as f1:
#     json.dump(l1,f1,ensure_ascii=False)

# data = [1,2,3,'liu']
# #读取文件
# with open('json1.json','r',encoding='utf-8') as f2:
#     data = json.load(f2)
#     print(data,type(data))

dic1 = {'name':'liu'}
dic2 = {'name':'zhang'}
dic3 = {'name':'li'}
with open('dic.json', 'w',encoding='utf-8') as f:
    # json.dumps(dic1,ensure_ascii=False)
    # json.dumps(dic2,ensure_ascii=False)
    # json.dumps(dic3,ensure_ascii=False)
    f.write(json.dumps(dic1,ensure_ascii=False)+'\n')
    f.write(json.dumps(dic2, ensure_ascii=False)+'\n')
    f.write(json.dumps(dic3, ensure_ascii=False)+'\n')
