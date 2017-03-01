class Hourse:
	def run(self):
		print("I'm runnig")


class Bird:
	def fly(self):
		print("I'm flying")


class Pegas(Hourse, Bird):
	pass


def main():
	pegasus = Pegas()
	pegasus.run()
	pegasus.fly()



if __name__ == "__main__":
	main()