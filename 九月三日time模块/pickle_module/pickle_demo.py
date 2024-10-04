'''
pickle:
将python中的所有数据类型转换成字节串，序列化过程
将字节串转换成python中的数据类型，反序列化过程
'''

'''
1、 pickle.dumps

2、 pickle.dump

3、 pickle.load

4、 pickle.loads
'''

import pickle

# bys  = pickle.dumps([1,2,3])
# print(type(bys))
# print(bys)

# bys = pickle.dumps((1,2,3))
# print(bys)
#  其返回的仍然是一个元组  这是json中所不能实现的
# res = pickle.loads(bys)
# print(res)
# print(type(res))

#  尝试set集合

# bys = pickle.dumps({1,45,3,23})
# print(bys)
# print(type(bys))
#
# res = pickle.loads(bys)
# print(type(res))
# print(res)

# with open('./pickle_file.txt', 'wb') as f:
#     pickle.dump([1,2,4],f)
# with open('./pickle_file.txt', 'rb') as f:
#     x = pickle.load(f)
#     print(type(x))
#     print(x)

# 多次pickle数据到同一个文件中
# with open('./pickle_file.txt', 'ab') as f:
#     pickle.dump([1, 2, 3], f)
#     pickle.dump([1, 2, 3], f)
#     pickle.dump([1, 2, 3], f)


# with open('./pickle_file.txt', 'rb') as f:
#     for x in range(4):
#         ret = pickle.load(f)
#     # ret = pickle.load(f)
#         print(ret)

# pickle 尽量还是一次写一次读  