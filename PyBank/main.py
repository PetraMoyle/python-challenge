# Module for the file path
import os
directory = os.path.dirname(__file__)

# Module for reading CSV files
import csv
budget_data = os.path.join(directory,'Resources', 'budget_data.csv')

# open/read the file
with open(budget_data) as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Read & print the header row 
    csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")

    #Variables
    total_months = 1

    #skipping the first row
    first_row = next(csv_reader)

    total_net = int(first_row[1])    
    profit_loss = int(first_row[1])
    changes = 0
    the_greatest_increase = 0
    the_greatest_decrease = 0

    #list
    changes_list = []

    # # Read each row of data after the header
    for row in csv_reader:
    #     #print(row)

    #     # Append/hold the total months and total profit/loss
         total_months = total_months + 1
         total_net = total_net + int(row[1])
         changes = int(row[1]) - profit_loss

         #reset profit loss
         profit_loss = int(row[1])

         #attach changes in a list 
         changes_list.append(changes)
  

    # Calculate the average 
    average_change = round(sum(changes_list)/len(changes_list),2)

    # Calculating the greatest increase and the greatest decrease
    the_greatest_increase = changes_list.index(max(changes_list)) 
    the_greatest_decrease = changes_list.index(min(changes_list))
        
    # the_greatest_increase = max(changes_list)
    # the_greatest_decrease = min(changes_list)

# print to the terminal 
# print

# print('----------------------------------------')
# print("Total Months:" + " " + str(total_months))
# print("Average Change:" + " " + "str($)" + "(average_change)")"
# print("Greatest Increase in Profits:" + " " + "?month?" + "str($)" + (the_greatest_increase))
# print("Greatest Decrease in Profits:" + " " + "?month?" + "str($)" + (the_greatest_decrease))

# # Specify the file to write to
# Analysis = os.path.join( "output", "analysis.csv")

# # Open the file using "write" mode. Specify the variable to hold the contents
#with open(Analysis, 'w') as csv_file:

    #Initialize txt.writter
    #csv_writter = csv.writer (csv_file, delimeter=',')

    #Results exported to the text file 
    # cvs_writter.writerow("Financial Analysis\n")
    # cvs_writter.writerow("-------------------------------------------------------\n")
    # cvs_writter.writerow("Total months" + ":" + "" + str(len(total_months)))
    # cvs_writter.writerow("\n")
    # cvs_writter.writerow("Average Change:" + " " + "str($)" + str(average_change))
    # cvs_writter.writerow("\n")
    # cvs_writter.writerow("Greatest Increase in Profits" + ":" + " " + "str($)" + ?month + ?str(the_greatest_increase))
    # cvs_writter.writerow("\n")
    # cvs_writter.writerow("Greatest Decrease in Profits" + ":" + " " + "str($)" + ?month + ?str(the_greatest_decrease))
    # cvs_writter.writerow("\n")
   