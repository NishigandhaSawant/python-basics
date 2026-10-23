'''
[expression for item in iterable if condition]

r = x* 2
item -> item in the iterable
iterable -> list, tuple, set, etc
condition -> optional, filter the items in the iterable

'''
'''squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)'''

squares = [ i ** 2 for i in range(1,11) if i%2 == 0]
print(squares)