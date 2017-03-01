class Animal:
	def __init__(self): # создаем метод-конструктор
		self.can_run = False # передаем два стандартных атрибута
		self.can_fly = False 

	def print_abilities(self):
		print(type(self).__name__ + ":") # выводим имя класса от которого наследуется данный экземпляр
		print("Can run: ", self.can_run)
		print("Can fly: ", self.can_fly)
		print()



class Hourse(Animal):
	def __init__(self):
		super().__init__() # вызываем метод суперкласса
		self.can_run = True # переопределяем атрибут суперкласса для данного экземпляра


class Bird(Animal):
	def __init__(self):
		super().__init__()
		self.can_fly = True


class Pegas(Hourse, Bird):
	pass
	# т.к этот класс наследуется от 2х предыдущих, то результатом будут унаследованные результаты
	# Hourse: can_fly = False, can_run = True
	# Bird: can_fly = True, can_run = False
	# Pegas: can_fly = True, cam_run = True


if __name__ == "__main__":
	hourse = Hourse()
	bird = Bird()
	pegas = Pegas()

	hourse.print_abilities()
	bird.print_abilities()
	pegas.print_abilities()
		
		