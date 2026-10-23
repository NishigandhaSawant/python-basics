a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]

#set function
s1 = set(a)
s2 = set(b)

s3 = s1.intersection(s2)
print(list(s3))  # Output: {4, 5}