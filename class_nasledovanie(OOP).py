class A:
    def print_hello(self):
        print("Hello")

class B(A):
    def print_world(self):
        print("World")

b = B()
b.print_hello()
b.print_world()
