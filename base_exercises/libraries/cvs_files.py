import csv

#with open("data.csv", "w") as file:
    #writer = csv.writer(file)
   #writer.writerow(["transaction_id", "product_id", "price"])
   #writer.writerow([10000, 1, 5])
   #writer.writerow([30000, 2, 25])

with open("data.csv") as read_file:
    reader = csv.reader(read_file)
    #print(list(reader)) if this line is executed the 
    # pointer of the file will go to the end and we 
    # will be unable to print every row
    for row in reader:
        print(row)