def selectionSort(L):
	n = len(L)

	for i in range(0, n-1):
		indexMin = i

		for j in range(i+1, n):
			if L[j] < L[indexMin]:
				indexMin = j

		if i != indexMin:
			L[i], L[indexMin] = L[indexMin], L[i]

	return L

#table driven test
def testSelectionSort():
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
		assert test_case["expected"] == selectionSort(test_case["input"]), test_case["name"]


if __name__ == "__main__":
	L = [6,1,4,9,2]

	print("Before sort: ", L)
	selectionSort(L)
	print("After sort: ", L)
