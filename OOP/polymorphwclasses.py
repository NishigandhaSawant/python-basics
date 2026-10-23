#polymorphism with classes method overriding
class Bird:
    def sound(self):
        print("Birds can make sounds")

class crow(Bird):
    def sound(self):
        print("Crows can caw")


class parrot(Bird):
    def sound(self):
        print("Parrots sounds squak")

bird1= crow()
bird2=parrot()

bird1.sound()
bird2.sound()