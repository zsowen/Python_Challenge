# import modules / dependencies
import os           #os to join elements of the file path for PC
import csv          #read csv file using .reader method

csv_file_path = os.path.join(".","Resources","election_data.csv")
print(csv_file_path)

#Initiate List & Dictionary
Candidate = []
Candidate_Votes = {}



#Open and read the csv_file called election_data.csv
with open(csv_file_path) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")

    #Read the header
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    #Read through each row of data after the header
    for row in csv_reader:

        #Create List for Candidate names & Dictionary for Candidate Vote Totals
        Candidate = row[2]

        if Candidate in Candidate_Votes.keys():

            Candidate_Votes[Candidate] +=1

        else:

            Candidate_Votes[Candidate] = 1

    # Specify the file to write to
    output_path = os.path.join(".", "Analysis","Results.txt")

    # Open the file using "write" mode. Specify the variable to hold the contents
    with open(output_path, 'w') as writer:

        #Calculate Total Votes
        Total_Votes = sum(Candidate_Votes.values())

        #Print first piece of results
        print(f"Election Results")
        writer.write(f"Election Results\n")

        print(f"-------------------------------")
        writer.write(f"-------------------------------\n")

        print(f"Total Votes: {Total_Votes}")
        writer.write(f"Total Votes: {Total_Votes}\n")

        print(f"-------------------------------")
        writer.write(f"-------------------------------\n")

        #Initiate List for Candidate Percentages
        Percent = []

        #Calculate percentages
        for i in Candidate_Votes:

            percent = round((Candidate_Votes[i]/Total_Votes)*100,2)
          
            print(f"{i}: {percent}% {Candidate_Votes[i]}")
            writer.write(f"{i}: {percent}% {Candidate_Votes[i]}\n")

        #Calculate the winner
        for key in Candidate_Votes.keys():

            if Candidate_Votes[key]==max(Candidate_Votes.values()):

                Winner = key

        #Print remainder of results
        print(f"-------------------------------")
        writer.write(f"-------------------------------\n")
        
        print(f"Winner: {Winner}")
        writer.write(f"Winner: {Winner}\n")

        print(f"-------------------------------")
        writer.write(f"-------------------------------\n")