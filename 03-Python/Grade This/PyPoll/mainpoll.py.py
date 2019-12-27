import os
import csv
#importing the file
election_data = os.path.join("Resources","election_data.csv")

#creating the file to store results in 
file_to_output = os.path.join("Resources","election_results.txt")

#box for totals
total_votes = 0

#candidate count
Candidates = []
#dictionary to put candidates in 
candidate_votes = {}

#vote count
Votes = []

#starts at 0 and keeps comparing candidates until
#  the greatest voteis reached
winning_candidate = ""
winning_count = 0


#opening the file
with open(election_data) as csvfile:
    #reading the file
    csvreader=csv.reader(csvfile)


    #get more clarification on this 
    csv_header = next(csvreader)

   

# count total number of votes by counting voter ID 
    for row in csvreader:
        total_votes = total_votes + 1
       

# sort the votes by candidate
# 	-run through and find each unique 	candidate
        candidate_name = row[2]
        #adding the unique candidates to the dictioary
        if candidate_name not in Candidates:
            Candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] +1

   # opening the file to write          
with open(file_to_output, "w") as txt_file:




    for candidate in candidate_votes:
        #getting the dictionary
        votes = candidate_votes.get(candidate)
        #percentages
        vote_percentage = float(votes) / float(total_votes) * 100

        #referring back to the top
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        #declaring what variables to write as a variable
        voter_output = f"{candidate}: {vote_percentage:.3f}%  ({votes})\n"
       #writing the variables
        txt_file.write(voter_output)



    #declaring what to write as a variable
    election_results = (
        f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n"
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
        f"-------------------------\n"
    )
    #writing it
    txt_file.write(election_results)



print (election_results)