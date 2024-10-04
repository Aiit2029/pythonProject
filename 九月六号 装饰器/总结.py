##  递归练习
    # 遍历文件下的所有文件
    # 二分查找   [1,2,3,4,5,6,7,12,34,45,67,78]





# def divide_find(lst):
#     x = int(input('>>>'))
#     while True:
#         if len(lst) %2 ==0:
#             if lst[len(lst)/2-1] == x or:
#
#
#         elif len(lst) %2 ==1:
#             if lst[len(math.ceil(len(lst)/2))] == x:
#                 return True
#             elif lst[len(math.ceil(len(lst)/2))] > x:
#                 lst = lst[0:math.ceil(len(lst)/2)-1]
#                 return lst
#             elif lst[len(math.ceil(len(lst)/2))] < x:
#                 lst = lst[math.ceil(len(lst)/2):]
#                 return lst
#             divide_find(lst)
#
# def divide_find(lst,x):
#     while True:
#         if lst[len(lst)//2] == x:
#             print('True')
#             return True
#         elif lst[len(lst)//2] > x:
#             lst = lst[:len(lst)//2]
#             print('在里面，再来一次')
#         elif lst[len(lst)//2] < x:
#             lst = lst[len(lst)//2+1:]
#             print('在外面,在来一次')
#         ret = divide_find(lst,x)
#         print('递归')
#         if ret == True : exit()
#
#
#
# def main():
#     list = [1, 2, 3, 4, 5, 6, 7, 12, 34, 45, 67, 78]
#     x = int(input('>>>'))
#     divide_find(list,x)
#
# if __name__ == '__main__':
#     main()
import  shutil

