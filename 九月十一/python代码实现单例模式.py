
class Baby():
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Baby, cls).__new__(cls)
        return cls.__instance

    def __init__(self,clothes,pants):
        self.clothes = clothes
        self.pants = pants


b1 = Baby('123','123')
b2 = Baby('123','434')
print(b1)
print(b2)

