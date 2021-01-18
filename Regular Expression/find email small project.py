import sys
sys.stdout = open("output.txt","w")

import re

string = "cp.book at subeen.com, bo_o.k At subeen.com, book (at) subeen dot com, book [at] subeen [dot] com"

#replace @
string = re.sub(r"\s+[\(\[]*\s*at\s*[\)\]]*\s+", "@", string,flags=re.IGNORECASE)

#replace .
string = re.sub(r"\s+[\(\[]*\s*dot\s*[\)\]]*\s+", ".", string,flags=re.IGNORECASE)

print(string,end="\n\n\n")

result = re.findall(r"[.\w]+@\w+[.]\w+", string)

print(result,end="\n\n\n")