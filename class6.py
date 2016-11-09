class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, self.age)


inna = Person("Inna", 20)
inna.print_info()
luci = Person("Luci", 26)
luci.print_info()

