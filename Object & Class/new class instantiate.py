import sys
sys.stdout = open("output.txt","w")

class Car:
	name = "Premio"
	color = "White"

	def __init__(self,n,c):
		self.nam = n
		self.colo = c

	def start(self):
		print("Starting the engine")

if __name__ == "__main__":
	#Creating a Car object
	my_car = Car("Allion", "Red")

	print("Fahim")
	print(Car.name)
	print(my_car.nam)