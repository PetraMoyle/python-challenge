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
candidates_list = []
vote_count_per_candidate = [] 

for row in csv_reader:

    #total votes count
    total_votes = total_votes + 1

    #rading the candidates in column 3 
    candidate = (row[2])

    #if candidate found in the candidate list, then locate the candidate by index & increment the vote count per candidate by 1     
    if candidate in candidate_list:   
        candidate_index = candidates_list.index(candidate)
        vote_count_per_candidate[candidate_index] = vote_count_per_candidate[candidate_index] + 1
    else:
        #if candidate not found in candidate list, then append to the candidate list and 1 vote 
        candidates_list.append(candidate)
        vote_count_per_candidate.append(1)


    print(total_votes) 
    print(candidates_list) 
    print(vote_count_per_candidate)        
    
    #Variables
    percentage = []
    max_votes = vote_count_per_candidate[0]
    index = 0

for i in range(len(candidates_list))
    #getting the percentage 
    vote_percentage = round(vote_count_per_candidate/total_votes*100,2)
    percentage.append(vote_percentage)

    #finding the maximum votes to determine the election winner
    max_votes = vote_count_per_candidate[i]
    index[i]

election_winner = candidates_list[index]

#election results txt file 
# Specify the file to write to
election_results = os.path.join( "output", "election_results.txt")

# # Open the file using "write" mode. Specify the variable to hold the contents
with open(election_results, 'w') as txt_file:

    #Initialize txt.writer
    txt_writter = txt.writer (txt_file, delimeter=',')

    txt_file.write("Election Results\n")
    txt_file.write("-------------------------------------------------------\n")
    txt_file.write("Total Votes:" + " " + str(total_votes))
    txt_file.write("\n")
    txt_file.write("-------------------------------------------------------\n")
    for i in range(len(candidates_list)):
        txt_file.write(candidates_list[i] ":" + " " + str(percentage[i] + "%" + (str(vote_count_per_candidate[i]))
    txt_file.write("\n")
    txt_file.write("-------------------------------------------------------\n")
    txt_file.write("Winner:" + " " + election_winner.upper())
    txt_file.write("-------------------------------------------------------\n")
    #txt_file.close()
