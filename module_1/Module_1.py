import pandas
import requests
import PIL.Image

 
response = requests.get("http://www.google.com")
print(len(response.text))

# this open function open the file in home directory
# image = PIL.Image.open("maaz.png")
# print(image.size)
# print(image.format)

visitors = [1235,6424,9345,8464,2345]
errors = [24,34,12,42,72]
df = pandas.DataFrame({"visitors" : visitors , "errors" : errors } , index=["Mon" , "Tues" , "Wed" , "Thurs" , "Fri"] )
print(df)