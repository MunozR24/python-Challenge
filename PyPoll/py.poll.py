# Import the necessary libraries
import os
import csv

# Set the file path for the CSV file

file_path = os.path.join('Resources', 'election_data.csv')
# Initialize variables
total_votes = 0
candidate_votes = {}
candidates = []

# Read the CSV file
with open(file_path, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    
    # Skip the header row
    header = next(csvreader)
    
    # Loop through each row in the CSV file
    for row in csvreader:
        # Calculate total votes
        total_votes += 1
        
        # Get the candidate's name
        candidate_name = row[2]
        
        # Add candidate to the list of candidates if not already present
        if candidate_name not in candidates:
            candidates.append(candidate_name)
        
        # Count the votes for each candidate
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

# Calculate the percentage of votes each candidate won
candidate_percentages = {}
for candidate in candidates:
    candidate_percentages[candidate] = (candidate_votes[candidate] / total_votes) * 100

# Find the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print the analysis results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {candidate_percentages[candidate]:.3f}% ({candidate_votes[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")