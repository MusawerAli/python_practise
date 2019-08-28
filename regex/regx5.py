import re

str = "The rain in Spain"

#Check if "ain" is present, but NOT at the beginning of a word:

x = re.findall(r"\Bain", str)

print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")
