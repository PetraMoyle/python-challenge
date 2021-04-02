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

    #print(csv_reader)

    # Read & print the header row 
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
    month_list = []

    # # Read each row of data after the header
    for row in csv_reader:
    #     #print(row)

    #     # Append/hold the total months and total profit/loss
         total_months = total_months + 1
         total_net = total_net + int(row[1])
         changes = int(row[1]) - profit_loss
         month_list.append(row[0]) 

         #reset profit loss
         profit_loss = int(row[1])

         #attach changes in a list 
         changes_list.append(changes)
  

    # # Calculate the average 
    average_change = round(sum(changes_list)/len(changes_list),2)

    # # Calculating the greatest increase and the greatest decrease
    the_greatest_increase = (max(changes_list)) 
    the_greatest_decrease = (min(changes_list))

    max_month = month_list[changes_list.index(the_greatest_increase)] 
    min_month = month_list[changes_list.index(the_greatest_decrease)]

  
    print("Financial Analysis")
    print('----------------------------------------')
    print("Total Months:" + " " + str(total_months))
    print("Average Change:" + " " + "$" + str(average_change))
    print("Greatest Increase in Profits:" + " " + max_month + " " + str(the_greatest_increase))
    print("Greatest Decrease in Profits:" + " " + min_month + " " + str(the_greatest_decrease))


# Specify the file to write to
Analysis = os.path.join("Resources", "analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(Analysis, 'w') as txt_writer:

    # txt_writter = txt_writer (txt_file, delimeter=',')

    Analysis.write(["Financial Analysis"])
    txt_writer.write("-------------------------------------------------------\n")
    txt_writer.write("Total months" + ":" + "" + str(len(total_months)))
    txt_writer.write("\n")
    txt_writer.write("Average Change:" + " " + "$" + str(average_change))
    txt_writer.write("\n")
    txt_writer.write("Greatest Increase in Profits" + ":" + " " + "$" + max_month + str(the_greatest_increase))
    txt_writer.write("\n")
    txt_writer.write("Greatest Decrease in Profits" + ":" + " " + "$" + min_month + str(the_greatest_decrease))
    txt_writer.write("\n")
   

    # file.write("Financial Analysis")
    # file.write("----------------------------")
    # file.write(f"Total Months: {len(total_months)}")
    # file.write(f"Total: ${sum(total_profit)}")
    # file.write(f"Average Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    # file.write("\n")
    # file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")
    # file.write("\n")
    # file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")