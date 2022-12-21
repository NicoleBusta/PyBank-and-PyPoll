# PyPoll Analysis

# total number of votes cast

# list of candidates, their percentage of votes and vote count

# winner

# add dependencies and file

import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

# set counter, list of candidates, candidate dictionary and winner
# dictionary key is candidate name, with value being their number of votes
total_votes = 0
candidate_avail = []
candidate_votes = {}
candidate_winner = ""

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",") 
    csvheader = next(csvfile)

    for row in csvreader:
        total_votes += 1

        candidate_name = row[2]
        if candidate_name not in candidate_avail:
            candidate_avail.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

    max_count = max(candidate_votes, key=candidate_votes.get)
    candidate_winner = max_count
    


#print outputs
print("Election Results")
print(" -------------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------------")
for candidate in candidate_votes:
    votes = candidate_votes.get(candidate)
    vote_percentage = float(votes) /  float(total_votes) * 100
    vote_percentage = round(vote_percentage, 3)
    print(candidate, " ", vote_percentage, "%", " ", votes)
print(f" ------------------------------")
print(f"Winner: {candidate_winner}")
print(f"------------------------------")


# write outcome to text file PyPoll Election Winner
PyPollElectionWinner = open("PyPollElectionWinner.txt","w")
 
PyPollElectionWinner.write("PyPoll Election Results\n")
PyPollElectionWinner.write("------------------------------\n")
PyPollElectionWinner.write(f"Total Votes: {total_votes}\n")
PyPollElectionWinner.write(f"-----------------------------\n")
for candidate in candidate_votes:
    votes = candidate_votes.get(candidate)
    vote_percentage = float(votes) /  float(total_votes) * 100
    vote_percentage = round(vote_percentage, 3)
    PyPollElectionWinner.write(candidate + " "+ str(vote_percentage) + "%" + " " + str(votes) + "\n" )
PyPollElectionWinner.write(f" ----------------------------\n")
PyPollElectionWinner.write(f"Winner: {candidate_winner}\n")
PyPollElectionWinner.write(f"-------------------------------")
 
PyPollElectionWinner.close()
