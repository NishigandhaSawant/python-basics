class Student:
    def set_details(self, name, age):
        self.name = name
        self.age = age

student1 = Student()
student1.set_details("Alice", 20)
print(f"Student Name: {student1.name}, Age: {student1.age}")  # Output: Student Name: Alice, Age: 20    

