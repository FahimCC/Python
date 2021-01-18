

def find_fib(n):
	if(n <= 2):
		return 1

	fib_x, fib_next = 1, 1	
	i = 3;
	while(i <= n):
		i += 1
		fib_x, fib_next = fib_next, fib_x + fib_next

	return fib_next

def list_fib(n):
	fib_list = [1,1]
	if(n <= 2):
		return fib_list[:n]

	fibx, fibnext = 1, 1	
	i = 3;
	while(i <= n):
		i += 1
		fibx, fibnext = fibnext, fibx + fibnext
		fib_list.append(fibnext)

	return fib_list


if __name__ == "__main__":

	for x in range(1,11):
		print(find_fib(x))
	print(list_fib(1))
	print(list_fib(2))
	print(list_fib(10))
