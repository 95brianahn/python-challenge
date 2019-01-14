#import dependencies
import os
import csv

#file loading and output
file_to_load = "election_data.csv"
file_to_output = "election_data_analysis.txt"

#vote counter
total_votes = 0

#candidate options & their vote
candidate_options = [0]
candidate_votes = {}

#winning vote tracker
winning_candidate = ""
winning_count = 0

#csv read
with open(file_to_load) as election_data:
    reader = csv.DictReader(election_data)

    for row in reader:
        #total vote count
        total_votes = total_votes + 1
        #candidate name
        candidate_name = row["Candidate"]
        if candidate_name not in candidate_options
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
#printing results and saving the data as a text file
with open(file_to_output, "w") as txt_file:
    #print final vote count
    election_results = (
    f"\n Election Results \n"
    f"-----------------------\n"
    f"Total Votes: {total_votes}\n"
    )
    print(election_results)

    #saving it as a text file
    txt_file.write(election_results)

    #find winner by looping it through the counts
    for candidates in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes) / float(total_votes) * 100

    if (votes > winning_count):
        winning_count = votes
        winning_candidate = candidate

    voter_output = f"(candidate): {vote_percentage:.3f}% ({votes})\n"
    print(voter_output)

    #save it in text file
    txt_file.write(voter_output)

    #printing winner candidate
winning_candidate_summary = (
    f"----------------\n"
    f"Winner: {winning_candidate}\n"
    f"----------------]\n"
)

print(winning_candidate_summary)
txt_file.write(winning_candidate_summary)
