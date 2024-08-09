#!/usr/bin/env python3
import sys
import os
import re

def error_search(log_file):
  error = input("What is the error? ")
#   in this error a string is store that we enter during execution of code 
  returned_errors = []
  
  with open(log_file, mode='r',encoding='UTF-8') as file:
      
    for log in  file.readlines():
        # log file read line by line
      error_patterns = ["error"]
      
      for i in range(len(error.split(' '))):
        # output of range is in this range(0, 5) this function find length that we enter during execution
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
        # all entered error during execution store in this list 
      
      # print("error patterns is ",error_patterns)  
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
        returned_errors.append(log)
        # if all pattern in error_patterns matches with log file line then it append in return errors 
        
    file.close()
  return returned_errors
  
def file_output(returned_errors):
    # os.path.expanduser('~')
  with open('./data'+ '/errors_found.log', 'w') as file:
    for error in returned_errors:
      file.write(error)
    file.close()

    
if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)