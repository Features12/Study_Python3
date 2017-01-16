class Student():
    """Experience class"""
    city = "Gomel"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print("Name is: ",self.name)
        print("Age is: ", self.age)

Ivan = Student("Ivan", 23)
Fedor = Student("Fedor", 26)

print(Student.__doc__)
Ivan.print_info()
Fedor.print_info()
Student.city
