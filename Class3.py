class Counter:
    """Replacement attributes class"""
    count = 0
    def __init__(self):
        self.__class__.count += 1


print(Counter.__doc__)
print("Call attributes with class: {}".format(Counter.count))
a = Counter()
print("Call attributes 'a' with init: {}".format(a.count))
b = Counter()
print("Call attributes 'b' with init: {}".format(b.count))

