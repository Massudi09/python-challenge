# DISCLAIMER : I know this method isn't the best, but that's the way I understand it for the time being

import os
import csv

# path to gather data from
PyBankCSV = '/Users/zeinabmassudi/Desktop/budget_data (1).csv'

# Read in the CSV file
with open(PyBankCSV, 'r') as csvfile:

    # separate data by comma
    csvreader = csv.reader(csvfile, delimiter=',')
    # set and skip header
    header = next(csvreader)
    
    # Set values for Revenue total(Profits/Losses), Month (row count) and Average Change 
    revenue = 0
    rowsNum = 0 
    averageChange = 0
    
    firstTime = True   

    # Parse through the data using for loop
    for i in csvreader:
        
        
        # add value to revenue
        revenue += int(i[1])

        # add one to row count
        rowsNum += 1   

        # AverageChange Calculations using if statement
        # If it's the first loop then....
        if firstTime:
            # set row as previous
            previous = int(i[1])
            firstTime = False
        else:
            # else set row as current
            current = int(i[1])

            # the difference between the two values represents the change
            difference = current - previous

            # divide by row count - 1 to get average change
            averageChange += (difference/85)

            # reset previous as current
            previous = current
         
    # print first part of results
    print(" ")
    print("Financial Analysis")
    print("---------------------------")
    print (f"Total Months: {rowsNum}")
    print(f"Total: ${revenue}")
    print(f"Average Change: ${averageChange:.2F}")

# MAX/MIN CHANGE VALUE CALCULATIONS
# The folowing scripts wouldn't run before or after another statement withough causing massive damage to my output 

# Parse through the data using for loop
with open(PyBankCSV) as csvfile:

    # separate data by comma, set and skip header
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  

    # find max value using max&lambda key funtions
    maxValue = max(csvreader, key=lambda column: int(column[1]))
    # print result 
    print("Greatest increase in Profits:" + str(maxValue).strip('[]'))

with open(PyBankCSV) as csvfile:
    # separate data by comma, set and skip header
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)  

    # find in value using max&lambda key funtions
    minValue = min(csvreader, key=lambda column: int(column[1]))
    # print result 
    print("Greatest increase in Profits:" + str(minValue).strip('[]'))

# WRITING TEXT FILE
# Create text file
with open("PyBank.txt","w") as output:

    # define each line to be added to text file
    line1 ="Financial Analysis"
    line2 = "---------------------------"
    line3 = f"Total Months: {rowsNum}"
    line4 = f"Total: ${revenue}"
    line5 = f"Average Change: ${averageChange:.2F}"
    line6 = "Greatest increase in Profits:" + str(maxValue).strip('[]')
    line7 = "Greatest increase in Profits:" + str(minValue).strip('[]')
    
    # add new line after each line is added
    output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
   
