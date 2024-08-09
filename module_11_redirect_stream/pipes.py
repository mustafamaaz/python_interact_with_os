#!/usr/bin/env python3

import sys

for line in sys.stdin:
    # this sys.stdin is input data from keyborad or any other file that we sent this take line by line data 
    print(line.strip().capitalize())
    
    # cat output_file.txt | ./pipes.py   we can use pipes for this and also 
    #  ./pipes.py < output_file.txt      use this both are standard stdin 
    
    #  this phenomina is called IO stream redirect  