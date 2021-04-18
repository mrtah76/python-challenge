# import Dependencies
import os
import csv

# #locate csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# #lets take look at the file
with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
        #Read the header row First
     csv_header = next(csvreader)

     # Define title,  
     month = []
     p_l = []

    #  Lets clean the data
     for row in csvreader:
         month_clean = row[0].split(" ")
         month.append(str(month_clean[0]))
         num_p_l = row[1].split(" ")
         p_l.append(float(num_p_l[0]))
     #print(f"Total Month: {len(month)}")
    
     #calculate total Profit&loss
     totalsum = round(sum(p_l))
     # Ready to print(f"Total : ${totalsum}")
     
     #ch is change in Profit/Loss
     ch = []
     
     for i in range(len(p_l)-1):
         ch.append(p_l[(i+1)] - p_l[i])
        
    #  print(ch)
    #  print(len(ch))

     avg = round(sum(ch)) / len(ch)
     # ready to print(f"Average Change: ${round(avg,2)}")
     max_profit = (max(ch))
    #  print(min(ch))
        # determine what is the index number for the Greatest Increase&Decrease Profit
     for i in range(len(ch)):
          if (ch[i] == max(ch)):
             Great_Inc_prof_index = i+1
          elif (ch[i] == min(ch)):
             Great_Dec_prof_index = i+1
     
     
     #Printing Report
     print("Financial Analysis")
     print("----------------------------")
     print(f"Total Month: {len(month)}")
     print(f"Total : ${totalsum}")
     print(f"Average Change: ${round(avg,2)}")
     print(f"Greatest Increase in Profits: {month[Great_Inc_prof_index]} (${round(max(ch))})")
     print(f"Greatest Increase in Profits: {month[Great_Dec_prof_index]} (${round(min(ch))})")
        
    # Save to text File 
     output_path = os.path.join("Analysis", "analysis.txt")
     with open(output_path, "w") as file:
        
         file.write("Financial Analysis\n")
         file.write("----------------------------\n")
         file.write(f"Total Month: {len(month)} \n")
         file.write(f"Total : ${totalsum} \n")
         file.write(f"Average Change: ${round(avg,2)}\n")
         file.write(f"Greatest Increase in Profits: {month[Great_Inc_prof_index]} (${round(max(ch))})\n")
         file.write(f"Greatest Increase in Profits: {month[Great_Dec_prof_index]} (${round(min(ch))})\n")
     
        