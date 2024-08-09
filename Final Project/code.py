#!/usr/bin/env python3

import re
import csv
from collections import defaultdict
import operator


def create_Dictionaries():
    
    error_counts = defaultdict(int)
    user_statistics = defaultdict(lambda: {"INFO": 0, "ERROR": 0})

    with open("test.log") as file:

        for line in file:
            line = line.strip('\n')
            info_pattern = re.compile(r"ticky: INFO ([\w'\.?\" ]*) \[#\d+\] \(([\w\.]+)\)")
            error_pattern = re.compile(r"ticky: ERROR ([\w ' ]*) \(([\w\.]*)\)")
            
            info_match = info_pattern.search(line)
            error_match = error_pattern.search(line)
        
            if info_match:
                user = info_match.group(2)
                user_statistics[user]["INFO"]+=1
                
            elif error_match:
                error_msg = error_match.group(1)
                user = error_match.group(2)
                error_counts[error_msg]+=1  
                #    we count type of error without condidering the user those face this error we count at general error types 
                user_statistics[user]["ERROR"]+=1
                #    we just count the total error occur to perticular user without considering the type of error 
                    
    return error_counts , user_statistics            



def Sort_dict(error_counts , user_statistics):
    
    Sorted_error = sorted(error_counts.items() , key= operator.itemgetter(1),reverse=True)
    # this sorted function return the list of dictionary means i send dict to sort funct {......................} it return [{...................}]
    Sorted_error.insert(0,("Error" , "Count"))
    
    Sorted_user_statistics = sorted(user_statistics.items() , key=operator.itemgetter(0) )
    return Sorted_error , Sorted_user_statistics






def create_csv_file(error_counts , user_statistics):
    
    
    with open("error_message.csv","w") as error:
        writer = csv.writer(error)
        writer.writerows(error_counts)
        
    with open("user_statistics.csv","w") as user:
        fieldnames = ["Username", "Info", "Error"]
        writer = csv.DictWriter(user, fieldnames=fieldnames)
        writer.writeheader()
        # this user_statistic data is in list of tuples i convert it into dictionary before writing into csv 
        for user,stat in user_statistics:
            # now we are in loop so we can't use writerows
            writer.writerow({"Username":user,
                              "Info":stat["INFO"],
                              "Error":stat["ERROR"]})
                
        
        
        
# Note csv.DictWriter(error, fieldname=fieldname) 
# write data if it present in list of dictionary and each row is on dictionary like this   
#         students = [
#     {"Name": "Alice", "Age": 23, "Grade": "A"},
#     {"Name": "Bob", "Age": 22, "Grade": "B"},
#     {"Name": "Charlie", "Age": 24, "Grade": "A"},
#     {"Name": "Diana", "Age": 22, "Grade": "C"} 
# ]in this each dict is one row so in this DictWriter have function of writeheader() and fieldname becz it map this dict item with fieldname and place value to correcponding of it 

# and csv.writer(error) write data if data is in list of list of list of tuples and each list and tuples is one row of csv but in this we have not any fieldname 
# we itself insert the column name into this data like we doing this in sorted function  because we use Sorted function it automatically convert my dict into list of tuples

    
    
        

error_counts, user_statistics = create_Dictionaries()

Sorted_error , Sorted_user_statistics = Sort_dict(error_counts, user_statistics )

create_csv_file(Sorted_error , Sorted_user_statistics)




# material 
# sorted(fruit.items(), key=operator.itemgetter(0))  this (0) is sort the dict according to the key of dict if (1) then sort according to values smaller -----> greater if revere=true then greater <--------------smaller