import sys
sys.stdout = open("output.txt","w")

import requests
import re

url = "http://books.toscrape.com/index.html"
response = requests.get(url)
if response.ok is False:
	sys.exit("server not found")

print(len(response.text))

string = response.text

compiler = re.compile(r'<li>\s*<a href="(.*?)">\s*(\w+[\w\s]+\w)\s*?<', re.M | re.DOTALL)
result = re.findall(compiler, string)
print(len(result))

for item in result:
	print(item)