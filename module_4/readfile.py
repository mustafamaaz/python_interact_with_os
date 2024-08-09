file = open("spider.txt")
print(file.readline())
# print(file.read())
# if we have small file so we can use read method for direct read all content at a time and performance is good but
# but when we have large file best practice is for content reading is read content line by line readline() method it cause minimun memory consumption and fast file processing if we read all content processing will be slow down

file.close()
# when you open file you should close file after work done because when we are working on multiple file and not closing after work done we can be enter in race condition 

# so we use with key word that open and close the file automatically and gave us block of code 

with open("spider.txt") as file :
    print(file.read())
    
    
 
with open("spider.txt") as file:
    for line in file:
        print(line.upper())    
        #  print lines in upper case
     
     
with open("spider.txt") as file:
    for line in file:
        print(line.strip().upper())
        # strip method use for removing the new line character one \n is in spider.txt line and other \n is in when print() function call 
        
        
file = open("spider.txt")
lines = file.readlines()
file.close()
lines.sort()
print(lines)                