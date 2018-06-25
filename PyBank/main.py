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
    greatest_increase=max(revenue)
    greatest_decrease=min(revenue)
    average_change=round(total/total_months,2)
    print('Financial Analysis \n')
    print('------------------------------')
    print('Total Months: '+str(total_months))
    print('Total: $'+str(total))
    print('Average Change: $'+str(average_change))
    for rows in csvreader:
        if greatest_increase==rows[1]:
            greatest_increase_month=rows[0]
        if greatest_decrease==rows[1]:
            greatest_decrease_month=rows[0]      
    print('Greatest Increase in Profits: '+greatest_increase_month +' ($'+str(greatest_increase)+')')
    print('Greatest Decrease in Profits: '+greatest_decrease_month +' ($'+str(greatest_decrease)+')')




    