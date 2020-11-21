class Animal: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr...")
        
class Dog(Animal):
    def bark(self):
        print("Woof!")

class Rat(Animal):
    def cui(self):
        print("Cui")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()
 
filomena = Rat("ebarista","rosa")
print(filomena.name)
filomena.cui()