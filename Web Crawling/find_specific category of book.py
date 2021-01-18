import sys
sys.stdout = open("output.txt","w")

import re
import requests

url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
response = requests.get(url)
print(response.ok)

string = response.text
string = string.replace("\n", " ")

compiler = re.compile(r'<h3><a href="(.*?)" title="(.*?)">',)

result = re.findall(compiler, string)
print(len(result))
print(result[0])