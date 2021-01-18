import sys
sys.stdout = open("output.txt","w")

import csv

field_names = ["Name","Author","Publisher","Price","Category"]

book1 = {"Name": "Computer Programming, Part 1","Author": "Tamim Shahriar Subeen","Publisher": "Onnorokom Prokashoni","Price": "240.00","Category": "Programming"}

book2 = {"Name": "Computer Programming, Part 2","Author": "Tamim Shahriar Subeen","Publisher": "Onnorokom Prokashoni","Price": "250.00","Category": "Programming"}

book3 = {"Name": "Learn Programming with Python","Author": "Tamim Shahriar Subeen","Publisher": "Dimik Prokashoni","Price": "200.00","Category": "Programming"}

book_list = [book1,book2,book3]

with open("DictBooks.csv","w") as csvf:
	csv_writer = csv.DictWriter(csvf, fieldnames = field_names)
	csv_writer.writeheader()
	csv_writer.writerows(book_list)

# with open("DictBooks.csv", newline='') as csvfile:
# 	csv_reader = csv.reader(csvfile)
# 	#print(csv_reader)
# 	for row in csv_reader:
# 		print(row)