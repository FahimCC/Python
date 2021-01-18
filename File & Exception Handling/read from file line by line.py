import sys
sys.stdout = open("output.txt","w")

lines = ["This is the first line\nThis is the second line","This is the third line"]

with open("file.txt","w") as fp:
	for line in lines:
		fp.write(line+"\n")

#1st way
with open("file.txt","r") as fp:
	content = fp.readlines()
	print(content)
	for line in lines:
		print(line)

#2nd way
with open("file.txt","r") as fp:
	for line in fp:
		print(line,end="")