#import csv

#with open('data/phone_book.csv', mode='r') as csv_file:
    #csv_reader = csv.reader(csv_file)
    #line_count = 0
    #for row in csv_reader:
        #if line_count==0:
            #line_count += 1
            #continue
        #print(f"{row[1]}: {row[2]}")


import csv

with open('data/phone_book.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        #print (type(row))
        print(row["first_name"], row["last_name"], row["phone_number"])
