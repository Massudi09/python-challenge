import os
import csv
from collections import Counter



# path to gather data from
PyPollCSV = '/Users/zeinabmassudi/Desktop/election_data.csv'

# TOTAL VOTES CALCULATIONS
# Read in the CSV file
with open(PyPollCSV, 'r') as csvfile:

    # Separate data by comma
    csvreader = csv.reader(csvfile, delimiter=',')

    # Set total vote volume value (row count)
    rowsNum = 0 

    # Parse through the data using for loop
    for i in csvreader:
        
        # add 1 to total votes count
        rowsNum += 1 

    #print title and total vote count
    print(" ")
    print("Elections Results")
    print("---------------------------")
    print (f"Total Votes: {rowsNum}")
    print("---------------------------")

# CANDIDATE RESULTS
# Read in the CSV file
with open(PyPollCSV, 'r') as csvfile:

    # Separate data by comma
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # set Counter module as counts
    counts = Counter()

    # set totalVotes volume to enable percentage count
    totalVotes = 0

    # loop through file and count...
    for num, row in enumerate(csvreader):

        # if a value occures at least once
        if num > 0:

            # ...add to candidate name count
            counts[row[2]] += 1

            # ..add to totalVotes count
            totalVotes += 1

    # loop through counted items     
    for candidate in counts.items():

        # print election results by candidate (candidate name, percentage, votes volume )
        print(f"{candidate[0]} : {candidate[1] / totalVotes * 100:.2F}% ({candidate[1]})")

# WINNER CALCULATION
# Read in the CSV file  
with open(PyPollCSV, 'r') as csvfile:

    # Separate data by comma
    csvreader = csv.reader(csvfile, delimiter=',')

    # set colum as location of candidate name
    column = (row[2] for row in csvreader)
    winner = Counter(column).most_common(1)
    
    # print delimiters
    print("---------------------------")

    # print name of candidate only
    print(f"Winner: {winner[0][0]}")

    #print delimiter
    print("---------------------------")

# WRITING TEXT FILE
# Create and open text file
with open("PyPoll.txt","w") as output:

    # define and add each line to be added to text file
    line1 = ""
    line2 = "Election Results"
    line3 = "-----------------------------"
    line4 = f"Total Votes: {rowsNum}"
    line5 = "-----------------------------"
    line6 = f"{candidate[0]} : {candidate[1] / totalVotes * 100:.2F}% ({candidate[1]})"
    line7 = "-----------------------------"
    line8 = f"Winner: {winner[0][0]}"
    line9 = "-----------------------------"

    # add new line after each line is added
    output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7,line8,line9))
    
