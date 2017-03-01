class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def giveRaise(self, percent):
        self.salary = self.salary + (self.salary * percent)

    def work(self):
        print(self.name, "I work")

    def __repr__(self):
        return object.__class__.__name__,"{}, {}".format(self.name, self.salary)


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
    print(Bob) # Employee.__repr__(name, salary)

    print()

    Anna = Chef("Anna")
    Anna.work()
    print(Anna)

    print()

    Cris = Server("Cris")
    Cris.work()
    print(Cris)

    print()

    MrRobot = PizzaBot("MrRobot")
    MrRobot.work()
    print(MrRobot)




if __name__ == "__main__":
    main()


