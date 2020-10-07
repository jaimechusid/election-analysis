# Election Analysis

## Project Overview
In this project, I was asked by a Colorado Board of Elections employee to complete the election audit of a recent local congressional election. I was given the following tasks to do so.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.6, Visual Studio Code 1.49.3

## Summary
The analysis of the election shows that:
- There were 369,711 votes cast in the election.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes.
    
## Challenge Overview
The purpose of this challenge is to add county-specific data to the analysis conducted in the project above. While the initial project consisted of data on each candidate's vote and vote percentage, as well as the election outcome, this addition includes similar statistics for each county. I used congruent methods to calculate the total number of votes in each county, each county's vote percentage, and ultimately the county with the largest voter turnout. 

## Challenge Summary
The continued analysis of the election shows that:
- The county results were:
    - Jefferson had 10.5% of the votes and 38,855 total votes.
    - Denver had 82.8% of the votes and 306,055 total votes.
    - Arapahoe had 6.7% of the votes and 24,801 total votes.
- The county with the largest voter turnout was:
    - Denver, which accounted for 82.8% of the votes (306,055 total votes)
    
The output of the completed program is shown below:

![Results](results.png)

## Election-Audit Summary
Because of the structure of this script, the election commission should be able to use it for any election, with any number of votes, candidates, and counties. The code snippet below does not included any hard-coded values in terms of candidate or county, and will go through the data and add each new value accordingly, until the last row of the data.  

    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        if county_name not in counties:

            # Add the existing county to the list of counties.
            counties.append(county_name)

            # Begin tracking the county's vote count.
            county_votes[county_name] = 0
            
        # Add a vote to that county's vote count.
        county_votes[county_name] += 1
        
An adjustment that the election commission may need to make is in the lines that assign candidate_name and county_name based on the index in the CSV file. If the file is formatted differently, the indexes must be adjusted accordingly. If the file is in the same format, no adjustments in this code are necessary. Additionally, adjustments may need to occur in the case of a tie in the election. The code below only accounts for elections with no ties, and in the case of a tie, the first encountered candidate or county would be assumed as the "winner". I would suggest the election commission make an addition to account for this possible outcome.

    # Determining largest county turnout
    if votes > largest_county_votes:
            largest_county_votes = votes
            largest_county = county_name
            
    # Determining winning candidate
    if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    
