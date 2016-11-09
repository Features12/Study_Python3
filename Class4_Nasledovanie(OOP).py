class Person:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(self.name)

class Student(Person):
    def __init__(self, gr, name):
        Person.__init__(self,name)
        self.group = gr

    def print_info(self):
        print("Name is: ",self.name, "\nGroup is: ",self.group)


Inna = Student("P - 41","Inna")
Inna.print_info()