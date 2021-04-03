# Module for the file path
import os
directory = os.path.dirname(__file__)

# Module for reading CSV files
import csv
budget_data = os.path.join(directory,'Resources', 'budget_data.csv')

# Open/read the file
with open(budget_data) as csv_file:

    # CSV reader specifies delimiter and variable that holds contents
    csv_reader = csv.reader(csv_file, delimiter=',')

    # Read & skip the header row 
    csv_header = next(csv_reader)

    # Variables
    total_months = 1

    # Skipping the first row
    first_row = next(csv_reader)

    total_net = int(first_row[1])    
    profit_loss = int(first_row[1])
    changes = 0
    the_greatest_increase = 0
    the_greatest_decrease = 0

    # Lists
    changes_list = []
    month_list = []

    # Read each row of data after the header
    for row in csv_reader:

         # Append/hold the total months and total profit/loss
         total_months = total_months + 1
         total_net = total_net + int(row[1])
         changes = int(row[1]) - profit_loss
         month_list.append(row[0]) 

         # Reset profit loss
         profit_loss = int(row[1])

         # Attach changes in a list 
         changes_list.append(changes)
  
    # Calculate the average 
    average_change = round(sum(changes_list)/len(changes_list),2)

    # Calculating the greatest increase and the greatest decrease
    the_greatest_increase = (max(changes_list)) 
    the_greatest_decrease = (min(changes_list))

    max_month = month_list[changes_list.index(the_greatest_increase)] 
    min_month = month_list[changes_list.index(the_greatest_decrease)]


    # Prin to the Terminal 
    print(" ")
    print("Financial Analysis")
    print('----------------------------------------')
    print("Total Months:" + " " + str(total_months))
    print("Total:" + " " + "$" + str(total_net))
    print("Average Change:" + " " + "$" + str(average_change))
    print("Greatest Increase in Profits:" + " " + max_month + " " + "(" + "$" + str(the_greatest_increase) + ")")
    print("Greatest Decrease in Profits:" + " " + min_month + " " + "(" + "$" + str(the_greatest_decrease) + ")")
    print('----------------------------------------')
    print(" ")


#Specify the file to write to and initialize txt.writer
txt_file = open("analysis.txt", "w")    

txt_file.write("Financial Analysis")
txt_file.write("\n")
txt_file.write("-------------------------------------------------------")
txt_file.write("\n")
txt_file.write("Total months:" + " " + str(total_months))
txt_file.write("\n")
txt_file.write("Total:" + " " + "$" + str(total_net))
txt_file.write("\n")
txt_file.write("Average Change:" + " " + "$" + str(average_change))
txt_file.write("\n")
txt_file.write("Greatest Increase in Profits:" + " " + max_month + " " + "(" + "$" + str(the_greatest_increase) + ")" )
txt_file.write("\n")
txt_file.write("Greatest Decrease in Profits:" + " " + min_month + " " + "(" + "$" + str(the_greatest_decrease) + ")" )
txt_file.write("\n")
txt_file.close()
   
