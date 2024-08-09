#!/usr/bin/env python3

import sys
import subprocess

filename = sys.argv[1]
# this arguments is file in which  jane files name and path present this process done by bash script now we update the name from jame to jdoe 

with open(filename, "r") as f:
    lines = f.readlines()
    for line in lines:
        oldname = line.strip()
        print("Original:", line)
        print("With strip:", oldname)
        newname = oldname.replace("jane","jdoe")
        print("with replace ", newname )
        subprocess.run(["mv",oldname,newname])


