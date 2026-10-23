profile = {
    'name': 'John Doe',
    'age': 30,
    'salary': 50000,
}
#dictionary.get() method is used to retrieve the value of a specified key from a dictionary. If the key is not found, it returns a default value (None if not specified).

age = profile.get('age')
print("Age:", age)  # Output: Age: 30