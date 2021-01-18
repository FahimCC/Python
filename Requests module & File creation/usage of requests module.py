import requests
import sys
sys.stdout = open("output.txt","w")

if __name__ == "__main__":
	url = "http://example.com/"
	response = requests.get(url)

	print(response.ok)
	print(response.status_code)
	print(response.reason)
	print(dir(response))
	print(type(response))
	print(response.text)
	print(type(response.text))