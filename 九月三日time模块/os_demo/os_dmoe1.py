# '''
#
# os : 和操作系统相关的操作封装在这个模块中
#
# '''
# import os
# #  文件操作  重命名 ， 删除 等
#
# # 文件的删除
# # os.remove('a.txt')
#
# # 文件的重命名
# # os.rename('a.txt','d.txt')
#
# # 删除目录， 必须是空目录才能够删除
# # os.removedirs('path')
#
# # 如果想要删除有内容的目录  可以使用  shutil 模块
# #  也可以使用笨方法 ，使用递归， 进入目录的最低层
# #  ，一个个删除然后退出到 上一层目录然后继续删除 等
# # import shutil
# #
# # shutil.rmtree('path')
#
# # 和路径相关的内容被 封装到了  OS.path中
#
# # 获取路径名
# os.path.dirname('path')  #将 P 所在的地方 的父目录的名字提取出来
# #  不会判断路径内容是否存在
# # 只会返回这个路径的父目录部分提取
#
# # 获取文件名
# res = os.path.basename('path')
#
# # 将文件名和目录名 切分开
# res = os.path.split('path')
#
# # 拼接路径
#
# path_1 = os.path.join('d:\\','aaa','bbb')
# print(path_1)
# #
# #  如果是以 / 开头的路径  ，默认是在当前盘符 下
import os.path

res = os.path.abspath(r'/a/b/c')

print(res)
#  如果不是以 / 开头的路径,则是在当前文件 同级目录下
res_1 = os.path.abspath(r'a/b/c')
print(res_1)