import sys
sys.stdin = open("input.txt","r")
sys.stdout = open("output.txt","w")

with open("test.txt","r") as fp:
	for line in fp:
		s = (str(line[0])).lower() + ".txt"
		with open(s,"a") as fp:
			fp.write(line)