# li = ["alex","Wusir","ritian","barry","wenzhou"]
#
# print(len(li))
# li.append("seven")
# print(li)
# li.insert(1, "Tony")
# print(li)
# li[1] = "Kelly"
# print(li)
# l2 = [1,'a',3,4,"heart"]
# li.extend(l2)
# print(li)
# li.remove("ritian")
# print(li)
# li.pop(1)
# print(li)
# del li[1:4]
# print(li)
#
# s = "qwert"
#
# li.extend(s)
# print(li)
#
# li = [1, 3, 2, "a", 4, "b", 5,"c",["a","b","cc"]]
#
# l1 = li[0:3]
# print(l1)

# lis = [2, 33, "k", ["qwe", 20, ["k1", ["tt", 3, "1"]], 89], "ab", "adv"]
#
# # lis[3][2][1][0] = lis[3][2][1][0].upper()
# # print(lis)
# lis[3][2][1][0].replace("t", "T")
# print(lis)
# li = ["alex", "wusir", "taibai","",1]
# strli = "_".join(str(x) for x in li)
# print(strli)
# strli = ""
# for i,v in enumerate(li):
#     if i ==0:
#         strli = strli + str(v)
#     else:
#         strli = strli + "_" + str(v)
# print(strli)



# def func(li):
#     if type(li) == list:
#         for i in li:
#             if type(i) == list:
#                 func(i)
#             else:
#                 print(str(i).lower())
#
#
# if __name__ == '__main__':
#
#     li = [1, 3, 4, "alex", [3, 7, 8, "TaiBai"], 5, "RiTiAn"]
#     func(li)


def func(max_num):
    a,b = 0,1
    fib_list = []

    if max_num >=0:
        fib_list.append(a)
    if max_num ==0:
        return fib_list

    if max_num >=1:
        fib_list.append(b)

    while True:
        c = a + b
        if c > max_num:
            return fib_list
        fib_list.append(c)
        a , b=  b , c
    return fib_list


if __name__ == '__main__':

    x = int(input("请输入一个数字："))
    print(func(x))


