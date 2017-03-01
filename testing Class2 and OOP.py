class Employee:
    def __init__(self, name, salary = 0):
        self.name = name
        self.salary = salary

    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(self.name, "I work")

    def print_class(self):
        return print("Class", type(self).__name__)

    def __repr__(self):
        return "name is: %s, salary: %s" % (self.name, self.salary)


class Chef(Employee):
    def __init__(self, name, salary = 50000):
        super().__init__(name, salary)
    def work(self):
        print(self.name, "I makes food")


class Server(Employee):
    def __init__(self, name, salary = 25000):
        super().__init__(name, salary)
    def work(self):
        print(self.name, "Interface for customer")


class PizzaBot(Chef):
    def __init__(self, name, salary = 15000):
        super().__init__(name, salary)
    def work(self):
        print(self.name, "Makes Pizza")


def main():
    Bob = Employee("Bob", 30000) # Employee.__init__(name, salary)
    Bob.giveRaise(0.20) # Employee.giveRaise()
    Bob.work() # Employee.work()
    Bob.print_class() # Employee.print_class()
    print(Bob) # Employee.__repr__(name, salary)

    print()

    Anna = Chef("Anna")
    Anna.work()
    Anna.print_class()
    print(Anna)

    print()

    Cris = Server("Cris")
    Cris.work()
    Cris.print_class()
    print(Cris)

    print()

    MrRobot = PizzaBot("MrRobot")
    MrRobot.work()
    MrRobot.print_class()
    print(MrRobot)

    """for klass in (Employee, Chef, Server, PizzaBot):
                    obj = klass(klass.__name__)
                    obj.work()"""




if __name__ == "__main__":
    main()


