import sys
sys.stdout = open("output.txt","w")


class Vehicle:
	"""Base class for all vehicles"""

	def __init__(self, name, manufacture, color):
		print("Creating a vehicle")
		self.name = name
		self.manufacture = manufacture
		self.color = color


class MotorCycle(Vehicle):
	"""MotorCycle class"""

	def __init__(self, name, manufacture, color, year):
		print("Creating a MotorCycle")
		super().__init__(name, manufacture, color)
		self.year = year
		self.wheels = 4


if __name__ == "__main__":
	m = MotorCycle("Walton", "Walton", "Red", 2017)
	print(m.name, m.year, m.wheels)
