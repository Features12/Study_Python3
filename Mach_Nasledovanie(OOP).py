class First:
    def print_name(self):
        print("class1_First")

class Second:
    def print_name(self):
        print("class2_Second")

class Children(First, Second):
    def print_parents_name(self):
        self.print_name()


child = Children()
child.print_parents_name()
