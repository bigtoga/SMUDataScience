# Your task is to create a Python script that analyzes the votes and calculates each of the following:
    # The total number of votes cast
    # A complete list of candidates who received votes
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    # The winner of the election based on popular vote.
# As an example, your analysis should look similar to the one below:
#   ```text
#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
#   ```
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
import os
import csv
from collections import Counter

cwd = os.getcwd()  # get current working dir: C:\\Users\\%USERPROFILE%\\Desktop
#print("My current working directory is: {} ".format(cwd))

# Path to collect data from the Resources folder
# script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in. YOU MUST RUN IN DEBUG MODE for this to work
script_dir = os.getcwd()
sourceFile = os.path.join(script_dir, "Resources/election_data.csv")
#sourceFile = os.path.join(script_dir, "Resources/smaller2.csv")
logFile = os.path.join(script_dir, "PyPoll output.txt")

total_votes = 0             # The total number of votes cast 
candidates = {}             # A complete list of candidates who received votes ("Candidate")
winner = ""                 # The winner of the election based on popular vote.

# Read in the CSV file
with open(sourceFile, 'r') as csvfile: # , newline="", encoding='utf-8'
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        total_votes += 1
        # Voter ID,County,Candidate
        voterId, county, candidate = row
        if candidate not in candidates:
            candidates[candidate] = 1 # 1 vote for the first row
        else:
            previous_votes = int(candidates[candidate])
            candidates[candidate] = previous_votes + 1



with open(logFile, "a") as myFile:
    sep = ''.join(['-' * 20])
    output = f'''

Election Results
{sep}
Total Votes: {total_votes}
{sep}
'''
    print(output)
    myFile.write(output)

    for key, value in candidates.items():
        votes = int(value)
        percVotes = votes / total_votes
        
        output = f'''
{key}: {"{:.3%}".format(percVotes)} ({value})'''
        print(output)
        myFile.write(output)
    
# s = sorted(candidates.items() , reverse=True, key=lambda x: x[1])
# list(my_dict.keys())[0]     -> key of "first" element
# list(my_dict.values())[0]   -> value of "first" element
# list(my_dict.items())[0]    -> (key, value) tuple of "first" element

    iterator = 0
    for w in sorted(candidates, key=candidates.get, reverse=True):
        iterator += 1
        if iterator == 1:
            # print(w, candidates[w])
            winner = w

    output = f'''
{sep}
Winner: {winner}
{sep}

'''
    print(output)
    myFile.write(output)

#   Election Results
#   -------------------------
#   Total Votes: 3521001
#   -------------------------
#   Khan: 63.000% (2218231)
#   Correy: 20.000% (704200)
#   Li: 14.000% (492940)
#   O'Tooley: 3.000% (105630)
#   -------------------------
#   Winner: Khan
#   -------------------------
