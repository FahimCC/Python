import sys
sys.stdout = open("output.txt","w")

import csv

field_names = ["Name","Author","Publisher","Price","Category"]

book1 = ["Computer Programming Part 1","Tamim Shahriar Subeen","Onnorokom Prokashoni","240.00","Programming"]

book2 = ["Computer Programming Part 2","Tamim Shahriar Subeen","Onnorokom Prokashoni","250.00","Programming"]

book3 = ["Learn Programming with Python","Tamim Shahriar Subeen","Dimik Prokashoni","200.00","Programming"]

book_list = [book1,book2,book3]

with open("books.csv","w") as csvf:
	csv_writer = csv.writer(csvf, delimiter=',', quotechar="\"", quoting=csv.QUOTE_MINIMAL)
	csv_writer.writerow(field_names)
	for book in book_list:
		csv_writer.writerow(book)

with open("books.csv", newline='\n') as csvfile:
	csv_reader = csv.reader(csvfile)
	for row in csv_reader:
		print(row)