import re

str = "The rain in Spain"

#Check if the string ends with "Spain":

x = re.findall("Spain\Z", str)

print(x)

if (x):
  print("Yes, there is a match!")
else:
  print("No match")