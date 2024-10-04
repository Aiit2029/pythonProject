#
import sys
# print(sys.argv)
# old_str = sys.argv[1]
# new_str = sys.argv[2]
# filename = sys.argv[3]
#
#
#
# with open("file_new_name", 'w+') as f1:
#     with open(filename, 'w+') as f:
#         for line in f:
#             if old_str in line:
#                 new_line = line.replace(old_str, new_str)
#             else:
#                 new_line = line
#             f.write(new_line)
import sys

old_str = sys.argv[1]
new_str = sys.argv[2]
filename = sys.argv[3]
list1 = []
# 打开新文件用于写入

with open(filename, 'r+') as f:
    for line in f:
        if old_str in line:
            new_line = line.replace(old_str, new_str)
        else:
            new_line = line
        # 将处理后的行写入新文件
        list1.append(new_line)
    f.seek(0)
    f.truncate()
    for line in list1:
        f.write(line)

