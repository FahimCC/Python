def bubbleSort(L):
	n = len(L)

	for i in range(0, n):
		check = False
		for j in range(0,n-i-1):
			if L[j] > L[j+1]:
				check = True
				L[j], L[j+1] = L[j+1], L[j]
		if check == False:
			break;

	return L

#table driven test
def testBubbleSort():
	test_cases = [
		{
			"name": "simple case 1",
			"input": [1,2,3],
			"expected": [1,2,3]
		},
		{
			"name": "simple case 2",
			"input": [1,2,1,4],
			"expected": [1,1,2,4]
		},
		{
			"name": "simple case 3",
			"input": [100],
			"expected": [100]
		},
		{
			"name": "simple case 4",
			"input": [7,3,4,2,9],
			"expected": [2,3,4,7,9]
		},
		{
			"name": "empty list",
			"input": [],
			"expected": []
		}
	]

	for test_case in test_cases:
		assert test_case["expected"] == bubbleSort(test_case["input"]), test_case["name"]


if __name__ == "__main__":
	L = [6,1,4,9,2]

	print("Before sort: ", L)
	bubbleSort(L)
	print("After sort: ", L)
