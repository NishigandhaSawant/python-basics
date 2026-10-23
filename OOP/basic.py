class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

dog = Dog()
cat = Cat() 

print(dog.speak())  # Output: Dog barks
print(cat.speak())  # Output: Cat meows

dog.speak()  # Output: Dog barks