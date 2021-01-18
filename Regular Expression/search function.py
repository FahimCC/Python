import sys
sys.stdout = open("output.txt","w")

import re

text = "Bangladesh"
match = re.search("Bangla", text)
print(match.group())

match = re.search("des", text)
print(match.group())

match = re.search('dets', text)
print(type(match))
print(match)

match = re.search('.', text)
print(match.group())

match = re.search('B.n', text)
print(match.group())

text = "Bangladesh is our homeland"
match = re.search('............', text)
print(match.group())

match = re.search('o\w\w', text)
print(match.group())

match = re.search('i\w\w', text)
print(match)

match = re.search('B\w+h', text)
print(match.group())

match = re.search('B.+h', text)
print(match.group())

match = re.search('B.+?h', text)
print(match.group())

text = "Phone number: 01521431178"
match = re.search('\d+', text)
print(match.group())

text = "house number:5, Phone number: 01521431178"
match = re.search('\d+', text)
print(match.group())

match = re.search('\d{11}', text)
print(match.group())

text = "house number:5, Phone number: 015 21431178"
match = re.search('\d{3}\s*\d{8}', text) #\s* space zero/more
print(match.group())

match = re.search('\d{3}\s?\d{8}', text) #? space nao thakte pare thakle 1 tar beshi na
print(match.group())
