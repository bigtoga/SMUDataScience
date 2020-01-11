# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `Profit/Losses`

# Your task is to create a Python script that analyzes the records to calculate each of the following:
  # The total number of months included in the dataset
  # The net total amount of "Profit/Losses" over the entire period
  # The average of the changes in "Profit/Losses" over the entire period
  # The greatest increase in profits (date and amount) over the entire period
  # The greatest decrease in losses (date and amount) over the entire period
# As an example, your analysis should look similar to the one below:

#   ```text
#   Financial Analysis
#   ----------------------------
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)
#   ```

# Lastly print the analysis to the terminal and export a text file with the results.
#PyBank/Resources/budget_data.csv
import os
import csv

# Path to collect data from the Resources folder
rel_path = "Resources/budget_data.csv"
script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
csvFile = os.path.join(script_dir, rel_path)
logFile = os.path.join(script_dir, "PyBank output.txt")

total_months = 0        # The total number of months included in the dataset
total = 0.00            # The net total amount of "Profit/Losses" over the entire period
avg_change = 0.00       # The average of the changes in "Profit/Losses" over the entire period
avg_change_first = 0.00
avg_change_last = 0.00
greatest_inc = 0.00     # The greatest increase in profits (date and amount) over the entire period
greatest_dec = 0.00     # The greatest decrease in losses (date and amount) over the entire period
prev_month_val = 0.00
this_month = "Set in code"
greatest_inc_month = "Set in code"
greatest_dec_month = "Set in code"

# Read in the CSV file
with open(csvFile, 'r') as csvfile:
    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Loop through the data
    for row in csvreader:
        total_months += 1
        currVal = row[1]
        this_month = row[0]

        total += float(currVal)
        avg_change_last = float(currVal) # always overwrite so "last row value" is persisted

        if total_months == 1:
            avg_change_first = float(currVal)

        change = float(currVal) - prev_month_val
        if change > greatest_inc:
            greatest_inc = change
            greatest_inc_month = this_month

        if change < greatest_dec:
            greatest_dec = change
            greatest_dec_month = this_month

        # assign so the next row will be able to compare it's currVal to this one:
        prev_month_val = float(currVal)

avg_change = (avg_change_last - avg_change_first) / (total_months - 1)
sep = ''.join(['-' * 20])
output = f'''

Financial Analysis
{sep}
Total Months: {total_months}
Total: ${int(total)}
Average  Change: ${str(round(avg_change, 2))}
Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc})
Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec})
{sep}

'''
print(output)
#   Total Months: 86
#   Total: $38382578
#   Average  Change: $-2315.12
#   Greatest Increase in Profits: Feb-2012 ($1926159)
#   Greatest Decrease in Profits: Sep-2013 ($-2196167)

file1 = open(logFile, "w")
file1.write(output)
file1.close()