import re

# capturing groups 
# is portion of pattern that are enclose in parantheses

result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])
"{} {}".format(result[2], result[1])



def rearrange_name(name):
    result = re.search(r"^([\w .-]*), ([\w .-]*)$", name)
    if result is None:
        return name
    return "{} {}".format(result[2], result[1])

print(rearrange_name("Lovelace, Ada"))
print(rearrange_name("Ritchie, Dennis"))
print(rearrange_name("Hopper, Grace M."))



print(re.search(r"[a-zA-Z]{5}", "a ghost"))
# [a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]  this 5 class means any string a to z number only 5 letter match 5 letter string so it is repetition of class so we can do this
# [a-zA-Z]{5}  by giving repetition qualifier range
print(re.search(r"[a-zA-Z]{5}", "a scary ghost appeared"))
print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appeared"))
# ['scary', 'ghost', 'appea']  this appea is not full letter so we restrict that we extract only five letter word with before and after space by using \b
re.findall(r"\b[a-zA-Z]{5}\b", "A scary ghost appeared")

print(re.findall(r"\w{5,10}", "I really like strawberries"))
# minimum letter 5 and maximuun 10 
print(re.findall(r"\w{5,}", "I really like strawberries"))
# minimum 5 and max unlimited
print(re.search(r"s\w{,20}", "I really like strawberries"))
print(re.findall(r"\w{,20}", "I really like strawberries"))



log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
 
def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex, log_line)
    if result is None:
        return ""
    return result[1]
print(extract_pid(log))

print(re.split(r"[.?!]", "One sentence. Another one? And the last one!"))
print(re.split(r"([.?!])", "One sentence. Another one? And the last one!"))
print(re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Received an email for go_nuts95@myexample.com"))
re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
# r"\2 \1"   this is a pattern of capturing group 2nd group first then 1 group display at second 






# The transform_comments function converts comments in a Python script into those usable by a C compiler. This means looking for text 
# that begins with a hash mark (#) and replacing it with double slashes (//), which is the C single-line comment indicator.
# For the purpose of this exercise, we'll ignore the possibility of a hash mark embedded inside of a Python command, and assume 
# that it's only used to indicate a comment. We also want to treat repetitive hash marks (##), (###), etc., as a single comment indicator, 
# to be replaced with just (//) and not (#//) or (//#). Fill in the parameters of the substitution method to complete this function: 


def transform_comments(line_of_code):
  result = re.sub(r"([#]+)",r"//\0",line_of_code) 
  return result

print(transform_comments("### Start of program")) 
# Should be "// Start of program"
print(transform_comments("  number = 0   ## Initialize the variable")) 
# Should be "  number = 0   // Initialize the variable"
print(transform_comments("  number += 1   # Increment the variable")) 
# Should be "  number += 1   // Increment the variable"
print(transform_comments("  return(number)")) 
# Should be "  return(number)"