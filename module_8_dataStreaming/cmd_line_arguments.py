#!/usr/bin/env python3
import sys
print(sys.argv)
# ././cmd_line_arguments.py
# output ['./cmd_line_arguments.py']  

# ./cmd_line_arguments.py one teo three
# output ['./cmd_line_arguments.py', 'one', 'two', 'three']

# return exit status is a value that program return after execution if success return 0 otherwise any other number which help to tell us what kind of error in it
# wc cmd count the line words and character 
# ? is variable in shell where last return status is present  


# (anaconda3)maaz@maaz-HP-ProBook-640-G3:~/Documents/Automation  with Python/python_interect_os/module_8_dataStreaming$ wc input.py 
#  20  90 711 input.py
# (anaconda3)maaz@maaz-HP-ProBook-640-G3:~/Documents/Automation  with Python/python_interect_os/module_8_dataStreaming$ echo $?
# 0
# (anaconda3)maaz@maaz-HP-ProBook-640-G3:~/Documents/Automation  with Python/python_interect_os/module_8_dataStreaming$ wc inpudet.py 
# wc: inpudet.py: No such file or directory
# (anaconda3)maaz@maaz-HP-ProBook-640-G3:~/Documents/Automation  with Python/python_interect_os/module_8_dataStreaming$ echo $?
# 1
# (anaconda3)maaz@maaz-HP-ProBook-640-G3:~/Documents/Automation  with Python/python_interect_os/module_8_dataStreaming$ 