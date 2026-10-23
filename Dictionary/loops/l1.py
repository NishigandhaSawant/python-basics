profile = {
    "name": "John Doe",
    "age": 30,
    "salary": 50000,
}

for k in profile.values():
    print(k)  # Output: John Doe, 30, 50000

for k in profile.items():
    print(k)  # Output: ('name', 'John Doe'), ('age', 30), ('salary', 50000)