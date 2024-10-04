import re


#
# re.match()
# re.serch()
# re.findall()
# re.finditer()

#
# ret = re.findall('[as]+','asdasdas12312313dasdsadsad200201123azsdjalsdhalih')
# print(ret)

#
# ret = re.findall(r'<h1>(.*?)</h1>', '<h1>1974ash93011ur</h1>')
# print(ret)

exp = '2-3*(5+6)'

print(re.findall(r'\d\+\d',exp))