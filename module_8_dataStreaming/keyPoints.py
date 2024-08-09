# In Python, there are usually a lot of different ways to accomplish the same task. Some are easier to write, some are better suited to a given 
# task, and some have a lower overhead in terms of the amount of computing power used. Subprocesses are a way to call and run other applications 
# from within Python, including other Python scripts. In Python, the subprocess module can run new codes and applications by launching the new
# processes from the Python program. Because subprocess allows you to spawn new processes, it is a very useful way to run multiple processes in 
# parallel instead of sequentially.

# Python subprocess can launch processes to: 

# Open multiple data files in a folder simultaneously. 

# Run external programs. 

# Connect to input, output, and error pipes and get return codes.

# Comparing subprocess to OS and Pathlib
# Again, Python has multiple ways to achieve most tasks; subprocess is extremely powerful, as it allows you to do anything you would from Python
# in the shell and get information back into Python. But just because you can use subprocess doesn’t always mean you'll want to. 

# Let’s compare subprocess to two of its alternatives: OS, which has been covered in other readings, and Pathlib. For tasks like getting the 
# current working directory or creating a directory, OS and Pathlib are more direct (or “Pythonic,” meaning it uses the language as it was intended)
# . Using subprocess for tasks like these is like using a crowbar to open a nut. It's more heavy-duty and can be overkill for simple operations. 

# As a comparison example, the following commands accomplish the exact same tasks of getting the current working directory. 

# Subprocess: 
import subprocess
cwd_subprocess = subprocess.check_output(['pwd'], text=True).strip()

# OS: 
import os
cwd_os = os.getcwd()

# Pathlib: 
import pathlib

cwd_pathlib = Path.cwd()

# And these following commands accomplish the exact same tasks of creating a directory. 

# Subprocess: 

subprocess.run(['mkdir', 'test_dir_subprocess2'])

# OS: 

# os.mkdir('test_dir_os2')

# Pathlib: 

# test_dir_pathlib2 = Path('test_dir_pathlib2')

# test_dir_pathlib2.mkdir(exist_ok=True) #Ensures the directory is created only if it doesn't already exist

# When to use subprocess
# Subprocess is best used when you need to interface with external processes, run complex shell commands, or need precise control over input and
# output. Subprocess also spawns fewer processes per task than OS, so subprocess can use less compute power. 

# Other advantages include:

# Subprocess can run any shell command, providing greater flexibility.

# Subprocess can capture stdout and stderr easily.

# On the other hand, OS is useful for basic file and directory operations, environment variable management, and when you don't need the 
# object-oriented approach provided by Pathlib. 

# Other advantages include:

# OS provides a simple way to interface with the operating system for basic operations.

# OS is part of the standard library, so it's widely available.

# Finally, Pathlib is most helpful for working extensively with file paths, when you want an object-oriented and intuitive way to handle file 
# system tasks, or when you're working on code where readability and maintainability are crucial. 

# Other advantages include: 

# Pathlib provides an object-oriented approach to handle file system paths.

# Compared to OS, Pathlib is more intuitive for file and directory operations. 

# Pathlib is more readable for path manipulations.

# Where subprocess shines
# The basic ways of using subprocess are the .run() and .Popen() methods. There are additional methods, .call(), .check_output(), and 
# .check_call(). Usually, you will just want to use .run() or one of the two check methods when appropriate. However, when spawning parallel 
# processes or communicating between subprocesses, .Popen() has a lot more power!

# You can think of .run() as the simplest way to run a command—it’s all right there in the name—and .Popen() as the most fully featured way to 
# call external commands. 

# All of the methods, .run(), .call(),  .check_output(), and .check_call() are wrappers around the .Popen() class. 

# Run
# The .run() command is the recommended approach to invoking subprocesses. It runs the command, waits for it to complete, then returns a
# CompletedProcess instance that contains information about the process.

# Using .run() to execute the echo command:

# result_run = subprocess.run(['echo', 'Hello, World!'], capture_output=True, text=True)

# result_run.stdout.strip()  # Extracting the stdout and stripping any extra whitespace

# output:

# 'Hello, World!'

# Call 
# The call() command runs a command, waits for it to complete, then returns the return code. Call is older and .run() should be used now,
# but it’s good to see how it works.

# Using call() to execute the echo command: 

# return_code_call = subprocess.call(['echo', 'Hello from call!'])

# return_code_call

# output:

# 0

# The returned value 0 indicates that the command was executed successfully.

# Check_call and check_output
# Use check_call() to receive just the status of a command. Use check_output() to also obtain output. These are good for situations such 
# as file IO, where a file might not exis, or the operation may otherwise fail. 

# The command check_call()is similar to call() but raises a CalledProcessError exception if the command returns a non-zero exit code.

# Using check_call() to execute the echo command:

# return_code_check_call = subprocess.check_call(['echo', 'Hello from check_call!'])

# return_code_check_call

# output:

# 0

# The returned value 0 indicates that the command was executed successfully.

# Using check_output() to execute the echo command:

# output_check_output = subprocess.check_output(['echo', 'Hello from check_output!'], text=True)

# output_check_output.strip()  # Extracting the stdout and stripping any extra whitespace

# output:

# 'Hello from check_output!'

# Note: Check_output raises a CalledProcessError if the command returns a non-zero exit code. For more on CalledProcessError, see 
# Exceptions
# .

# Popen
# Popen() offers more advanced features compared to the previously mentioned functions. It allows you to spawn a new process, connect 
# to its input/output/error pipes, and obtain its return code.

# Using Popen to execute the echo command:

# process_popen = subprocess.Popen(['echo', 'Hello from popen!'], stdout=subprocess.PIPE, text=True)

# output_popen, _ = process_popen.communicate()

# output_popen.strip()  # Extracting the stdout and stripping any extra whitespace

# output:

# 'Hello from popen!'

# Pro tip
# The Popen command is very useful when you need asynchronous behavior and the ability to pipe information between a subprocess and the
# Python program that ran that subprocess. Imagine you want to start a long-running command in the background and then continue with other 
# tasks in your script. Later on, you want to be able to check if the process has finished. Here’s how you would do that using Popen.

# import subprocess

# Using Popen for asynchronous behavior: 

# process = subprocess.Popen(['sleep', '5'])

# message_1 = "The process is running in the background..."

# # Give it a couple of seconds to demonstrate the asynchronous behavior

# import time

# time.sleep(2)

# # Check if the process has finished

# if process.poll() is None:

# 	message_2 = "The process is still running."

# else:

# 	message_2 = "The process has finished."

# print(message_1, message_2)

# output:

# ('The process is running in the background...',

#  'The process is still running.')

# The process runs in the background as the script continues with other tasks (in this case, simply waiting for a couple of seconds).
# Then the script checks if the process is still running. In this case, the check was after 2 seconds' sleep, but Popen called sleep on 5 
# seconds. So the program confirms that the subprocess has not finished running. 

# Key takeaways
# Subprocess is a powerful module that allows you to do anything you could in Python from within the shell, then get information back into Python.
# You’ll probably want to stick with OS for basic file and directory operations or Pathlib for working extensively with file paths. But when you
# interface with external processes, run complex shell commands, or need precise control over input and output, the subprocess module is the way to 
# go.

# source url is 
# https://www.coursera.org/learn/python-operating-system/supplement/hjJ5u/study-guide-python-subprocesses
# What does the copy method of os.environ do?

# Creates a new dictionary of environment variables