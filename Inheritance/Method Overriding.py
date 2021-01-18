import sys
sys.stdout = open("output.txt","w")


class Vehicle:
	"""Base class for all vehicles"""

	def __init__(self, name, manufacture, color):
		self.name = name
		self.manufacture = manufacture
		self.color = color
	
	def turn(self, direction):
		print("Turning", self.name, "to", direction)


class Car(Vehicle):
	"""Car class"""

	def __init__(self, name, manufacture, color, year):
		self.name = name
		self.manufacture = manufacture
		self.color = color
		self.year = year
		self.wheels = 4

	def change_gear(self, gear_name):
		"""Method for changing gear"""
		print(self.name, "is change gear to", gear_name)
	
	def turn(self, direction):
		print(self.name, "is turning", direction)



if __name__ == "__main__":
	c = Car("Mustang 5.0 GT Coupe", "Ford", "Red", 2017)
	v = Vehicle("Softail Delux", "Harley-Davidson", "Blue")
	c.turn("right")
	v.turn("right")
