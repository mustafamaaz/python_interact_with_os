import os
import subprocess

my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/", my_env["PATH"]])

result = subprocess.run(["myapp"], env=my_env)

# in this parent process have seperate enviroment variables so run cmd create child process so in this code we copy parent env and and copy it and change some directory
# and pass child process this env 