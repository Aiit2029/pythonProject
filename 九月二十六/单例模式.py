# class A:
#     __instance = None
#     def __new__(cls, *args, **kwargs):
#         if not cls.__instance:
#             cls.__instance = super(A, cls).__new__(cls)
#             return cls.__instance
import threading


class A:
    __instance = None
    lock = threading.Lock()
    def __new__(cls, *args, **kwargs):
        with cls.lock:
            if not cls.__instance:
                cls.__instance = super(A, cls).__new__(cls)
                return cls.__instance








