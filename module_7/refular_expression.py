#  regular expression are used for processing the text 
log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
print(index)
print(log[index+1:index+6])
#  this is not a regular expresion if in log there are many square brackets then this method not working 

# ubuntu command g grep l.rts /usr/share/dict/words rep l.rts /usr/share/dict/words   this . is wildcard for finding whole words
#  grep ^fruits or cat$ /usr/share/dict/words    ^ start of line and $ means end of line 
# ^iting    this ^ match the pattern of words from start of words like writing is words if we find ^iting  its not present becasue no word start from iting  


log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])



import re
result = re.search(r"aza", "plaza")   # r indcate that this is a rawstring    alway use a rawstring for regular expression in python
print(result)
# output <re.Match object; span=(2, 5), match='aza'>


result = re.search(r"aza", "bazaar")
print(result)
# <re.Match object; span=(1, 4), match='aza'>


result = re.search(r"aza", "maze")
print(result)
print(re.search(r"^x", "xenon"))
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))
print(re.search(r"p.ng", "Pangaea", re.IGNORECASE))




print(re.search(r"[Pp]ython", "Python"))

print(re.search(r"[a-z]way", "The end of the highway"))

print("given", re.search(r"[a-z]way", "What a way to go"))
# output is  None because range of wild card character is a to z but in sentance before way there is space " "  
print(re.search("cloud[a-zA-Z0-9]", "cloudy"))
print(re.search("cloud[a-zA-Z0-9]", "cloud9"))






print(re.search(r"[^a-zA-Z]", "Thisis a sentence with spaces."))
print(re.search(r"[^a-zA-Z # ]", "This is a sentence with # $ spaces."))
#  this use for searching special character 

print(re.search(r"cat|dog", "I like cats."))
print(re.search(r"cat|dog", "I love dogs!"))
print(re.search(r"cat|dog", "I like both dogs and cats."))
#  this search function match values of only first occur in above only dog display so for this we use findall function for all matches values
print(re.findall(r"cat|dog", "I like both dogs and cats."))


# repetition qualifier

print(re.search(r"Py.*n", "Pygmalion"))
print(re.search(r"Py.*n", "Python Programming"))
# above all match pattern till n comes  this is greedy approach
print(re.search(r"Py[a-z]*n", "Python Programming"))
print(re.search(r"Py[a-z]*n", "Pyn"))


print(re.search(r"o+l+", "goldfish"))
print(re.search(r"o+l+", "woolly"))
print(re.search(r"o+l+", "boil"))

# + means o , l character occur one or more time 

print(re.search(r"p?each", "To each their own"))
print(re.search(r"p?each", "I like peaches"))
# ? means P occur 0 or 1 time



print(re.search(r".com", "welcome"))
# . is wild card so we want to match .com from google.com so we use / for escape any special character  before .
print(re.search(r"\.com", "welcome"))
print(re.search(r"\.com", "mydomain.com"))



print(re.search(r"\w*", "This is an example"))
# /w means number letter and underscore  in above output is this because /w have not space that why is only print this 
print(re.search(r"\w*", "And_this_is_another"))
# this sentance have not spaces that way whole string is print 
#  /d for digits /s for spaces, tab ,  new line  /b for word boundry


print(re.search(r"A.*a", "Argentina"))
print(re.search(r"^A.*a$", "Azerbaijan"))
# we restrict that start form A and end at a 
print(re.search(r"^A.*a$", "Australia"))



pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
# pattern start from latter or _ and end with letter number or underscore
print(re.search(pattern, "_this_is_a_valid_variable_name"))
print(re.search(pattern, "this isn't a valid variable"))
#  it does not match pattern bcz space are include in possible character
print(re.search(pattern, "my_variable1"))
print(re.search(pattern, "2my_variable1"))


# r”\d{3}-\d{3}-\d{4}”  This line of code matches U.S. phone numbers in the format 111-222-3333.


# r”^-?\d*(\.\d+)?$”  This line of code matches any positive or negative number, with or without decimal places.

# r”^(.+)\/([^\/]+)\/” This line of code matches any path and filename.


# finditer






