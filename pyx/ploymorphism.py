class Animal:
    def speak(self):
        return "some sound"
    
class Dog(Animal):
    def speak(self):
        return "woof"
    
class Cow(Animal):
    def speak(self):
        return "moo"
    

# use the plymorohism
animalx = [Dog(), Cow()]

for animal in animalx:
    print(animal.speak())

