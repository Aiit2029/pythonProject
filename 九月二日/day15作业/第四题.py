# 给l1 = [1,1,2,2,3,3,6,6,5,5,2,2]去重，不能使用set集合（面试题）

l1 = [1,1,2,2,3,3,6,6,5,5,2,2]

l2 = []
for i in range(len(l1)):
    if l1[i] not in l2:
        l2.append(l1[i])
print(l2)



