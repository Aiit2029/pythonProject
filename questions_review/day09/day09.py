# def check_element(obj):
#     if not isinstance(obj,(list,tuple)):
#         raise TypeError("The function only accepts dictionaries as input.")
#     return [obj[i] for i in range(1,len(obj),2)]
#
#
# if __name__ == '__main__':
#     lst = [1,2,3,4,5,6,7,8,9,10]
#     print(check_element(lst))
# new_lst = []
# for i in range(len(lst)):
#     if i % 2 == 0:
#         continue
#     else:
#         new_lst.append(lst[i])
# return new_lst

# def check_element_len(obj):
#     if not isinstance(obj,(list,tuple,str)):
#         raise TypeError("The function only accepts dictionaries as input.")
#     return len(obj) > 5

# def compare_elements(obj1, obj2):
#     if not isinstance(obj1,obj2,(int,float)):
#         raise TypeError("The function only accepts dictionaries as input.")
#     # if obj1 > obj2:
#     #     return obj1
#     # else:
#     #     return obj2
#     return obj1 if obj1 > obj2 else obj2
#


# def check_element(obj):
#     if not isinstance(obj,(dict)):
#         raise TypeError("The function only accepts dictionaries as input.")
#     for key,value in obj.items():
#         if not isinstance(value,(str,list)):
#             raise TypeError("The function only accepts dictionaries as input.")
#         if len(value) > 2:
#             value = value[:2]
#             obj[key] = value
#     return obj
#
#
# if __name__ == '__main__':
#     dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
#     print(check_element(dic))

# def recive_numbers(numbers):
#     sum = 0
#     numbers = numbers.split(" ")
#     numbers = [int(i) for i in numbers]
#     for i in numbers:
#         sum += i
#     return sum
#
#
# if __name__ == '__main__':
#     numbers = input("请输入n个数字，用空格分隔：").strip()
#     print(recive_numbers(numbers))

# a = 10
# b = 20
#
#
# def test5(a, b):
#     print(a, b)
#
#
# c = test5(b, a)
# print(c)

# a = 2
# def wrapper():
#
#     print(a)
# wrapper()
# def wrapper():
#     a = 1
#
#     def inner():
#         print(a)
#
#     inner()
#
#
# wrapper()


def wrapper():
    a = 1

    def inner(a):
        a += 1
        print(a)

    inner(a)


wrapper()