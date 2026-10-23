class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

#creating objects of the class
student1 = Student("Alice", 20, "A")
student2=Student("Raju", 22, "B")

print(student1.name, student1.age, student1.grade)  # Output: Alice 20 A
print(student2.name, student2.age, student2.grade)  # Output: Raju  

'''
default constructor is a constructor which does not take any parameters. It is used to initialize the object with default values. If we do not define any constructor in a class, Python provides a default constructor that initializes the object with default values. (self)
parameterized constructor is a constructor that takes parameters to initialize the object with specific values. It allows us to create objects with different initial values.
constructor with default values is a constructor that takes parameters with default values. It allows us to create objects with specific values or use default values if no values are provided.    '''