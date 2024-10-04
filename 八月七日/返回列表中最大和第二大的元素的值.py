def returnNum():

    list1 = [1,2,3,4,5,6,7,8,9]
    list1.sort()
    print(max(list1))
    templist = list1
    templist.sort()
    templist.pop(-1)
    print(max(templist))




returnNum()