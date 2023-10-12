import os
import csv

election_data = os.path.join("..","Resources","election_data.csv")
#import data from 'election_data.csv from resources folder


totalVotes = 0
candidateVotes = {}
#declare variables to store data
#assign initial value of 'totalVotes' to 0

#'r'ead the csv file 
with open("election_data.csv", "r") as file:
    next(file)
    #use to bypass first row with header info
    
    for line in file:
        voterID, county, candidate = line.strip().split(",")
        #use to pull info from the csv file, and split them at the comma
        
        totalVotes += 1
        #count and store the 'totalVotes'
        
        if candidate in candidateVotes:
            candidateVotes[candidate] += 1
        else:
            candidateVotes[candidate] = 1
        #count 'candidateVotes' for each 'candidate'

# Find the winning candidate and their vote count
winningCandidate = max(candidateVotes, key=candidateVotes.get)
maxVotes = candidateVotes[winningCandidate]
#find the 'winningCandidate' and their 'candidateVotes'


#print the election results to the terminal
print("Election Results")
print("-" * 20)
print(f"Total Votes: {totalVotes}")
print("-" * 20)
for candidate, votes in candidateVotes.items():
    percentage = (votes / totalVotes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print("-" * 20)
print(f"Winner: {winningCandidate}")
print("-" * 20)

#export the election results to a .txt file called 'electionResults.txt'
with open("electionResults.txt", "w") as outputFile:
    outputFile.write("Election Results\n")
    outputFile.write("-" * 20 + "\n")
    outputFile.write(f"Total Votes: {totalVotes}\n")
    outputFile.write("-" * 20 + "\n")
    for candidate, votes in candidateVotes.items():
        percentage = (votes / totalVotes) * 100
        outputFile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    outputFile.write("-" * 20 + "\n")
    outputFile.write(f"Winner: {winningCandidate}\n")
    outputFile.write("-" * 20 + "\n")
