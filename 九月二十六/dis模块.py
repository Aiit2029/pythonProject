import dis


def func():
    a = []
    a.append(2)
    b = 3
    a.append(b)



dis.dis(func)