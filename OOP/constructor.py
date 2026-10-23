'''
__init__ method is a special method in Python classes. It is called a constructor and is automatically invoked when an object of the class is created. The purpose of the __init__ method is to initialize the attributes of the class with specific values.
The __init__ method takes the self parameter, which refers to the instance of the class being'''


class car:
    def set_details(self, make, model):
        self.make = make
        self.model = model  

car1 = car()
car1.set_details("Toyota", "Camry")

car2 = car()
car2.set_details("Honda", "Civic")

print(car1.make)  # Output: Toyota
print(car1.model)  # Output: Camry
print(car2.make)  # Output: Honda
print(car2.model)  # Output: Civic