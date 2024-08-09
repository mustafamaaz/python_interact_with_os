#!/usr/bin/env python3

def validate_user(username, minlen):
    
  assert type(username) == str,"username must be string"
    #  this assert keyword use to raise error in conditional expression  
    
  if minlen < 1:
    raise ValueError("minlen must be at least 1")
# key word for generate error in python is raise

  if len(username) < minlen:
    return False
  if not username.isalnum():
    return False
  return True

# validate_user("", -1)
# output
#  raise ValueError("minlen must be at least 1")
# ValueError: minlen must be at least 1

# print(validate_user("", 1))
# output False
# print(validate_user("myuser", 1))
# output True

# validate_user(88, 1)
# output
# File "/home/maaz/Documents/Automation  with Python/python_interect_os/module_10_exception_handling/2.py", line 8, in validate_user
#     if len(username) < minlen:
#        ^^^^^^^^^^^^^
# TypeError: object of type 'int' has no len()

# print(validate_user([], 1))
# false

# print(validate_user(["name"], 1))
# error in list we have not isalnum fucntion 


# print(validate_user([3], 1))
# output
        #   ^^^^^^^^^^^^^^^^^^^^^
# AssertionError: username must be string