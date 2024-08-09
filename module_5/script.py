# One of the easiest ways is to use low-level functions in the OS and SYS modules that closely mimic standard Linux commands such as os.mkdir()and 
# os.rmdir(). Alternatively, you can utilize the Pathlib module, which provides an object-oriented interface to working with the file systems. 
# Let’s take a look at two examples. The first example uses OS; the second uses Pathlib. These two code examples do the same thing: 
# They create a directory called test1 and move a file named README.md from the sample_data folder into test1.






# # Create a directory and move a file from one directory to another
# # using low-level OS functions.

import os

# print(os.getcwd())
# Check to see if a directory named "test1" exists under the current
# directory. If not, create it:
dest_dir = os.path.join(os.getcwd(), "test1")
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)


# Construct source and destination paths:
src_file = os.path.join(os.getcwd(), "sample_data", "README.md")
dest_file = os.path.join(os.getcwd(), "test1", "README.md")

print("this is scr file" , src_file)
print("this is dest file" , dest_file)


# Move the file from its original location to the destination:
os.rename(src_file, dest_file)  # for this we must create first smaple_data dir and having file readme after this rename function work it is just prototype function now

print("this is scr file" , src_file)
print("this is dest file" , dest_file)














# Create a directory and move a file from one directory to another
# using Pathlib.

from pathlib import Path

# Check to see if the "test1" subdirectory exists. If not, create it:
dest_dir = Path("./test1/")
if not dest_dir.exists():
  dest_dir.mkdir()

# Construct source and destination paths:
src_file = Path("./sample_data/README.md")
dest_file = dest_dir / "README.md"

# Move the file from its original location to the destination:
src_file.rename(dest_file)

