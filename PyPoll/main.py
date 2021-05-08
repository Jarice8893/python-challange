import os
import csv

election_data = os.path.join("..", "election_data.csv")

with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    total_votes = 0
    khan = 0
    correy = 0
    li = 0
    otooley = 0

    for row in csv_reader:
        
        total_votes +=1

        if row[2] == "Khan":
            khan +=1
        elif row[2] == "Correy":
            correy +=1
        elif row[2] == "Li":
            li +=1
        elif row[2] == "O'Tooley":
            otooley +=1
    
    contestants = ["Khan", "Correy", "Li", "O'Tooley"]
    votes = [khan, correy, li, otooley]

    #dict_contestants_votes = dict(zip(contestants,votes))
    #winner = max(dict_contestants_votes, winner=dict_contestants_votes.get)

    khan_percent = (khan/total_votes) *100
    correy_percent = (correy/total_votes) *100
    li_percent = (li/total_votes) *100
    otooley_percent = (otooley/total_votes) *100

    print(f"Elections Results")
    print(f"-------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"-------------------------")
    print(f"Khan: {khan_percent:.3f}% ({khan})")
    print(f"Correy: {correy_percent:.3f}% ({correy})")
    print(f"Li: {li_percent:.3f}% ({li})")
    print(f"O'Tooley: {otooley_percent:.3f}% ({otooley})")
    print(f"-------------------------")
    print(f"Winner: Khan")
    print(f"-------------------------")
    
    output_file = os.path("python-challenge", "PyPoll", "Elections_Analysis.txt")

    with open(output_file,"w") as file:

            file.write(f"Elections Analysis")
            file.write("\n")
            file.write(f"-------------------")
            file.write("\n")
            file.write(f"Total Votes: {len(total_months)}")
            file.write("\n")
            file.write(f"-------------------------")
            file.write("\n")
            file.write(f"Khan: {khan_percent:.3f}% ({khan})")
            file.write("\n")
            file.write(f"Correy: {correy_percent:.3f}% ({correy})")
            file.write("\n")
            file.write(f"Li: {li_percent:.3f}% ({li})")
            file.write("\n")
            file.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley})")
            file.write("\n")
            file.write(f"-------------------------")
            file.write("\n")
            file.write(f"Winner: {winner}")
            file.write("\n")
            file.write(f"-------------------------")