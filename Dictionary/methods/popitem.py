profile = {
    "name": "John Doe",
    "age": 30,
    "salary": 50000,
}

popped_item = profile.popitem()
print("Popped Item:", popped_item)  # Output: Popped Item: ('salary', 50000)
print(profile)  # Output: {'name': 'John Doe', 'age': 30}