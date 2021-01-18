def binarySearch(L, x):
	left, right = 0, len(L)-1

	while left <= right:
		mid = (left+right)//2

		if L[mid] == x:
			return mid
		elif L[mid] < x:
			left = mid + 1
		else:
			right = mid - 1

	return -1
#table driven test
def testBianrySearch():
	test_cases = [
		{
			"name": "simple case 1",
			"input1": [1,2,3],
			"input2": 2,
			"expected": 1
		},
		{
			"name": "simple case 2",
			"input1": [1,2,1,4],
			"input2": 4, 
			"expected": 3
		},
		{
			"name": "simple case 3",
			"input1": [100],
			"input2": 100,
			"expected": 0
		},
		{
			"name": "simple case 4",
			"input1": [7,3,4,2,9],
			"input2": 10,
			"expected": -1
		},
		{
			"name": "empty list",
			"input1": [],
			"input2": None,
			"expected": -1
		}
	]

	for test_case in test_cases:
		assert test_case["expected"] == binarySearch(test_case["input1"],test_case["input2"]), test_case["name"]


if __name__ == "__main__":
	L = [1,2,3,4,5,6,7,8,9]

	for x in range(1,11):
		position = binarySearch(L, x)

		if position == -1:
			if x in L:
				print(x, "is in L, but function returnrd -1")
			else:
				print(x,"not in list")

		else:
			if L[position] == x:
				print(x, "found in correct position.")
			else:
				print("binary search returned", position, "for", x, "which is incorrect")
	print("Program Terminated")