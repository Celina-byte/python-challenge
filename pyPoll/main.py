import csv
import os
# Files to load and output 
file_to_load = os.path.join("Resources", "pyPoll_Homework.csv")
file_to_output = os.path.join("analysis", "Results.txt")

# Track various financial parameters
total_votes = 0
kvotes=0
candidate1="Khan"
kpercentage=0
cvotes=0
candidate2="Correy"
cpercentage=0
lvotes=0
candidate3="Li"
lpercentage=0
ovotes=0
candidate4="O'Tooley"
opercentage=0
Winner = []


# total votes
with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    # Read the header row
    header = next(csvreader)
    
    total_votes += 1 
    for row in csvreader:
        #Track the votes
        total_votes +=1

#Khan votes
with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    # Read the header row
    header = next(csvreader) 
    for row in csvreader:
        if row[2]==candidate1:
            kvotes +=1
        kpercentage=(kvotes/total_votes)*100

#Correy votes
with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    # Read the header row
    header = next(csvreader) 
    for row in csvreader:
        if row[2]==candidate2:
            cvotes +=1
        cpercentage=(cvotes/total_votes)*100

#Li votes
with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    # Read the header row
    header = next(csvreader) 
    for row in csvreader:
        if row[2]==candidate3:
            lvotes +=1
        lpercentage=(lvotes/total_votes)*100

#O'Tooley votes
with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    # Read the header row
    header = next(csvreader) 
    for row in csvreader:
        if row[2]==candidate4:
            ovotes +=1
        opercentage=(ovotes/total_votes)*100

#Winner
if (kvotes>cvotes)and(kvotes>lvotes)and(kvotes>ovotes):
    Winner=candidate1
elif (cvotes>kvotes)and(cvotes>lvotes)and(cvotes>ovotes):
        Winner=candidate2
elif (lvotes>kvotes)and(lvotes>cvotes)and(lvotes>ovotes):
        Winner=candidate3
elif (ovotes>kvotes)and(ovotes>cvotes)and(ovotes>lvotes):
        Winner=candidate4


results=(
"Election Results\n----------------------------\n"
f"Total Votes: {total_votes}\n-----------------------\n"
f'Khan: {kpercentage:.2f}% ({kvotes})\n'
f'Correy: {cpercentage:.2f}% ({cvotes})\n'
f'Li: {lpercentage:.2f}% ({lvotes})\n'
f"O'Tooley: {opercentage:.2f}% ({ovotes})\n-----------------------\n"
f"Winner: {Winner}\n-----------------------")

print(results)


with open (file_to_output,'w') as file:
    file.write(results)