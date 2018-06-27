import os
import csv
csvpath = os.path.join('..','..','Instructions', 'PyPoll','Resources','election_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    total_voters=0
    candidates=[]
    Khan=0
    Correy=0
    Li=0
    O_Tooley=0
    percentage=[]
    for row in csvreader:
        total_voters=total_voters+1
        if row[2] not in candidates:
            candidates.append(row[2])
        if row[2]=="Khan":
            Khan=Khan+1
        if row[2]=="Correy":
            Correy=Correy+1
        if row[2]=="Li":
            Li=Li+1
        if row[2]=="O'Tooley":
            O_Tooley=O_Tooley+1
    percentage_khan=round(int(Khan)/total_voters * 100,2)
    percentage.append(int(percentage_khan))
    percentage_correy=round(int(Correy)/total_voters * 100,2)
    percentage.append(int(percentage_correy))
    percentage_li=round(int(Li)/total_voters * 100,2)
    percentage.append(int(percentage_li))
    percentage_tooley=round(int(O_Tooley)/total_voters * 100,2)
    percentage.append(int(percentage_tooley))
    for candidate in candidates:
        print(candidate+':\n')
    print(total_voters)
    print(Khan)
    print(Correy)
    print(Li)
    print(O_Tooley)
    print(percentage_khan)
    print(percentage_correy)
    print(percentage_li)
    print(percentage_tooley)
    print(percentage)
    winner=max(percentage)
    print(winner)
    store these values in dictionary and display



       
