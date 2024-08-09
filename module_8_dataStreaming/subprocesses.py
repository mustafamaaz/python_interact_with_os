# python provide a way to execute system command in out python script using function providing by subprocess module 

import subprocess
subprocess.run(["date"])
# date cmd for data we can run data cmd by using run function this run function return an object of complete process type and exit status code is attribute present in this complete process instanc
# this interaction of system command from script is parent child process out script is parent and sys cmd is child parent wait untill child finished its work
subprocess.run(["sleep", "2"])


result = subprocess.run(["ls", "this_file_does_not_exist"])
print(result.returncode)

# note this stratigy is use full for those script where we dont want need of output of command only we want to know weather or not this command run like chnage file permission we dont need of output
#  if we want to capture output of sys cmd we use another stratigy in next video 

# this attributes capture_optput = true capture the output of system cmd in script of python 
result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result)
print(result.returncode)




result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout)
# b'8.8.8.8.in-addr.arpa domain name pointer dns.google.\n'  this b means it is in bytes we want to decode the 

result = subprocess.run(["host", "8.8.8.8"], capture_output=True)
print(result.stdout.decode().split())


result = subprocess.run(["rm", "does_not_exist"], capture_output=True)
print(result.returncode)
print(result.stdout)
print(result.stderr)



# this sys cmd use only when we want to solve problem very quick and not long running job because sys cmd vary os to os so 
# if we want to solve for all os and long running job we must use baked module of python pypi like 