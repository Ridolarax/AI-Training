import re

text = "Today is the most wonderful day of the week"
if re.search("wonderful", text):
    print("Yes, Today is good")
else:
    print("Alas! :(")