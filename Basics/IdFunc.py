"""
Id function used for checking the identity of both variables if the reference is same or not.
"""
x = 90
y = 90
if id(x) == id(y):
    print("Both are referencing same object")
else:
    print("Both are referencing different object")
