# lambda1 = lambda a: print((a[0],a[2]))
# lambda1('son')

lambda1 = lambda a,b: a if a > b else b
print(lambda1(20, 21))