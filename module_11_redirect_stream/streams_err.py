#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
raise ValueError("Now we generate an error to STDERR")

# in this code we redirect the STDIN from file instead of keyboard  
# but STDERR display the error using STDOUT but when error raise  

# (anaconda3)maaz@maaz-HP-ProBook-640-G3:~/Documents/Automation  with Python/python_interect_os/module_11_redirect_stream$ ./streams_err.py < output_file.txt
# This will come from STDIN: Now we write it to STDOUT: Don't mind me, just a bit of text here...
# ^^^^^^^^^^^^^^^^^^^^^^ above is output of 2 line code below is for error raise now we want to display error into file not in screen 
# Traceback (most recent call last):
#   File "/home/maaz/Documents/Automation  with Python/python_interect_os/module_11_redirect_stream/./streams_err.py", line 5, in <module>
#     raise ValueError("Now we generate an error to STDERR")
# ValueError: Now we generate an error to STDERR


# note
# ./streams_err.py < input_file.txt > display.txt
# if script has input filed STDIN so it get value form output file and display all values of STDOUT into display.txt if there is any STDERR error raise in script it display into screen default but we want to display error in to new file using 2> error.txt 

# ./streams_err.py < output_file.txt 2> error.txt > display.txt  final cmd 
# 2> in this 2 is file discriptor of STD ERR stream  0 for STDIN and 1 for STDOUT



# cat output_file.txt | tr ' ' '\n' | sort | uniq -c | sort -nr | head    is cmd use for sort the words of file and count them