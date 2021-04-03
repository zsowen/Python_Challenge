# import modules / dependencies
import os           #os to join elements of the file path for PC
import csv          #read csv file using .reader method

csv_file_path = os.path.join(".","Resources","budget_data.csv")
print(csv_file_path)

#Initiate variables
total_months = 0
total = 0
average_change = 0
greatest_increase = ["",0]
greatest_decrease = ["",0]

#Open and read the csv_file called budget_data.csv
with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")

    #Read the header
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    #Read through each row of data after the header
    for row in csv_reader:
        
        #print(row[0],row[1])
        
        #increase total_months by 1
        total_months = total_months + 1

        #sum total Profit/Losses
        total += int(row[1])

        #Calculate the month to month change
        if total_months <= 1:
            continue

        else:
            print("Greater")



        #use conditional to see if current change is greater than greatest_increase
            #if greater than replace current values in greatest_increase

        #use conditional to see if current change is less than greatest_decrease
            #if less than replace current values in greatest_decrease

        #--------------------------------------
        
        #setup variables for next iteration

        #set prior_value = current_row

#Calculate total

#Calculate total change

#Calculate average_change = total change/(total months-1)

print()

# Create Summary Table
output=(
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: {total}\n"
    f"Average Change: {average_change}\n"
    f"Greatest Increase in Profits: {greatest_increase}\n"
    f"Greatest Decrease in Profits: {greatest_decrease}\n"
)

print(output)