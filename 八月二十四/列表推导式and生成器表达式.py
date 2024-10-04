# list = []
# for i  in range(1,100):
#     list.append(i)
# print(list)
# lsit1 = [i**2 for i in range(1,11) if i%2 ==0]
# print(lsit1)
# list2 = [f'python{i}' for i in range(1,101)]
# print(list2)

# lst1 = ['jay', 'zhangsan', 'lisi']
# lst2 = ['1','2','3','4']
#
# dic = {lst2[i]:lst1[i] for i in range(len(lst1))}
# print(dic)

# s = {i for i in range(1,200)}
# print(type(s))
# print(s)
# print(s)

s = '''
for i in range(1,11):
    print(i)
'''
exec(s)