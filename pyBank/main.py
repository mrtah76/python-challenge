# import Dependencies
import os
import csv


#locate csv file
csvpath = os.path.join('Resources', 'budget_data.csv')
#lets take look at the file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    for row in csvreader:
        print(row)
# the total number of month included in the dataset
total_month_num = len(csvreader)
print(total_month_num)