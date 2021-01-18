def linearSearch(L, x):
	n = len(L)

	for i in range(n):
		if L[i] == x:
			return i;

	return -1

#table driven test
def testLinearSearch():
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
		assert test_case["expected"] == linearSearch(test_case["input1"],test_case["input2"]), test_case["name"]


if __name__ == "__main__":
	result = linearSearch([7,3,4,2,9], 7)
	print(result)