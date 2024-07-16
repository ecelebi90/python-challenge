import os
import csv
# csvpath = os.path.join('.','Resouces','budget_data.csv')

#csvpath = os.path.join('python-challenge' ,'PyBank','Resources','budget_data.csv')

Total_Votes = 0
Candidate_Votes = 0
Candidates = {}
Ballet_List = []
Candidate_List = []
Unique_List = []
Candidate1_List = []
Max_Val = 0
Max_Candidate = 0
count = 0
Candidates_Name = []

csvpath = os.path.join("C:\\","DataAnalytics","CU-VIRT-DATA-PT-06-2024-U-LOLC","python-challenge","PyPoll","Resources","election_data.csv")

with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     next(csvreader)

     for row in csvreader:
          Total_Votes = Total_Votes + 1 
          Candidate_Votes = Ballet_List.append(row[0])
          Candidate_List.append(row[2])

          if row[2] in Candidates:
              Candidates[row[2]]["Votes"] += 1
              Candidates[row[2]]["Percent"] = round((Candidates[row[2]]["Votes"]/Total_Votes)*100,2)
          else:
              Candidates[row[2]] = {"Votes":1}
              Candidates[row[2]]["Percent"] = round((Candidates[row[2]]["Votes"]/Total_Votes)*100,2)
print(Candidates)        
            

for i in Candidates:
    Votes = Candidates[i]["Votes"] 
    Percent = Candidates[i]["Percent"]
 
for x in Candidate_List:
     if x not in Unique_List:
         count +=1
         Unique_List.append(x)


for key, Candidates in Candidates.items():
    for x in Candidates.items():
        if x[1] > Max_Val:
            Max_Val = x[1]
            Max_Candidate = [key]
      

print("Election Results")

print("------------------------------------------")

print(f"Total Votes: {Total_Votes}")

print("------------------------------------------")

print(f'{Candidate_List[0]} : {Candidates["Percent"]}')




 



