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
		print("Turning", self.name, "to", direction)
	
	def brake(self):
		print(self.name, "is stopping!")

if __name__ == "__main__":
	v1 = Vehicle("Fusion", "Walton", "Black")
	v2 = Vehicle("Delux", "Noah", "Blue")
	v3 = Vehicle("Mustang", "Ford", "Red")

	v1.drive()
	v2.drive()
	v3.drive()

	v1.turn("left")
	v1.turn("right")

	v1.brake()
	v2.brake()
	v3.brake()