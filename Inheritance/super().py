import sys
sys.stdout = open("output.txt","w")


class Vehicle:
	"""Base class for all vehicles"""

	def __init__(self, name, manufacture, color):
		print("Creating a vehicle")
		self.name = name
		self.manufacture = manufacture
		self.color = color


class Car(Vehicle):
	"""Car class"""

	def __init__(self, name, manufacture, color, year):
		print("Creating a 	car")
		super().__init__(name, manufacture, color)
		self.year = year
		self.wheels = 4


if __name__ == "__main__":
	c = Car("Mustang 5.0 GT Coupe", "Ford", "Red", 2017)
	print(c.name, c.year, c.wheels)
