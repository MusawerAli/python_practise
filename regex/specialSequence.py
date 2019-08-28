import re

str = "That will be 59 dollars"

#Find all digit characters:

x = re.findall("\d", str)
print(x)
