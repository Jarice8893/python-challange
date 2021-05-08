
import os
import csv

#budget_data = os.path.join("C:\Users\jmarshall.000\Desktop\nu-chi-data-pt-04-2021-u-c\02-Homework\03-Python\Instructions\PyBank")

#budget_data = os.path.join("..\Resources\budget_data.csv")

#budget_data = os.path.join("..", "Resources", "budget_data.csv")

#budget_data = os.path.join("..", "python-challange", "budget_data.csv")

budget_data = os.path.join("..", "budget_data.csv")

with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

    total_months = []
    total_amount = []
    total_amount_change = []

    for row in csv_reader:
        
        total_months.append(row[0])
        total_amount.append(int(row[1]))

        #print(len(total_months))

    for i in range(len(total_amount)-1):

        total_amount_change.append(total_amount[i+1]-total_amount[i])

        max_value = max(total_amount_change)
        min_value = min(total_amount_change)

        max_value = total_amount_change.index(max(total_amount_change)) + 1
        min_value = total_amount_change.index(min(total_amount_change)) + 1

        print("Financial Analysis")
        print("-------------------------")
        print(f"Total Months: {len(total_months)}")
        print(f"Total: ${sum(total_amount)}")
        print(f"Average Change: {round(sum(total_amount_change)/len(total_amount_change),2)}")
        print(f"Greatest Increase in Profits: {total_months[max_value]} (${(str(max_value))}")
        print(f"Greatest Decrease in Profits: {total_months[min_value]} (${(str(min_value))}")
    """
    #output_file = Path("python-challenge", "PyBank", "Financial_Analysis.txt")
    #output_file = Path("..","Financial_Analysis.txt")
    #output_file = os.path("..","Financial_Analysis.txt")
    output_file = os.path("..","PyBank", "Financial_Analysis.txt")

    with open(output_file,"w") as file:

            file.write("financial Analysis")
            file.write("\n")
            file.write("-------------------")
            file.write("\n")
            file.write("Total Months: {len(total_months)}")
            file.write("\n")
            file.write("Total: ${sum(total_amount)}")
            file.write("\n")
            file.write("Average Change: {round(sum(total_amount_change)/len(total_amount_change),2)}")
            file.write("\n")
            file.write("Greatest Increase in Profits: {total_months[max_value]} (${(str(max_value))}")
            file.write("\n")
            file.write("Greatest Decrease in Profits: {total_months[min_value]} (${(str(min_value))}")
"""






