# 递归函数最深 1000 层
# 为什么最深1000层
'''
  为了节省内存空间，不让用户无限的使用内存空间
  在js前端 是没有递归限制的
'''
# 循环和递归的关系
    # 如果一个问题可以使用递归也可以不使用递归实现
    # 那么这个问题 使用递归完成 没有不使用递归解决简单
    # 递归比循环更占用内存
    # 递归不是万能的
# 递归的深度是可以修改的
import sys
# sys.setrecursionlimit(10000000)
count = 0
s1 = 0
def func():
    global count
    global s1
    count += 1
    s1 += 1
    print(count)
    if count == 3:
        return 3
    print('这是之前的调用')
    func()
    print(f'这是之后的调用{s1}')

func()

# 递归函数必须要停下来
