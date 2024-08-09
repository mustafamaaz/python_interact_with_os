with open("spider.txt", "w") as file:
    # this w is mode of open file w mean write if file exist it override the comming content in file and del previous content 
    # default r read mode is sellected when open file call
    # a is append mode it append comming content in file not override the content
    # r+ is read and write
    file.write("It was a dark and stormy night")
    
    
    
guests = open("spider.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
    
guests.close()


with open("spider.txt") as guests:
    for line in guests:
        print(line)
        
        
        
        
new_guests = ["Sam", "Danielle", "Jacob"]
with open("spider.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

with open("spider.txt") as guests:
    for line in guests:
        print(line)
        
        
        
        
# Now let's remove the guests that have checked out already. There are several ways to do this, however, the method we will choose for this exercise is outlined as follows:

# Open the file in "read" mode.
# Iterate over each line in the file and put each guest's name into a Python list.
# Open the file once again in "write" mode.
# Add each guest's name in the Python list to the file one by one.

# Ready? Fill in the missing code in the following cell to remove the guests that have checked out already.        
        
        
        
checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("spider.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("spider.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")
               
            
with open("spider.txt") as guests:
    for line in guests:
        print(line)



# The current names in the guests.txt file should be: Bob, Polly, Sam, Danielle and Jacob.

# Were the names of the checked out guests correctly removed from the guests.txt file? If not, go back and edit your code making sure to fill in the gaps appropriately so that the checked out guests are correctly removed from the guests.txt file. Once the checked out guests are successfully removed, you have filled in the missing code correctly. Awesome!

# Now let's check whether Bob and Andrea are still checked in. How could we do this? We'll just read through each line in the file to see if their name is in there. Run the following code to check whether Bob and Andrea are still checked in.


guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("spider.txt","r") as guests:
    for g in guests:
        checked_in.append(g.strip())
        
    for check in guests_to_check:
        if check in checked_in:
            print("{} is checked in".format(check))
        else:
            print("{} is not checked in".format(check))





