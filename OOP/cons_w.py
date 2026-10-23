class car:
    def __init__(self, make, color):
        self.make = make
        self.color = color

car1 = car("Toyota", "Red")
print(car1.make, car1.color)  # Output: Toyota

'''
syntax
class classname:
    def __init__(self, parameters1, parameters2, ...):
        self.attribute1 = parameters1
        self.attribute2 = parameters2
__init__() constructor
self.property = value
        
        '''