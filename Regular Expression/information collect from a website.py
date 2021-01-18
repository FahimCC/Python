import re
import os
import requests
import sys
sys.stdout = open("output.txt","w")

def create_directory(name):
	try:
		os.mkdir(name)
	except FileExistsError:
		print(name, "already exists")

def get_directory_name(regexp, url):
	result = re.findall(regexp, url)
	dir_name = "_".join(result[0])
	return dir_name

def download_image(image_url, file_name):
	print("Image Downloading.... ")
	response = requests.get(image_url)

	with open(file_name,"wb") as fp:
		fp.write(response.content)

def process():
	main_dir = "dimik_pub"
	create_directory(main_dir)

	URL = ["http://dimik.pub/page/1", "http://dimik.pub/page/2", "http://dimik.pub/page/3"]
	for page in URL:
		print(page)
		response = requests.get(page)
		if response.ok is False:
			sys.exit("Could not get response from server")
		page_content = response.text

		regexp = re.compile(r'<div class="book-cover">\s*<a href="(.*?)">\s*<img src="(.*?)">.*?<h2 class="sd-title"><.*?>(.*?)<', re.S)
		result = re.findall(regexp, page_content)

		dir_regexp = re.compile(r'book/(\d+)/(\w+)-(\w+)-')

		for item in result:
			url = item[0]
			name =	item[2]
			image_url = item[1]

			string = get_directory_name(dir_regexp,url)
			dir_name = main_dir + "/" + string

			create_directory(dir_name)

			file_name = dir_name + "/" + "info.txt"

			with open(file_name,"w",encoding="utf-8") as fp:
				fp.write(name + "\n")
				fp.write(url)

			image_file_name = dir_name + "/" + "image.png"
			download_image(image_url, image_file_name)

if __name__ == "__main__":
	process()