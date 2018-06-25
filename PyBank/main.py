import os
import csv
csvpath = os.path.join('..','..','Instructions', 'PyBank','Resources','budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    total_months=0
    total=0
    revenue=[]
    for row in csvreader:
        total_months=total_months+1
        total=total+int(row[1])
        revenue.append(int(row[1]))
    print(revenue)
    average_change=round(total/total_months,2)
    greatest_increase=max(revenue)
    greatest_decrease=min(revenue)
    print(total_months)
    print(total)
    print(average_change)
    print(greatest_increase)
    print(greatest_decrease)


    