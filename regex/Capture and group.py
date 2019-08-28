import re

str = "The rain in Spain falls mainly in the plain! stays"

#Check if the string contains either "falls" or "stays":

x = re.findall("falls|stays", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
