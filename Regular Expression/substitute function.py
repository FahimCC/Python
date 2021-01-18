import sys
sys.stdout = open("output.txt","w")

import re

string = "abcd 1234 - 33"
result = re.sub(r"\d", "0", string)
print(result)

string = "22/07/2017, 20/01/2017, 01/01/2018"
#result = re.sub(r"(\d{4})/(\d{2})/(\d{2})", "\3-\2-\1", string)
result = re.sub(r"(\d{4})/(\d{2})/(\d{2})", "\g<3>-\g<2>-\g<1>", string)
print(result)
