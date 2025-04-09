# users = ['大黑哥','龚明阳',666,'渣渣辉']
# str1 = "_".join(str(x) for x in users)
# print(str1)
#
# v1 = (11,22,33)
# v2 = [44,55,66]
# v2.extend(v1)
# print(v2)
# v2.append(v1)
# print(v2)
# v1 = (11,22,33,44,55,66,77,88,99)
# v2 = v1[0::2]
# print(v2)
# v2 = [v1[i] for i in range(len(v1)) if i % 2 == 0]
# print(v2)

key_list = []
value_list = []
info = {'k1':'v1','k2':'v2','k3':'v3'}
for k,v in info.items():
    key_list.append(k)
    value_list.append(v)
print(key_list)
print(value_list)
info["k4"] = "v4"
info.update(k5="v5")
info.update({"k6":"v6"})
print(info)