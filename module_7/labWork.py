#!/usr/bin/env python3

import re
import csv


def contains_domain(address, domain):
  """Returns True if the email address contains the given,domain,in the domain position, false if not."""
  domain_pattern = r'[\w\.-]+@'+domain+'$'
  if re.match(domain_pattern,address):
    return True
  return False


def replace_domain(address, old_domain, new_domain):
  """Replaces the old domain with the new domain in the received address."""
  old_domain_pattern = r'' + old_domain + '$'
  address = re.sub(old_domain_pattern, new_domain, address)
  return address

def main():
  """Processes the list of emails, replacing any instances of the old domain with the new domain."""
  old_domain, new_domain = 'abc.edu', 'xyz.edu'
  csv_file_location = './data/user_email.csv'
  report_file = './data' + '/updated_user_emails.csv'
  
  user_email_list = []
  old_domain_email_list = []
  new_domain_email_list = []

  with open(csv_file_location, 'r') as f:
    user_data_list = list(csv.reader(f))
    # [['Full Name', ' Email Address'], ['Blossom Gill', ' blossom@abc.edu'], ['Hayes Delgado', ' nonummy@utnisia.com']] user_data_list is this formet
    
    user_email_list = [data[1].strip() for data in user_data_list[1:]]
    # ['Blossom Gill', ' blossom@abc.edu'] user_data_list[1] is this so we want 1: it means from 1 to till end but data[1] extract only emial 1 index not 0 name
    # and in such way all email store in user_email_list strip remove all spaces in email and store into user_email_list
    
    


    for email_address in user_email_list:
      if contains_domain(email_address, old_domain):
        old_domain_email_list.append(email_address)
        replaced_email = replace_domain(email_address,old_domain,new_domain)
        new_domain_email_list.append(replaced_email)



    email_key = ' ' + 'Email Address'
    email_index = user_data_list[0].index(email_key)
    # this email_index is ['Full Name', ' Email Address'] only Email Address
    
    
    
    for user in user_data_list[1:]:
    # this is a list of list of csv file that create at start
    
      for old_domain, new_domain in zip(old_domain_email_list, new_domain_email_list):
          
        if user[email_index] == ' ' + old_domain:
          user[email_index] = ' ' + new_domain
                       
  f.close()

  with open(report_file, 'w+') as output_file:
    writer = csv.writer(output_file)
    writer.writerows(user_data_list)
    #  this user_data_list is updated with new domain
    output_file.close()

main()