"""
21.车牌区域划分, 现给出以下车牌. 根据车牌的信息, 分析出各省的车牌持有量. (选做题)
cars = ['鲁A32444','鲁B12333','京B8989M','⿊C49678','⿊C46555','沪 B25041']
locals = {'沪':'上海', '⿊':'⿊⻰江', '鲁':'⼭东', '鄂':'湖北', '湘':'湖南'}
结果: {'⿊⻰江':2, '⼭东': 2, '上海': 1}
"""

cars = ['鲁A32444','鲁B12333','京B8989M','⿊C49678','⿊C46555','沪 B25041']
locals = {'沪':'上海', '⿊':'⿊⻰江', '鲁':'⼭东', '鄂':'湖北', '湘':'湖南'}
dict1 = {}
# 1、cars中的字符串的首位有 == locals中的任意一个key的，locals的value所对应的值 +1
for key in locals.values():
    dict1[key] = 0

for i in range(len(cars)-1,-1,-1):
    if cars[i][0] in locals.keys():
        dict1[locals[cars[i][0]]] += 1
print(dict1)



# for count1 in locals.values():
#     print(count1)

# 2、如果cars中添加了一个  原来没有的 车牌照，例如，  湘  则在 结果的字典里添加  {湖南 ， 1}