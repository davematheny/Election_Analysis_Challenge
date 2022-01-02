# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
#Step 1: Country list and voted dictionary
county_list = []
county_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Step 2: Track the winning country, vote count, and percentage.
winning_county = ""
winning_county_votes = 0
winning_county_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        #Step 3: Get the county name from each row.
        county_name = row[1]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

        #Step 4a: Write a decision statement with a logical operator to check if the county name acquired in Step 3 is in the county list you created in Step 1
        if county_name not in county_list:

            #Step 4b: If the county is not in the list created in Step 1, add it to the list of county names
            county_list.append(county_name)

            #Step 4c: Write a script that initializes the county vote to zero, like you did when you began to track the vote counts for the candidates.
            county_votes[county_name] = 0

        #Step 5: Write a script that adds a vote to the county’s vote count as you are looping through all the rows
        county_votes[county_name] += 1
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # After opening the file print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")
    # After printing the final vote count to the terminal save the final vote count to the text file.
    txt_file.write(election_results)

    #Step 6a: Write a repetition statement to get the county from the county dictionary.
    for county_name in county_votes :

        #Step 6b: Initialize a variable to hold the county’s votes as they are retrieved from the county votes dictionary.
        countyvotes = county_votes.get(county_name)
        #Step 6c: Write a script that calculates the county’s votes as a percentage of the total votes.
        countyvotespercentage = float(countyvotes) / float(total_votes) * 100

        #Step 6d: Write a print statement that prints the current county, its percentage of the total votes, and its total votes to the command line.
        county_results = (
            f"{county_name}: {countyvotespercentage:.1f}% ({countyvotes:,})\n")
        print (county_results)
        #Step 6e: Write a script that saves each county, the county’s total votes, and the county’s percentage of total votes to the election_results.txt file
        txt_file.write(county_results)
        #Step 6f: Write a decision statement that determines the county with the largest vote count and then adds that county and its vote count to the variables created in Step 2
        if (countyvotes > winning_county_votes) and (countyvotespercentage > winning_county_percentage):
            winning_county_votes = countyvotes
            winning_county = county_name
            winning_county_percentage = countyvotespercentage

    #Step 7: Write a print statement that prints out the county with the largest turnout.
    winning_county_summary = (
        f"\n----------------------------------------\n" 
        f"Largest County Turnout: {winning_county}\n"
        f"----------------------------------------\n" )
    print(winning_county_summary)

    #Step 8: Write a script that saves the county with the largest turnout to the election_results.txt file.
    txt_file.write(winning_county_summary)

    for candidate_name in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)