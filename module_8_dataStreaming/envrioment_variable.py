#!/usr/bin/env python3
import os

# to access enviroment variable we use environ method 

print("Home: " + os.environ.get("HOME",""))
# this environ is dictionary method for searching env variable one value is key and other is default if not present 
print("shell: " + os.environ.get("SHELL",""))
print("FRUIT: " + os.environ.get("FRUIT",""))

# output is Home: /home/maaz
# shell: /bin/bash
# FRUIT: 
# home and shell is defined but fruit is not in this enviroment so we want to export fruit env like this 
# export FRUIT=apple
#  we define variable by just setting value export keyword tell the shell we want to set value to env variable 

# Home: /home/maaz
# shell: /bin/bash
# FRUIT: apple


# echo $PATH  gives some directory name where shell will looks for programs when we run pyhton3 program shell check this program in path variable 
# 