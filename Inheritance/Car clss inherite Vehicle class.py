import sys
sys.stdout = open("output.txt","w")


class Vehicle:
	"""Base class for all vehicles"""

	def __init__(self, name, manufacture, color):
		self.name = name
		self.manufacture = manufacture
		self.color = color

	def drive(self):
		print("Driving", self.manufacture, self.name)
	
	def turn(self, direction):
		print("Turning", self.nam66e, "to", direction)
	
	def brake(self):
		print(self.name, "is stopping!")


class Car(Vehicle):
	"""Car class"""

	def change_gear(self, gear_name):
		"""Method for changing gear"""
		print(self.name, "is change gear to", gear_name)


if __name__ == "__main__":
	c = Car("Mustang 5.0 GT Coupe", "Ford", "Red")
	c.drive()
	c.brake()
	c.change_gear("p")
