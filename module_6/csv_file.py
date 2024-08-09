import csv
f = open("csv_file.txt")
csv_f = csv.reader(f)
for row in csv_f:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name, phone, role))
f.close()






hosts = [["workstation.local", "192.168.25.46"],["webserver.cloud", "10.2.5.6"]]
with open('hosts.csv','w') as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
    
    
    
    
    
    # aceess data using column name  
with open('software.csv') as software:
    reader = csv.DictReader(software)
  
    
    for row in reader:
      print("this is row \n" , row)
      print(("{} has {} users").format(row["name"], row["users"]))
      
      
      
# store dictionary data into csv file in column sence
users = [ {"name": "Sol Mansi", "username": "solm", "department": "IT infrastructure"}, 
 {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"}, 
  {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]

keys = ["name", "username", "department"]

with open('by_department.csv', 'w') as by_department:
    writer = csv.DictWriter(by_department, fieldnames=keys) # keys is arrgumets for column header
    writer.writeheader()
    writer.writerows(users)          
    
    
    
#     csv.reader This function returns a reader object that iterates over lines in the .csv file.
# csv.writer This function returns a writer object that’s responsible for converting the user’s data into delimited strings on the given file-like object.
# class csv.DictReader This function creates an object that functions as a regular reader but maps the information in each row to a dictionary whose keys are given by the optional fieldname parameters.