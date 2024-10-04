dict1 = {}
list1 = ['name','age','gender','height','weight']
value1  = ['liuzheng', 18 ,'男' ,178 ,168]


for i in range(len(value1)):
    dict1[list1[i]] = value1[i]

# dict1 = dict(zip(list1,value1))
print(dict1)