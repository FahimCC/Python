def is_balanced(string):
	s = list()

	for ch in string:
		if ch == "(" or ch == "{" or ch == "[":
			s.append(ch)
		if ch == ")":
			if not s or s.pop() != "(":
				return False
		if ch == "}":
			if not s or s.pop() != "{":
				return False
		if ch == "]":
			if not s or s.pop() != "[":
				return False
	return True

if __name__ == "__main__":
	#string = input()

	string = "{(})" 

	#print(is_balanced(string))
	if is_balanced(string):
		print(string, "is balanced")
	else:
		print(string, "is not balanced")