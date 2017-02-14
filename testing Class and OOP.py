class Person:
	def __init__(self, name, job = None, pay = 0):
		self.name = name
		self.job = job
		self.pay = pay

	def last_name(self):
		return(self.name.split()[-1])

	def up_pay(self, percent):
		self.pay = int(self.pay * (1 + percent))

	def __str__(self):
		return "Person: {} and {}".format(self.name, self.pay)
	# функция __repr__ == __str__ , но выводит в формате с обозначением типа данных:
		# __str __ : name = "Inna" --> Output: Inna
		# __repr__ : name = "Inna" --> Output: "Inna"
	# функция print() будет автоматически вызывать метод __str__


class Manager(Person):
	def __init__(self, name, pay):
		Person.__init__(self, name, "mrg", pay) # Переопределение конструктора. Вызов оригинального конструктора со стандартным значением "mrg" в аргументе job

	def up_pay(self, percent, bonus = .10):
		Person.up_pay(self, percent + bonus) # Вызов функции через родительский класс и перезадать нужные изменения


if __name__ == "__main__":
	bob = Person("Bob Smith")
	sue = Person("Sue Jones", job = "dev", pay = 100000)
	tom = Manager("Tom Jones", 50000)

"""	print(bob)
	print(sue)
	print(tom)
	print(bob.last_name(), "and" , sue.last_name(),"and",tom.last_name())
	sue.up_pay(.10)
	tom.up_pay(.10)
	print(sue)
	print(tom)
"""

	print("--All three--")
	for object in (bob, sue, tom):
		object.up_pay(.10)
		print(object)