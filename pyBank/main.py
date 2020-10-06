


import csv
import os
# Files to load and output 
file_to_load = os.path.join("Resources", "pybank_homework.csv")
file_to_output = os.path.join("analysis", "Results_pyB.txt")

# Track various financial parameters
total_months = 0
month_of_change = []
net_change_list = []
date=[]
total_net = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as financial_data:
   reader = csv.reader(financial_data)
   # Read the header row
   header = next(reader)

# Extract first row to avoid appending to net_change_list
   first_row = next(reader)
   total_months += 1   
   total_net += int(first_row[1])
   prev_net = int(first_row[1])
   for row in reader:
       # Track the total
       date.append(row[0])
       total_months += 1
       total_net += int(row[1])
       # Track the net change
       net_change = int(row[1]) - prev_net
       prev_net = int(row[1])
       net_change_list += [net_change]


# Calculate the greatest increase
greatest_increase=max(net_change_list)
greatest_month_i=date[net_change_list.index(greatest_increase)]

# Calculate the greatest decrease
greatest_decrease=min(net_change_list)
greatest_month_d=date[net_change_list.index(greatest_decrease)]

# Calculate the Average Net Change
net_monthly_avg = sum(net_change_list) / len(net_change_list)


results=(
f"Total month: {total_months}\n"
f"Total : {total_net}\n"
f"Average Change : {net_monthly_avg}\n"
f"Greatest Increase in Profits:: {greatest_month_i} ${greatest_increase}\n"
f"Greatest Decrease in Profits: {greatest_month_d} ${greatest_decrease}\n")

with open (file_to_output,'w') as file:
    file.write(results)