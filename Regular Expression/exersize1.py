import sys
sys.stdout = open("output.txt","w")

import re

with open("list.html","r") as fp:
	string = fp.read()

# result = re.sub(r"[\n\t]", "", string)
# string = result
# result = re.findall(r">(.*?)<", string, re.M)

# result = list(dict.fromkeys(result))
# result.remove("")

# for i in range(0,len(result)-1,3):
# 	print(result[i],"-",result[i+1],",",result[i+2])

result = re.findall(r"^(\w+?)\s+<ol>\s+<li>(.+?)</li>\s+<li>(.+?)</li>$", string,re.M)

for I in result:
	I = "-".join(I)
	a = re.sub(r"(.+?)-(.+?)-(.+?)", r" \1 - \2, \3", I)
	print(a)