import os
import csv

file_path = os.path.join('Resources', 'budget_data.csv')
#variables to store data
total_months = 0
net_total = 0
changes = []
dates = []
greatest_increase = 0
greatest_decrease = 0


#Read the CSV file and store the data:

with open(file_path, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    header = next(csvreader)  # Skip the header row
    
    for row in csvreader:
        # Calculate total months and net total
        total_months += 1
        net_total += int(row[1])
        
        # Store dates and profits/losses for calculating changes
        dates.append(row[0])
        changes.append(int(row[1]))

#Calculate the changes in profits/losses

for i in range(1, len(changes)):
    change = changes[i] - changes[i - 1]
    if change > greatest_increase:
        greatest_increase = change
        greatest_increase_date = dates[i]
    elif change < greatest_decrease:
        greatest_decrease = change
        greatest_decrease_date = dates[i]

#Calculate the average change:

average_change = sum(changes[1:]) / len(changes[1:])

#Print the analysis results:

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")



