# program that completes the following in Python3:
# 1) counts the total number of votes
# 2) prints a complete list of candidates who received votes
# 3) calculates the percentage of votes each candidate won
# 4) prints the total number of votes each candidate won
# 5) prints the winner of the election based on the popular vote
# 6) print results to txt

# uses a csv file named Candidate_Votes.csv
# import needed modules
import csv

# Reformat the data a little
data = open('Z:\TCC_Data_Analytics\Module_3_Python\PyPoll\Resources\election_data.csv')
data = [i for s in data for i in s.split(',')]
fields = len(data) - 1

# create empty lists to separate the columns into
ID = []
County = []
Candidate = []
n=0
while n < fields: 
    ID.append(data[n])
    County.append(data[n+1])
    Candidate.append(data[n+2].replace("\n",""))
    n=n+3

print("Election Results")
print("-------------------------------")

# 1) counts the total number of votes
total_votes = len(ID)-1
print(f"Total Votes: {total_votes}")
print("-------------------------------")

# 2) sets a complete list of unique candidates who received votes
cands = list(set(Candidate[1:]))

# 3) calculates the percentage of votes each candidate won
# find the number of votes for each candidate
can1 = Candidate[1:].count(cands[0])
can2 = Candidate[1:].count(cands[1])
can3 = Candidate[1:].count(cands[2])

# calculate the percentage of votes each received and print it to the screen
can1per = int(can1/total_votes*100)
can2per = int(can2/total_votes*100)
can3per = int(can3/total_votes*100)

print(f"{cands[0]}: {can1per}% ({can1})")
print(f"{cands[1]}: {can2per}% ({can2})")
print(f"{cands[2]}: {can3per}% ({can3})")
print("-------------------------------")

# 5) prints the winner of the election based on the popular vote
# create a variable that determines the winner of the popular vote and set winner variable
def winner():
    if can1 > can2:
        if can1 > can3:
            print(f"Winner: {cands[0]}")
            return cands[0]
        if can1 < can3:
            print(f"Winner: {cands[2]}")
            return cands[2]
    else:
        print(f"Winner: {cands[1]}")
        return cands[1]
winner = winner()
print("-------------------------------")



#6) print results to txt
results_file = "Z:\TCC_Data_Analytics\Module_3_Python\PyPoll\Analysis\pypoll_output.txt"
with open(results_file, 'w', newline='',) as file:
    file.write("Election Results\n")
    file.write("-------------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------------\n")
    file.write(f"{cands[0]}: {can1per}% ({can1})\n")
    file.write(f"{cands[1]}: {can2per}% ({can2})\n")
    file.write(f"{cands[2]}: {can3per}% ({can3})\n")
    file.write("-------------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------------")
