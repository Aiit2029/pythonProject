tuple1 = (1,2,[3,4],{3},5,{'饿狼传说':'歌曲'},7,8,9)
# for i in tuple1:
#     print(i)
list1 = list(tuple1)
# list1.insert(2,[5])   在第三个位置增加一个【5】列表
list1[2].append(5)
print(list1)
print(type(tuple[3]))
print(tuple1)
