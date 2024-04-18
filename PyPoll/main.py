import os
import csv
csvpath = os.path.join(os.getcwd(), "PyPoll","Resources", "election_data.csv")
# set variables
charless_votes = 0
dianad_votes = 0
raymond_votes = 0
total_votes = []
winner = []
candidate1 = "Charles Casper Stockham"
candidate2 = "Diana DeGette"
candidate3 = "Raymon Anthony Doane"
# total number of votes
total_votes = 0
# open csv file
with open(csvpath, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

#header row
    header = next(csv_reader)

    for row in csv_reader:   
        # Add to vote count
        total_votes += 1
        
        # update the candidate list
        if row[2] == "Charles Casper Stockham": 
            charless_votes +=1
        elif row[2] == "Diana DeGette":
            dianad_votes +=1
        elif row[2] == "Raymon Anthony Doane": 
            raymond_votes +=1
           
#candidate percent
charless_pct = round((charless_votes / total_votes) * 100, 3)
dianad_pct = round((dianad_votes / total_votes) * 100, 3)
raymond_pct = round((raymond_votes / total_votes) * 100, 3)

    #winner
    
if charless_votes > dianad_votes and charless_votes > raymond_votes:
    winner = candidate1
elif dianad_votes > charless_votes and dianad_votes > raymond_votes:
    winner = candidate2
else: winner = candidate3
#Displaying information

print("Election Results")
print("..............")
print(f"Total Votes:{(total_votes)}")
print("..............")
print(f"Charles Casper Stockham: {charless_pct}% ({charless_votes})")
print(f"Diana DeGette: {dianad_pct}% ({dianad_votes})")
print(f"Raymon Anthony Doane: {raymond_pct}% ({raymond_votes})")
print("..............")
print(f"Winner: {winner}")
print("..............")

# Exporting to .txt file
output = open("output.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {(total_votes)}")
line4 = str("--------------------------")
line5 = "Charles Casper Stockham: {charless_pct}% ({charless_votes})"
line6 = "Diana DeGette: {dianad_pct}% ({dianad_votes})"
line7 = "Raymon Anthony Doane: {raymond_pct}% ({raymond_votes})"
line8 = "--------------------------"
line9 = "--------------------------"
line10 = "Winner: {winner}"
line11 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line1, line2, line3,line4, line5, line6,line7, line8, line9,line10, line11))



