class car:
    def set_details(self, make, model):
        self.make = make
        self.model = model  

car1 = car()
car1.set_details("Toyota", "Camry")
print(f"Car Make: {car1.make}, Model: {car1.model}")  # Output: Car Make: Toyota, Model: Camry
