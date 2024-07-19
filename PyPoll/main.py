import os
import csv

Total_Votes = 0
Candidate_Votes = 0
Candidates = {}
Ballet_List = []
Candidate_List = []
Unique_List = []
count = 0
Candidates_Name = []
Votes_List = []
Percent_List = []
Max_Value = 0 
Max_Index = 0
Percent = 0

csvpath = os.path.join("C:\\","DataAnalytics","CU-VIRT-DATA-PT-06-2024-U-LOLC","python-challenge","PyPoll","Resources","election_data.csv")

with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=",")
     next(csvreader)

     for row in csvreader:
          Total_Votes = Total_Votes + 1 
          Candidate_Votes = Ballet_List.append(row[0])
          Candidate_List.append(row[2])

          if row[2] in Candidates:
              Candidates[row[2]] += 1
              
          else:
              Candidates[row[2]] = 1
               
for i in Candidates:
    Votes_List.append(Candidates[i])
    Percent = round((Candidates[i]/Total_Votes)*100,3)
    Percent_List.append(Percent)

 
for x in Candidates:
     if x not in Unique_List:
         count +=1
         Unique_List.append(x)

Max_Value = max(Votes_List)
Max_Index = Votes_List.index(Max_Value)

# print("Election Results")
# print("------------------------------------------")
# print(f"Total Votes: {Total_Votes}")
# print("------------------------------------------")
# for i in range(0,len(Unique_List)):
#     print(f'{Unique_List[i]}: {Percent_List[i]}%  ({Votes_List[i]}) ')
# print("------------------------------------------")
# print("Winner:", Unique_List[Max_Index])
# print("------------------------------------------")


line1 ="Election Results"
line2 = "Total Months: "
line2a = str(Total_Votes)
line4 = "Winner:"
line4a = str(Unique_List[Max_Index])
sline = "---------------------------------------"
phr1 = ":"
phr2 = "%"
phr3 = "("
phr4 = ")"


file = open("c:\DataAnalytics\CU-VIRT-DATA-PT-06-2024-U-LOLC\python-challenge\PyPoll\Analysis\PyPoll_Analysis.txt","w")

file.write(line1 + "\n" + sline + "\n" + line2 + line2a + "\n" + sline + "\n") 

for i in range(0,len(Unique_List)):
    line3 = str(Unique_List[i])
    line3a = str(Percent_List[i])
    line3b = str(Votes_List[i])    
    length = len(Unique_List)

    file.write(line3 + phr1 + " " + line3a + phr2 + " " + phr3 + line3b + phr4 + "\n")

file.write(sline + "\n" + line4 + " " + line4a +  "\n" + sline + "\n")   

file.close() 
   


