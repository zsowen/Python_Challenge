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
accum_change = 0
prev_month = 0
current_change = 0

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
        #Check if current month is the first month
        if total_months <= 1:
            #Advance previous month value to current row
            prev_month = int(row[1])

        else:
            #Calculate current_change as row[1] - the previous months row[1]
            current_change = int(row[1])-prev_month
            
            #Calculate accum_change by adding the current_change value
            accum_change += current_change

            #Advance previous month value to current row
            prev_month = int(row[1])
        
        #use conditional to see if current change is greater than greatest_increase
        if current_change > int(greatest_increase[1]):
            #if greater than replace current values in greatest_increase
            greatest_increase = [row[0], current_change]
        
        #use conditional to see if current change is less than greatest_decrease
        elif current_change < int(greatest_decrease[1]):
            #if less than replace current values in greatest_decrease
            greatest_decrease = [row[0], current_change]
        
        else:
            continue 

        #--------------------------------------        
        

#Calculate average_change = total change/(total months-1)
average_change = round(accum_change/(total_months-1),2)

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

# Specify the file to write to
output_path = os.path.join(".", "Analysis","Results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(output)
    # csvwriter.writerow(["Financial Analysis"])
    # csvwriter.writerow(["----------------------------"])
    # csvwriter.writerow(["Total Months: {total_months}"])
    # csvwriter.writerow(["Total: {total}"])
    # csvwriter.writerow(["Average Change: {average_change}"])
    # csvwriter.writerow(["Greatest Increase in Profits: {greatest_increase}"])
    # csvwriter.writerow(["Greatest Decrease in Profits: {greatest_decrease}"])
