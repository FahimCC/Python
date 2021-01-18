import sys
sys.stdout = open("output.txt","w")

if __name__ == "__main__": 
	import turtle
	from turtle import Turtle
	
	nonte = Turtle()
	fonte = Turtle()

	nonte.shape("circle")
	fonte.shape("square")
	nonte.left(30)
	nonte.forward(100)
	fonte.backward(50)

	monte = Turtle()
	monte.setpos(-100,-100)
	monte.forward(30)
	monte.clear()
	nonte.clear()
	#fonte.clear()
	fonte.shape("triangle")
	monte.shape("square")


	turtle.done()