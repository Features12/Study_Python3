def factory(aClass, *args):
	return aClass(*args)


class Spam:
	def doit(self, message):
		print(message)


class Person:
	def __init__(self, name, job):
		self.name = name
		self.job = job


obj1 = factory(Spam) # Spam()
obj2 = factory(Person, "Guido", "Dev") # Person(name, job) __init__(self, name, job)


obj1.doit("Hello")
print(obj2.name, obj2.job)
