import os
import csv
csvpath = os.path.join('..','..','Instructions','PyBank','Resources','budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    total_months=0
    total=0
    revenue=[]
    row_number="first_row"
    change=0
    previous_row=0
    change_list=[]
    for row in csvreader:
        total_months=total_months+1
        total=total+int(row[1])
        revenue.append(int(row[1]))
        if row_number=="first_row":
            previous_row=int(row[1])
            row_number="next_row"
        else:
            change=(int(row[1])-previous_row)
            change_list.append(int(change))
            previous_row=int(row[1])
            row_number=="next_row"     
    greatest_increase=max(revenue)
    greatest_decrease=min(revenue)
    csvfile.seek(0)
    for values in csvreader:
        if values[1]==greatest_increase:
            greatest_increase_month=values[0]
        if values[1]==greatest_decrease:
            greatest_decrease_month=values[0]
    change_sum=sum(change_list)
    average_change=round(change_sum/len(change_list),2)
    print('\nFinancial Analysis \n')
    print('------------------------------')
    print('Total Months: '+str(total_months))
    print('Total: $'+str(total))
    print('Average Change: $'+str(average_change))
    print(greatest_increase_month)
    print(greatest_decrease_month)



