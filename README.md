# Election_Analysis_Challenge
By David Matheny on 1/2/2021

## Overview of Election Audit:
The purpose of the election audit is to take in the results from election_results.csv to provide a terminal\text report of the results for audit purposes.  The results should be the total votes, votes by county, largest county turnout as well as votes by candidate(Winner and percentage).

## Election-Audit Results:
### How many votes were cast in this congressional election?
- 369,711 votes were cast in this congressional election.

### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
- Jefferson: 10.5% (38,855)
- Denver: 82.8% (306,055)
- Arapahoe: 6.7% (24,801)

### Which county had the largest number of votes?
- Denver

### Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
- Charles Casper Stockham: 23.0% (85,213)
- Diana DeGette: 73.8% (272,892)
- Raymon Anthony Doane: 3.1% (11,606)

### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
- Winner: Diana DeGette
- Winning Vote Count: 272,892
- Winning Percentage: 73.8%

### Images of results
- Terminal image
![Graph 1. Election Audit Results](Election_Analysis_Challenge/resources/TerminalOutput.png)

- Text file image
![Graph 2. Election Audit Results](Election_Analysis_Challenge/resources/TextFileOutput.png)

## Election-Audit Summary: 
I propose that we use the existing script to report beyond just the county\candidate scope.  I propose take in and report the results at a state or national level.  First we need to consolidate the data, instead of spreadsheets we should put the data into a database(possibly sql server\Azure, data is structured no need for Hadoop).  On a state or county level have the local officials conform their data so that each state and county is reporting their data in the same format(easier said than done).  We could setup a dynamic SSIS or datafactory pipeline to import all the spreadsheets per county(have a secure national drop FTP).  Once the data is loaded into SQL server would could modify our script by adding a python library to directly pull the data from SQL server instead of a csv.  We could then modify our script to include a state, so that it would have a state header to distinguish each state and the corresponding counties(states might have the same county names).  Or we could have this script be dynamic where it takes in a state and produces a report at the state level for each state(one report per state instead of one giant report).  Even easier would be since python is slow with data(even if you up the compute power) would be to use Power BI\Tableau to report directly from SQL server instead of a python script.  SQL server could handle any data scrubbing or check for any data quality.  Just a thought.
