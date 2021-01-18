import sys
sys.stdout = open("output.txt","w")

def div(a, b):
	try:
		return a/b
	except ZeroDivisionError:
		return "Cannot divide by zero"
	except TypeError:
		return "Unsupported type. Did you use string?"
	except Exception as e:
		return e

if __name__ == "__main__":
	print(div(1,2))
	print(div(1,0))
	print(div(0,2))
	print(div(0,'2'))