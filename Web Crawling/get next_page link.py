import sys
sys.stdout = open("output.txt","w")

import re
import requests

url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
response = requests.get(url)
print(response.ok)
string = response.text
next_page = re.findall(r'<li class="next"><a href="(.*?)">next</a></li>', string)


s = str(next_page[0])
url = "http://books.toscrape.com/catalogue/category/books/mystery_3/index.html"
i = url.rfind("/")
print(url[0:i+1])
url = url[0:i+1] + s
print(url)