import math

def quadratic(a,b,c):
    x1 = (-b + math.sqrt((b**2) - (4*a*c) ))/ 2*a
    x2 = (-b - math.sqrt((b**2) - (4*a*c) ))/ 2*a

    return "x is either {} or {}".format(x1, x2)


q1 = quadratic(1,3,2)
print(q1)

# print("yes")
