import csv

csvPath= r"03-Python/Instructions/PyBank/Resources/budget_data.csv"
#print(csvPath)

#init total votes
totalMonths = 0
totalProfit = 0

lastRowProfit = 0

# read in the file
with open(csvPath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:

        #row[0] = Month-Year
        #row[1] = Profit/Loss

        totalMonths += 1
        totalProfit += int(row[1])

    #find the average changes
    average_change = []

    for row in range(1,len(row[1]))
        average_change.append((int(row,row[1])-int(row-1,row[1]))

    average_change = sum(average_change)/len(average_change)
    ptint(average_change)

        # if first row, do nothing, but set lastRowProfit
        #otherwise, get the change
        #row - last row profit
        # add to dictionary with month as the key
        # update last row profit
        #continue loop

print(totalMonths)
print(totalProfit)
