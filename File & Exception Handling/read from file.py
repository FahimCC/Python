import sys
sys.stdout = open("output.txt","w")

lines = ["This is the first line", "This is the second line","This is the third line"]

with open("file.txt","w") as fp:
	for line in lines:
		fp.write(line+"\n")

with open("file.txt","r") as fp:
	content = fp.read()
	print(content)