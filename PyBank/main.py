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

    print(csv_reader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csv_reader)
    print(f"CSV Header: {csv_header}")

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
         profit_loss = int(row[1])
         changes_list.append(changes)
    
       # Obtain the greatest increase and the greatest decrease of the the montly change
         if changes > changes - 1
            the greatest_increase = changes
            changes - row[1]
            print(the_greatest_increase)


#We use the plus 1 at the end since month associated with change is the + 1 month or next month
# the_greatest_increase = monthly_profit_change.index(max(monthly_profit_change)) + 1
# the_greatest_decrease = monthly_profit_change.index(min(monthly_profit_change)) + 1 
    
    average_change = round(sum(changes_list)/len(changes_list),2)

    # the_greatest_increase = max(changes_list)
    # the_greatest_decrease = min(changes_list)

    print(total_months)
    print(total_net)
    print(average_change)

    

# # Analysis results - write out 
# import os
# import csv

# # Specify the file to write to
# output_path = os.path.join("..", "output", "new.csv")

# # Open the file using "write" mode. Specify the variable to hold the contents
# with open(output_path, 'w') as csvfile:

#     # Initialize csv.writer
#     csvwriter = csv.writer(csvfile, delimiter=',')

#     # Write the first row (column headers)
#     csvwriter.writerow(['First Name', 'Last Name', 'SSN'])

#     # Write the second row
#     csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])