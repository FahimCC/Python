import logging
import requests
import re
import csv
import sys
from html import unescape
sys.stdout = open("output.txt","w")

def get_category_list(content):
	"""get_category_list() takes content of home page and returns a list of categories and their urls"""
	
	return category_pat.findall(content)


def get_book_list(content):
	"""get_book_list(content) takes a content of a book list page and returns a list of books(name ans url)"""
	
	content = content.replace("\n", " ")
	result = book_list_pat.findall(content)
	return result


def get_product_details(content):
	"""get_product_details(content) takes content of a product page, parses the page and returns details about a product"""
	
	image_base = "http://books.toscrape.com/"
	result = img_pat.findall(content)
	if(len(result) == 0):
		logging.warning("Image url not found!")
		img_url = ""
	else:
		img_url = result[0].replace("../../","")
		img_url = image_base + img_url

	result = desc_pat.findall(content)
	if(len(result) ==0):
		logging.warning("Description not found!")
		description = ""
	else:
		description = result[0]

	result = upc_pat.findall(content)
	if(len(result) ==0):
		logging.warning("UPC not found!")
		upc = ""
	else:
		upc = result[0]

	result = price_pat.findall(content)
	if(len(result) ==0):
		logging.warning("Price not found!")
		price = ""
	else:
		price = result[0]

	result = avail_pat.findall(content)
	if(len(result) ==0):
		logging.warning("UPC not found!")
		availability = ""
	else:
		availability = result[0]

	return upc, price, img_url, availability, description


def get_page_content(url):
	"""get_page_content() takes a url and returns the content of the page"""
	
	try:
		response = requests.get(url)
		#print(response.ok)
	except requests.exceptions.RequestException as e:
		logging.error(e)


	if(response.ok):
		return response.text

	logging.error("Cannot get content from URL: " + url)

	return None


def get_next_page(url, content):
	"""Checks the content of a book list page and returns link of the next page"""
	
	result = next_page_pat.findall(content)
	if(len(result) == 0):
		return None

	i = url.rfind("/")
	return url[0:i+1] + result[0]


def scrape_book_info(book_info, category_name):
	"""gets the content of abook details page, and parsws different components and stores the info"""
	
	book_url, book_name = book_info
	book_dict = {"Name": unescape(book_name), "Category": category_name}
	
	book_url = book_url.replace("../../../","")
	book_url = "http://books.toscrape.com/catalogue/" + book_url
	book_dict["URL"] = book_url

	#print("Scraping book", unescape(book_name))
	logging.info("Scraping : " + book_url)

	content = get_page_content(book_url)
	content = content.replace("\n", " ")

	upc, price, img_url, availability, description = get_product_details(content)

	book_dict["UPC"] = upc
	book_dict["Price"] = price
	book_dict["ImageURL"] = img_url
	book_dict["Availability"] = availability
	book_dict["Description"] = unescape(description)

	csv_writer.writerow(book_dict)


def crawl_category(category_name, category_url):
	"""crawls a particular category of book"""

	while True:
		content = get_page_content(category_url)
		book_list = get_book_list(content)

		for book in book_list:
			scrape_book_info(book, category_name)

		next_page = get_next_page(category_url, content)
		if next_page is None:
			break

		category_url = next_page


def crawl_website():
	"""crawl_website() is the main function that coordinates the whole crawling task"""

	url = "http://books.toscrape.com/index.html"
	host_name = "books.toscrape.com"

	content = get_page_content(url)
	if content is None:
		logging.critical("Failed to get content from " + url)
		sys.exit(1)

	category_list = get_category_list(content)

	for category in category_list:
		category_url, category_name = category
		category_url = "http://" + host_name + "/" + category_url
		#print(category_url)
		#sys.exit(1)
		crawl_category(category_name, category_url)


if __name__ == "__main__":
	#Compile different regular expression patterns 
	category_pat = re.compile(r'<li>\s*<a href="(catalogue/category/books/.*?)">\s*(\w+[\s\w]+\w)\s*?<', re.M | re.DOTALL)
	
	next_page_pat = re.compile(r'<li class="next"><a href="(.*?)">next</a></li>')

	book_list_pat = re.compile(r'<h3><a href="(.*?)" title="(.*?)">')

	img_pat = re.compile(r'<div class="item active">\s*<img src="(.*?)"')

	desc_pat = re.compile(r'<div id="product_description" class="sub-header">.*?<p>(.*?)</p>')

	upc_pat = re.compile(r'<th>UPC</th>\s*<td>(.*?)</td>')

	price_pat = re.compile(r'<th>Price \(incl. tax\)</th>\s*<td>(.*?)</td>')

	price_pat = re.compile(r'<th>Price \(incl. tax\)</th>\s*<td>\D+([\d.]+?)</td>')

	avail_pat = re.compile(r'<th>Availability</th>\s*<td>(.*?)</td>')

	logging.basicConfig(format="%(asctime)s %(message)s", datefmt="%d/%m/%y %I:%M:%S %p", filename="bookstore_crawler.log", level=logging.DEBUG)

	field_names = ["Name", "Category", "UPC", "URL", "ImageURL", "Price", "Availability", "Description"]

	with open("book_list.csv", "w",encoding="ISO-8859-1") as csvf:
		csv_writer = csv.DictWriter(csvf, fieldnames=field_names)
		csv_writer.writeheader()
		crawl_website()