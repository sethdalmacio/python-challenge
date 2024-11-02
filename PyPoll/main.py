import csv

file_path = "/Users/ylsstudent/Documents/Data_Analytics_Bootcamp/Module_3_Python/python-challenge/PyPoll/Resources/election_data.csv"

total_votes = 0
vote_counts = {}

with open(file_path, mode = "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    for row in csv_reader:
        total_votes += 1
        candidate = row[2]
        if candidate in vote_counts:
            vote_counts[candidate] += 1
        else:
            vote_counts[candidate] = 1

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

winner = None
max_votes = 0

for candidate, votes in vote_counts.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
   
    if votes > max_votes:
        max_votes = votes
        winner = candidate


print("-------------------------")
print(f"Winner: {winner}")

output_path = "/Users/ylsstudent/Documents/Data_Analytics_Bootcamp/Module_3_Python/python-challenge/PyPoll/Analysis/PyPoll_Analysis.txt"

with open(output_path, mode = "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")

    output_file.write(f"{list(vote_counts.keys())[0]}: {((vote_counts[list(vote_counts.keys())[0]] / total_votes) * 100):.3f}% ({vote_counts[list(vote_counts.keys())[0]]})\n")
    output_file.write(f"{list(vote_counts.keys())[1]}: {((vote_counts[list(vote_counts.keys())[1]] / total_votes) * 100):.3f}% ({vote_counts[list(vote_counts.keys())[1]]})\n")
    output_file.write(f"{list(vote_counts.keys())[2]}: {((vote_counts[list(vote_counts.keys())[2]] / total_votes) * 100):.3f}% ({vote_counts[list(vote_counts.keys())[2]]})\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")