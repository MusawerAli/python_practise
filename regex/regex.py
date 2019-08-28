import re

txt = "The rain in Spain"

x = re.search("^The.*Spain$", txt)

print("Have a match") if (x) else print("no match")