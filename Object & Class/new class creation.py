import sys
sys.stdout = open("output.txt","w")

class Car:
	name = ""
	color = ""

	def start():
		print("Starting the engine pip.... pip.....")

if __name__ == "__main__":
	Car.name = "Axio"
	Car.color = "Black"

	print("Name of the car: ", Car.name)
	print("Color: ",Car.color)
	Car.start()