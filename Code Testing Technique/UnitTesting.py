def average(L):
	if not L:
		return None

	return sum(L)/len(L)

def test_average():
	assert average([1,2,3,4,5]) == 3.0 