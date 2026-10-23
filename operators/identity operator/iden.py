"""
is
is not - True if both variables are the same object"""

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)  # True, because b is the same object as a
print(a is c)  # False, because c is a different object with the same content
print(a is not b)  # False, because b is the sameobject as a