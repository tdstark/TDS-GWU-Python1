import os
import pandas as pd

csvpath = os.path.join('.', 'Resources', 'election_data.csv')
electiondata = pd.read_csv(csvpath)

votesTotal = electiondata.shape[0]
khanIndex = electiondata.loc[electiondata["Candidate"] == "Khan"]
khanTotal = khanIndex.shape[0]
correyIndex = electiondata.loc[electiondata["Candidate"] == "Correy"]
correyTotal = correyIndex.shape[0]
liIndex = electiondata.loc[electiondata["Candidate"] == "Li"]
liTotal = liIndex.shape[0]
otooleyIndex = electiondata.loc[electiondata["Candidate"] == "O'Tooley"]
otooleyTotal = otooleyIndex.shape[0]
winnerIndex = electiondata['Candidate'].value_counts().to_frame()
winningCandidate = winnerIndex.index[0]
# winningCandidateTotal = winnerIndex.iloc[0,0]

totalVotesText = f"Total Votes: {votesTotal}"
khanText = f"Khan: {khanTotal / votesTotal:.3%} ({khanTotal})"
correyText = f"Correy: {correyTotal / votesTotal:.3%} ({correyTotal})"
liText = f"Li: {liTotal / votesTotal:.3%} ({liTotal})"
otooleyText = f"O'Tooley: {otooleyTotal / votesTotal:.3%} ({otooleyTotal})"
winnerText = f"Winner: {winningCandidate}"

print("Election Results")
print("------------------------------")
print(totalVotesText)
print("------------------------------")
print(khanText)
print(correyText)
print(liText)
print(otooleyText)
print("------------------------------")
print(winnerText)
print("------------------------------")

outputpath = os.path.join('.', 'analysis', 'poll_data.txt')
with open(outputpath, 'w') as txtfile:
    txtfile.write("Election Results \n")
    txtfile.write("------------------------------ \n")
    txtfile.write(totalVotesText + " \n")
    txtfile.write("------------------------------ \n")
    txtfile.write(khanText + " \n")
    txtfile.write(correyText + " \n")
    txtfile.write(liText + " \n")
    txtfile.write(otooleyText + " \n")
    txtfile.write("------------------------------ \n")
    txtfile.write(winnerText + " \n")
    txtfile.write("------------------------------ \n")