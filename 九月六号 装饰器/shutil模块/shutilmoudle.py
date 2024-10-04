import os
import shutil


# #  拷贝文件
# shutil.copy2('原文件名','现文件名')
#
# # 拷贝目录
# shutil.copytree('源目录','新目录')
# # 把源目录中的内容 全部copy到新的目录中
# shutil.copytree('源目录','新目录',ignore=shutil.ignore_patterns('目标文件'))
# # 把除了目标文件以外的 文件copy过来 ，可以是某个文件， 可以是某个文件类型  ，可以是多个文件
#
# # 删除目录
#
# shutil.rmtree('目标目录',ignore_errors=True)
# # ignore_errors = Ture忽略删除中发出现的错误
#
#
# # 移动目录
# shutil.move('目标现路径','目标要移动到的路径',copy_function=shutil.copy2)
# # copy_function  移动的方式
#
#
# # 获得当前磁盘的使用空间


# total,used, free = shutil.disk_usage('.')
# print(total,used,free)

# 压缩文件
shutil.make_archive('压缩后文件叫什么名字','压缩文件的格式','要压缩的文件的路径')

#解压文件
shutil.unpack_archive('要解压的目标文件名称')   #  默认解压到当前文件夹下

shutil.unpack_archive('要解压的目标文件名称','要解压到的目标文件夹路径')








