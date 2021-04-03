# import modules / dependencies
import os           #os to join elements of the file path for PC
import csv          #read csv file using .reader method

csv_file_path = os.path.join(".","Resources","election_data.csv")
print(csv_file_path)