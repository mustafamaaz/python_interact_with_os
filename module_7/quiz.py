# The check_web_address function checks if the text passed qualifies as a top-level web address, meaning that it contains alphanumeric
# characters (which includes letters, numbers, and underscores), as well as periods, dashes, and a plus sign, followed by a period and
# a character-only top-level domain such as ".com", ".info", ".edu", etc. Fill in the regular expression to do that, using escape characters,
# wildcards, repetition qualifiers, beginning and end-of-line characters, and character classes.


import re
def check_web_address(text):
  pattern = r"^[a-zA-Z0-9_.+-]+[a-zA-Z0-9-]+\.[a-zA-Z]+$"
  result = re.search(pattern, text)
 
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True






# The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, with no leading zero,
# followed by a colon, then minutes between 00 and 59, then an optional space, and then AM or PM, in upper or lower case. Fill in the regular
# expression to do that. How many of the concepts that you just learned can you use here?



# ^: Start of the string.

# (1[0-2]|[1-9]):

# 1[0-2]: Matches "10", "11", or "12".
# [1-9]: Matches single-digit hours from "1" to "9".
# The entire group (1[0-2]|[1-9]) ensures that the hour is between 1 and 12, with no leading zeros.
# :: Matches the literal colon character separating hours and minutes.

# ([0-5][0-9]):

# [0-5][0-9]: Matches minutes from "00" to "59".
# ?:

# The space and question mark ? together match an optional space. The question mark ? makes the preceding space optional.
# ([AaPp][Mm]):

# [AaPp]: Matches either "A" or "P", regardless of case.
# [Mm]: Matches "M", regardless of case.
# The entire group ([AaPp][Mm]) matches "AM" or "PM" in any case combination.
# $: End of the string.

# This regular expression covers the specified time format, ensuring valid inputs like "12:45pm" or "9:59 AM" are matched while invalid inputs like "6:60am" or "five o'clock" are not.




def check_time(text):
  pattern = r"^(1[0-2]|[1-9]):([0-5][0-9]) ?([AaPp][Mm])$"
  result = re.search(pattern, text)
  # print(result)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False
print(check_time("6:02 am")) # True
print(check_time("6:02km")) # False





# The contains_acronym function checks the text for the presence of 2 or more characters or digits surrounded by parentheses,
# with at least the first character in uppercase (if it's a letter), returning True if the condition is met, or False otherwise. 
# For example, "Instant messaging (IM) is a set of communication technologies used for text-based communication" should return True since
# (IM) satisfies the match conditions." Fill in the regular expression in this function: 






import re
def contains_acronym(text):
  pattern = r"\([a-zA-z0-9]+[a-zA-z0-9]\)"
#  this expression first class match only one character present one or more time "+ 2nd class" check match that minimum 2 or more character present 
  result = re.search(pattern, text)
  print(result)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True







# An intern implemented a zip code checker, but it works only with five-digit zip codes. Your task is to update the checker so that it
# includes all nine digits of the zip code; the leading five digits and the optional four after the hyphen. The zip code needs to be
# preceded by at least one space, and cannot be at the start of the text. Update the regular expression.





import re

def correct_function(text):
  
  result = re.search(r" \d{5}(-\d{4})?", text)  # Corrected regex pattern with space
  print(result)
  return result is not None

def check_zip_code(text):
  return correct_function(text)  # Call the correct_function

# Call the check_zip_code function with test cases
print(check_zip_code("The zip codes for New York are 10001 thru 11104."))  # True
print(check_zip_code("90210 is a TV show"))  # False (no space before 90210)
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001."))  # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9."))  # False






# You’re working with a CSV file that contains employee information. Each record has a name field, followed by a phone number field, 
# and a role field. The phone number field contains U.S. phone numbers and needs to be modified to the international format, with "+1-"
# in front of the phone number. The rest of the phone number should not change. Fill in the regular expression, using groups, to use the 
# transform_record function to do that.

def transform_record(record): 
    # Match the phone number in the format XXX-XXX-XXXX or XXX-XXXXXXX and add +1- in front of it
    new_record = re.sub(r"(\d{3}-\d{3}-\d{4}|\d{3}-\d{7})", r"+1-\1", record)
    return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer




# The multi_vowel_words function returns all words with 3 or more consecutive vowels (a, e, i, o, u).
# Fill in the regular expression to do that.


def multi_vowel_words(text):
 # \b marks word boundaries; [aeiouAEIOU]{3,} matches 3 or more consecutive vowels, case insensitive
  pattern = r"\b\w*[aeiouAEIOU]{3,}\w*\b"
  result = re.findall(pattern, text)
  return result

print(multi_vowel_words("Life is beautiful")) 
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious.")) 
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner.")) 
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)")) 
# ['queue']

print(multi_vowel_words("Hello world!")) 
# []











# The convert_phone_number function checks for a U.S. phone number format: XXX-XXX-XXXX (3 digits followed by a dash,
# 3 more digits followed by a dash, and 4 digits), and converts it to a more formal format that looks like this: 
# (XXX) XXX-XXXX. Fill in the regular expression to complete this function.



def convert_phone_number(phone):
  result = re.sub( r"\s([0-9]{3})-([0-9]{3})-([0-9]{4})",r"(\1) \2-\3 ",phone)
  return result

print(convert_phone_number("My number is 212-345-9999.")) # My number is (212) 345-9999.
print(convert_phone_number("Please call 888-555-1234")) # Please call (888) 555-1234
print(convert_phone_number("123-123-12345")) # 123-123-12345
print(convert_phone_number("Phone number of Buckingham Palace is +44 303 123 7300")) # Phone number of Buckingham Palace is +44 303 123 7300







def find_gov_urls(website):
 pattern = r"(https://www\.\w*\.gov)" #enter the regex pattern here
 result = re.findall(pattern, website) #enter the re method here
 return result


print(find_gov_urls("https://www.data.gov is a great place to find open source datasets!")) # Should return ['https://www.data.gov']
print(find_gov_urls("Learn more about US National Parks at https://www.nps.gov, https://www.nationalparks.org, or https://www.recreation.gov.")) # Should return ['https://www.nps.gov', 'https://www.recreation.gov']
print(find_gov_urls("The Library of Congress (https://www.loc.gov) is an incredible resource!")) # Should return ['https://www.loc.gov']
print(find_gov_urls("The Library of Congress (www.loc.gov) is an incredible resource!")) # Should return []







# You’re working with a dataset on capital cities around the world. This dataset includes a field that contains information on both city and 
# country. You’d like to separate this field into two fields, a city field and a country field. In the current field, city and country are separated 
# by either a comma or a period. Complete the function parse_city_country to split city and country into two strings and return only the city.




def parse_city_country(text):
    pattern = r'^([^,\.]+)[,\.]'  # Match any characters except commas and periods until the first comma or period
    result = re.findall(pattern, text)
    print(len(result))
    if len(result) != 1:
        return ""
    return result[0].strip()  # Return the captured group, removing any leading or trailing whitespace

print(parse_city_country("Paris, France"))  # should return Paris
print(parse_city_country("Mumbai, India"))  # should return Mumbai
print(parse_city_country("Rio de Janeiro. Brazil"))  # should return Rio de Janeiro
print(parse_city_country("Tokyo! Japan"))  # result should be blank



# A company uses unique, 9-character codes that begin with a capital letter, followed by a hyphen (-), followed by 7 or 8 digits as employee
# ID numbers, in the format A-1234567 or A-12345678. Project reports submitted to the company include the employee’s ID number and a summary 
# of the work they completed on the project. 
# A data analyst wants to pull all of the employee ID numbers out of these projects. Complete the find_eid function to extract these employee
# ID numbers from the reports. 


def find_eid(report):
  pattern = r"\b([A-Z]-[0-9]{7,8})\b" #enter the regex pattern here
  result = re.findall(pattern, report) #enter the re method  here
  return result


print(find_eid("Employees B-1234567 and C-12345678 worked with products X-123456 and Z-123456789")) # Should return ['B-1234567', 'C-1234567']
print(find_eid("Employees B-1234567 and C-12345678, not employees b-1234567 and c-12345678")) #Should return ['B-1234567', 'C-1234567']