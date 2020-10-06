# Data we need to retrieve
# 1. Total number of votes cast
# 2. Complete list of candidates who received votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidate won\
# 5. Winner of the election based on popular vote

import csv
import os
# Assign a variable to load a file from the path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize total vote counter
total_votes = 0

# Candidate options and votes
candidate_options = []
candidate_votes = {}

# Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read in the header row
    headers = next(file_reader)

    # Print each row in the csv file
    for row in file_reader:
        # Add to total vote count
        total_votes += 1
        # Get candidate name from each row
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            # Add candidate to list
            candidate_options.append(candidate_name)
            # Begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add to candidate's vote count
        candidate_votes[candidate_name] += 1

    # Save results to text file
    with open(file_to_save, "w") as txt_file:
        # Print final vote count to terminal
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end="")
        # Write results to text file
        txt_file.write(election_results)

        # Track winning candidate, votes, and percentage
        winning_candidate = ""
        winning_count = 0
        winning_percentage = 0

        for candidate_name in candidate_votes:
            # Retrieve vote count
            votes = candidate_votes[candidate_name]
            # Calculate percentage
            vote_percentage = float(votes) / float(total_votes) * 100
            # Print results
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            # Write to text file
            txt_file.write(candidate_results)

            # Determine if votes are greater than winnning count
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # Update winning info
                winning_candidate = candidate_name
                winning_count = votes
                winning_percentage = vote_percentage
    
        # Print winning candidate, vote count, and percentage
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)




