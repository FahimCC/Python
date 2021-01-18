import sys
sys.stdout = open("output.txt","w")


import re

text = "multiple phone number, 01521431178, 01869457862, 01521431176, 01552301706 00000000000"
li= re.findall(r"\d{3}\s*\d{8}",text)
print(li,end='\n\n\n')

li= re.findall(r"01[3456789]\s*\d{8}",text)
print(li,end='\n\n\n')

text = "Banlga english bangla"
li = re.findall(r"english", text)
print(li,end='\n\n\n')

li = re.findall(r"^english", text)
print(li,end='\n\n\n')

li = re.findall(r"english$", text)
print(li,end='\n\n\n')

li = re.findall(r"^Banlga", text)
print(li,end='\n\n\n')

li = re.findall(r"bangla$", text)
print(li,end='\n\n\n')

text = "Bangla english Bangla"
li = re.findall(r"^bangla", text, re.I)
print(li,end='\n\n\n')

li = re.findall(r"bangla$", text, re.IGNORECASE)
print(li,end='\n\n\n')

with open("file.txt","r") as fp:	
	text = fp.read()

li = re.findall(r"^.*?$", text, re.MULTILINE)
print(li,end='\n\n\n')

text = "<li>Fahim</li><li>Nuren</li><li>Faysal</li><li>Durdana</li>"
li = re.findall(r"<li>(.*?)</li>", text)
print(li,end='\n\n\n')