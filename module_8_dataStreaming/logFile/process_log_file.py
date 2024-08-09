#!/usr/bin/env python3

import sys
import re


logfile = sys.argv[1]

username = {}


with open(logfile) as f:
  for line in f:
    if "CRON" not in line:
      continue
    
    pattern = r"USER \((\w+)\)$"
    result = re.search(pattern, line)
    if result is None:
      continue
    name = result[1]
    username[name] = username.get(name,0) + 1 
    
print(username)   
