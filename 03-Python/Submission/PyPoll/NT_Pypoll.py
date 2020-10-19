import csv

csvPath= r"03-Python/Instructions/PyPoll/Resources/election_data.csv"
#print(csvPath)

#init total votes
totalVotes = 0

#init candidate counts
# correyCount = 0
# khanCount = 0
# liCount = 0
# otooleyCount = 0

candidateDict = {}

# read in the file
with open(csvPath, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # print(row)
        totalVotes += 1
        #print(totalVotes)
    
        candidate = row[2]
        if candidate in candidateDict.keys():
            candidateDict[candidate] += 1
        else:
            candidateDict[candidate] = 1
        winner = max(candidateDict, key=candidateDict.get)
        #print(winner)
    
        # Create Dict for candidates
        percentDict = {}
        for key in candidateDict.keys():
            percentEach = candidateDict[key]/ totalVotes
            percentDict[key] = percentEach
        #print(percentDict)

# create our list of text to write out - per candidate
listOfStrings = []
for key in percentDict.keys():
    myString = key + ": " + str(round(percentDict[key], 3) * 100) + "% (" + str(candidateDict[key]) + ")"
    listOfStrings.append(myString)

print(listOfStrings)

finalString = "\n".join(listOfStrings)

summaryString = f"""Election Results
-------------------------
Total Votes: {totalVotes}
-------------------------
{finalString}
-------------------------
Winner: {winner}
-------------------------"""
print(summaryString)

#write summary string
with open("nt_poll_results.txt", "w") as file1:
    file1.write(summaryString)
