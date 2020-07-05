# Write a function to write a comma-separated value (CSV) file. It
# should accept a filename and a list of tuples as parameters. The
# tuples should have a name, address, and age. The file should create
# a header row followed by a row for each tuple. If the following list of
# tuples was passed in:

# [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]
# it should write the following in the file:
# name,address,age
# George,4312 Abbey Road,22
# John,54 Love Ave,21

import csv

def write_csv(filename, lst):
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Address', 'Age'])
        for i in range(len(lst)):
            writer.writerow(lst[i])


def read_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for eachline in reader:
            print(eachline)


filename = 'new_csv.csv'
lst = [('George', '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]

write_csv(filename, lst)
read_csv(filename)


