import re

str = "hello youtube, hellowise"

x = re.findall("^hello", str)
print(x)