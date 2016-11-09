class Person:
    city = "Gomel"
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(self.name)


class Student(Person):
    def __init__(self, group, name):
        self.group = group
        Person.__init__(self, name)

    def print_info_student(self):
        print(self.group, self.name)


inna = Student("P -41", "Inna")
inna.print_info_student()

