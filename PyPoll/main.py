# Module for the file path
import os
directory = os.path.dirname(__file__)

# Module for reading CSV files
import csv
election_data = os.path.join(directory,'Resources', 'election_data.csv')

# Open/read the file
with open(election_data) as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Read the header row 
    csv_header = next(csv_reader)
  
# Variables
    total_votes = 0
    candidate_list = []
    vote_count_per_candidate = [] 

    for row in csv_reader:

        #total votes count
        total_votes = total_votes + 1

        #rading the candidates in column 3 
        candidate = (row[2])

        #if candidate found in the candidate list, locate the candidate and increment the vote count per candidate by 1     
        if candidate in candidate_list:   
            candidate_index = candidate_list.index(candidate)
            vote_count_per_candidate[candidate_index] = vote_count_per_candidate[candidate_index] + 1
        else:
            #if candidate not found in candidate list, then append to the candidate list and 1 vote 
            candidate_list.append(candidate)
            vote_count_per_candidate.append(1)
        
        
    #Variables
    vote_percentage = 0
    max_votes = vote_count_per_candidate[0]
    index = 0
    percentage = []

    for i in range(len(candidate_list)):

        #getting the percentage 
        vote_percentage = round((vote_count_per_candidate[i])/total_votes*100,2)
        percentage.append(vote_percentage)
  
    # Finding the maximum votes to determine the election winner
    max_votes = max(vote_count_per_candidate)
    index = vote_count_per_candidate.index(max_votes)   

    # Election winner
    election_winner = candidate_list[index]


    # Print to the terminal
    print(" ")
    print("Election results")
    print("-----------------------------------------------")
    print("Total votes" + ":" + " " + str(total_votes)) 
    print("-----------------------------------------------")
    for i in range(len(candidate_list)):
        print(candidate_list[i] + " " + str(percentage[i]) + "%" + " " + "(" + str(vote_count_per_candidate[i]) + ")" )
    print("-----------------------------------------------")
    print("Winner" + ":" + " " + (election_winner))  
    print(" ")


#Specify the file to write to and initialize txt.writer
txt_file = open("election_results.txt", "w")
      
#writting out the results to a text file 
txt_file.write("Election Results")
txt_file.write("\n")
txt_file.write("-------------------------------------------------------")
txt_file.write("\n")
txt_file.write("Total Votes:" + " " + str(total_votes))
txt_file.write("\n")
txt_file.write("-------------------------------------------------------")
txt_file.write("\n")
for i in range(len(candidate_list)):
        txt_file.write(candidate_list[i] + " " + str(percentage[i]) + "%" + " " + "(" + str(vote_count_per_candidate[i]) + ")" )
txt_file.write("\n")
txt_file.write("-------------------------------------------------------")
txt_file.write("\n")
txt_file.write("Winner:" + " " + election_winner.upper())
txt_file.write("\n")
txt_file.close()
