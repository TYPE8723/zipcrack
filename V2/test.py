import csv

with open("passwords.csv",'r') as csv_reader:
    data = csv.reader(csv_reader)
    row_count = sum(1 for row in data)#this makes the cursor go to the end of file.
    #moves cursor to starting
    csv_reader.seek(0)
    for row in data:
        print(row)