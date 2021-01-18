import sys
sys.stdout = open("output.txt","w")

import re

string = "This is line 1. Date is 2017/06/01. And there is another date : 2017-07-01. The third and final date is 2017/08/30."

pat = re.compile(r"(\d{4})[-/](\d{2})[-/](\d{2})")
print(pat,end="\n\n\n")
print(type(pat),end="\n\n\n")
result = pat.findall(string)
print(result,end="\n\n\n")

string = "New date: 2017/06/15"
result = pat.findall(string)
print(result,end="\n\n\n")

print(dir(pat),end="\n\n\n")