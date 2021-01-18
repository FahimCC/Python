
if __name__ == "__main__":
	import trial
	import fibo

	print("Hello, I am inside program.py!")
	print(trial.__name__)
	print(fibo.__name__)
	n = fibo.find_fib(100)
	print("15th fibonacci number is,", n)

	
