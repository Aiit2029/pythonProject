import re
string = "aapaple,banana,1a23,chearry"
result = re.split("[a]", string)
print(result)
for i in result:
    print(i)
