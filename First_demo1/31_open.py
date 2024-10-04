f = open('first.txt', 'r')
# lines = f.readlines()
# for line in lines:
#         print(line)
lines = f.readlines()
for line in lines:
    if len(line) >12:
        print(line)
    else:
        print('太短了懒得写\n')

f.close()