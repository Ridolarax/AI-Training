import re

text = "Today is the most wonderful day of the week"
if re.search("wonderful", text):
    print("Yes, Today is good")
else:
    print("Alas! :(")
    
new_text = "The man is good. The man loves to play The Cricket. The man lost his eye on The field. Sorry for The man"
dummy = new_text.split("The")
print(dummy)

dummy1 = re.split("The", new_text)
print(re.findall("man", new_text))

if re.search("^Welcome", new_text):
    print("Yes, It begins with 'The'")
else:
    print("I don't know this")
    

dummy2 = "Calculator is compulsory for every science student!"
if re.search("student!$", dummy2):
    print("Yeah, This ends with 'student'")
else:
    print("No, This doesn't :(")

grades = "ABAAABACACAB"
print(re.findall("AB", grades))
print(re.findall("AB|AC", grades))
print(re.findall("[AB]", grades))
print(re.findall("[A][B-C]", grades))


# I guess this is not called set Operator
if re.search("^B", grades):
    print("Yeah, Begins with A")
else:
    print("No!")
    
    
# This following one is called the set operator: Now, i get it, set operator is the []
grades = grades
print(re.findall("[^A]", grades))


# Lemme assume one thing to work with it!

std_grade = "AABCABAAABCBAAC"

# Check for the number of occurences of A, then B, then C only
print(re.findall("A", std_grade), "Occurence = ", len(re.findall("A", std_grade)))
print(re.findall("B", std_grade), "Occurence = ", len(re.findall("B", std_grade)))
print(re.findall("C", std_grade), "Occurence = ", len(re.findall("C", std_grade)))

# Now, check for the occurence of both AB together alone

print(re.findall("AB|AC", std_grade))

# Try using the Set Operator

print(re.findall("^AA", std_grade))

print(std_grade)
# Now moving to Quantifiers
print(re.findall("A{2,3}", std_grade))