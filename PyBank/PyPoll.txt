# Module for the file path
import os
directory = os.path.dirname(__file__)

# Module for reading CSV files
import csv
election_data = os.path.join(directory,'Resources', 'election_data.csv')

# open/read the file
with open(election_data.csv) as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Read the header row 
    csv_header = next(csv_reader)
  
# Variables
total_votes = 0
candidate = 0
candidate_list = []
votes_for_khan = 0

khan = []

    for candidate in candidate_list:
        candidate_list.append(candidate)
        if candidate in candidate_list:
            
    
    for row in csv_reader:
        if row[2] == candidate:
            candidate_list.append(candidate)
                if candidate = candidate:

            
            
            votes_for_khan = votes_for_khan + 1




    

        votes = candidate_votes[candidate]
        vote_percentage = float(votes)/float(total_votes)*100
        if (votes > winner_count):
            winner_count = votes
            winner = candidate
        voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(voter_output)
        txt_file.write(voter_output)
        