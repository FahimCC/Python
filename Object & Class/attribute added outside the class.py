import sys
sys.stdout = open("output.txt","w")

class Car:

	def __init__(self,n,c):
		self.name = n
		self.color = c

	def start(self):
		print("Name: ",self.name)
		print("Color: ",self.color)
		print("Year: ",self.year)
		print("Starting the engine")

if __name__ == "__main__":
	#Creating a Car object
	my_car = Car("Allion", "Red")
	my_car.year = 2017

	Car.start(my_car)
	my_car.start()