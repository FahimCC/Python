def average(L):
	if not L:
		return None

	return sum(L)/len(L)

def test_average():
	assert average([1,2,3,4,5]) == 3.0 , "average() produced incorrect result"

if __name__ == "__main__":
	L = [7,3,4,2,9]
	average(L)