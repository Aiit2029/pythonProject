# l1 = [11,22,33,44,55,66]
#
# l2 = iter(l1)
# print(l2)
# for i in range(0,len(l1)):
#     print(next(l2))

#

# def func():
#     print(111)
#     print(222)
#     yield 3
# ret = func()
# print(next(ret))

def func():
    lst1 = ['老冰柜','weilong','latiao']
    lst2 = [1,2,3,4,5,6,7,8,9,10]
    yield from lst1
    yield from lst2

g = func()
while 1:
    x = input('>>>')
    try:
        if x == '1':
            print(next(g))
    except StopIteration:
        break