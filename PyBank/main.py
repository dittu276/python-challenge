import os
import csv
#path
csvpath = os.path.join('..','..','Instructions','PyBank','Resources','budget_data.csv')
#read csv file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#read header and skip
    csv_header = next(csvreader)
#declare variables
    total_months=0
    total=0
    row_number="first_row"
    change=0
    previous_row=0
    change_list=[]
    month=[]
#find total months. total revenue and change between months
    for row in csvreader:
        total_months=total_months+1
        total=total+int(row[1])
        month.append(str(row[0]))
        if row_number=="first_row":
            previous_row=int(row[1])
            row_number="next_row"
        else:
            change=(int(row[1])-previous_row)
            change_list.append(int(change))
            previous_row=int(row[1])
            row_number=="next_row"     
#find greatest increase and decrease and find index for those in the change list
    greatest_increase=max(change_list)
    max_index=change_list.index(greatest_increase)
    greatest_decrease=min(change_list)
    min_index=change_list.index(greatest_decrease)
#find the max and min month in the month list
    max_month=month[max_index+1]
    min_month=month[min_index+1]
#find average change
    change_sum=sum(change_list)
    average_change=round(change_sum/len(change_list),2)
#print results to terminal
    print('\nFinancial Analysis \n')
    print('------------------------------')
    print('Total Months: '+str(total_months))
    print('Total: $'+str(total))
    print('Average Change: $'+str(average_change))
    print('Greatest Increase in Profits:'+' '+str(max_month)+ ' ('+str(greatest_increase)+')')
    print('Greatest Decrease in Profits:'+' '+str(min_month)+ ' ('+str(greatest_decrease)+')')



