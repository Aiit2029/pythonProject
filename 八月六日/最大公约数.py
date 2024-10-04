

x = int(input())
y = int(input())
# set1 = set()
list1 = []
# 一个数能被另一个数整除
for i in range(1,x + y):
    if x % i == 0 and y % i == 0:
        list1.append(i)
        list1.sort()
print(list1)
print(list1[-1])



#      wrong
# for i in range(1,x + y):
#     if x % i ==0:
#         set1.add(i)
#     if y % i == 0:
#         set1.add(i)
# print(set1)
# print(max(list(set1)))

