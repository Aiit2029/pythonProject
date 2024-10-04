import re

list1 = ['猴一','猴二','猴萨满','猴悟空','侯大生','敖丙']

for i in range(len(list1)-1,-1,-1):
    if re.match(r'猴[\u4e00-\u9fff]+',list1[i]):
        del list1[i]
print(list1)