# import modules / dependencies
import os           #os to join elements of the file path for PC
import csv          #read csv file using .reader method

csv_file_path = os.path.join(".","Resources","election_data.csv")
print(csv_file_path)

#Initiate Variables
Total_Votes = 0
Khan_Votes = 0
Khan_Percent = 0
Correy_Votes = 0
Correy_Percent = 0
Li_Votes = 0
Li_Percent = 0
Tooley_Percent = 0
Tooley_Votes = 0

#Open and read the csv_file called election_data.csv
with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")

    #Read the header
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    #Read through each row of data after the header
    for row in csv_reader:

        #Increase Total_Votes by 1
        Total_Votes = Total_Votes + 1

print()

#Create Summary Table
output=(
    f"Election Results\n"
    f"-------------------------------------\n"
    f"Total Votes: {Total_Votes}\n"
    f"-------------------------------------\n"
    f"Khan: {Khan_Percent}% ({Khan_Votes})\n"
    f"Correy: {Correy_Percent}% ({Correy_Votes})\n"
    f"Li: {Li_Percent}% ({Li_Votes})\n"
    f"O'Tooley: {Tooley_Percent}% ({Tooley_Votes})\n"
    f"-------------------------------------\n"
    f"Winner: \n"
    f"-------------------------------------\n"
)

print(output)

# Specify the file to write to
output_path = os.path.join(".", "Analysis","Results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(output)