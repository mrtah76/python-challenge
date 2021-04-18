# import Dependencies
import os
import csv

# #locate csv file
csvpath = os.path.join('Resources', 'election_data.csv')

#lets take look at the file
with open(csvpath) as csvfile:
     csvreader = csv.reader(csvfile, delimiter=',')
        #Read the header row First
     csv_header = next(csvreader)
            
    # Define empty List to store clean Data, 
     voter_id = []
     county = []
     candidate = []
    
    #Data Cleaning
     for row in csvreader:
         voter_id_clean = row[0].split(" ")
         voter_id.append(float(voter_id_clean[0]))
         county_clean = row[1].split(" ")
         county.append(str(county_clean[0]))
         candidate_clean = row[2].split(" ")
         candidate.append(str(candidate_clean[0]))
     
     #start with summerizing canidates
     candidate_summary = []
         
     for i in candidate:
         if i not in candidate_summary:
             candidate_summary.append(i)

    # print(f"Total Votes: {len(voter_id)}")
    # print(candidate_summary)
    

     #Counting each candidate total vote
     candidate_total_vote = []
     candidate_percent_vote = []
     candidate_subtotal = 0
     
     #c_s is candidate summary, c is candidate
     for c_s in candidate_summary:
         for c in candidate:
             if c_s == c:
                 candidate_subtotal = candidate_subtotal + 1
         candidate_total_vote.append(candidate_subtotal)

     
        #  print(f"{c_s} Total Vote is {candidate_subtotal}")
   
         #in this loop I calculate percent_vote for each candidate
         each_candidate_percent = round((candidate_subtotal / len(voter_id)) * 100,)
         candidate_percent_vote.append(each_candidate_percent)
         formatted_cand_perc_vote = ["%.3f" % member for member in candidate_percent_vote]
         candidate_subtotal = 0
    # print(candidate_total_vote)
    # print(formatted_cand_perc_vote)

    #Finding the index to identify the winner
     max_vote = max(candidate_total_vote)
     winner_index = candidate_total_vote. index(max_vote) 
     print(candidate_summary[winner_index])
    
       # Print Report
     
     print("Election Results")
     print("----------------------------")
     print(f"Total Votes: {len(voter_id)}")
     print("----------------------------")
     for i in range(len(candidate_summary)):
         print(f"{candidate_summary[i]}: {formatted_cand_perc_vote[i]}% ({candidate_total_vote[i]})")
     print("----------------------------")
     print(f"Winner: {candidate_summary[winner_index]}")
       
     # save file to a text file
     output_path = os.path.join("Analysis", "analysis.txt")
     with open(output_path, "w") as file:
        
         file.write("Election Results\n")
         file.write("----------------------------\n")
         file.write(f"Total Votes: {len(voter_id)}\n")
         file.write("----------------------------\n")
         for i in range(len(candidate_summary)):
             file.write(f"{candidate_summary[i]}: {formatted_cand_perc_vote[i]}% ({candidate_total_vote[i]})\n")
         file.write("----------------------------\n")
         file.write(f"Winner: {candidate_summary[winner_index]}\n")
         file.write("----------------------------\n")
         