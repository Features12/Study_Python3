class MyObject:
    attr = 8

    def __init__(self):
        self.attr2 = 42

    def print_info(self):
        print(self.attr2)

    @staticmethod
    def static_meth():
        print(MyObject.attr)

if __name__ == "__main__":
    MyObject.static_meth()
    a = MyObject()
    a.print_info()
    a.static_meth()