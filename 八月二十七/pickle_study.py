# l1 = [1,2,3,{"name":"alex"}]
# import pickle
# st = pickle.dumps(l1)
# print(type(st))
# print(st)
#
# l2 = pickle.loads(st)
# print(type(l2))
# print(l2)

import pickle

def func():
    print('hello')

# f = open('pick对pickle',mode = 'wb')
# pickle.dump(func,f)
# f.close()

f = open('pick对pickle',mode = 'rb')
ret = pickle.load(f)
print(ret, type(ret))
ret()
