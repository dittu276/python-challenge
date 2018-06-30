import os
import csv
#path
csvpath = os.path.join('..','..','Instructions', 'PyPoll','Resources','election_data.csv')
#read csv file
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
#read header and skip
    csv_header = next(csvreader)
#declare variables
    total_voters=0
    candidates=[]
    voters={}
#print initial statments
    print("\nElection Results")
    print("----------------------")
#iterate through rows to find total voters and append candidates to a list
    for row in csvreader:
        total_voters=total_voters+1
        candidates.append(row[2])
    print("Total Votes:"+" "+str(total_voters))
    print("----------------------------")
#convert candidates to unique set and count the number of voters for each candidates from candidates list
    for each in set(candidates):
        count=candidates.count(each)
#append each cadidate and their respective votes into a dictionary
        voters[each]=count
#calculate respective percentage for each candidate
        percentage=round(count/total_voters * 100,2)
#print results
        print(each+": "+str(percentage)+"% "+"("+str(count)+")")
#find winner from the dictionary
    winner_name= max(voters, key=voters.get)
#print results
    print("------------------------")
    print("Winner: "+str(winner_name))
    print("------------------------")
    


