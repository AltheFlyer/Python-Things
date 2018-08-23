#Animal Class
#Allen Liu
#August 9, 2018
#A test for python classes

from enum import Enum

#Animal sizes, simple enum test
class Size(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"
    
class Animal():

    num_animals = 0
    
    def __init__(self, name, weight, size):
        self.name = name
        self.weight = weight
        self.size = size
        Animal.num_animals += 1

    def print_attr(self):
        print("Animal stats for %s" % self.name)
        print("Weight: %.2f" % self.weight)
        print("Size: %s" % self.size.name.lower())

    def print_animal_count(self):
        print("Current animal count: %d" % Animal.num_animals)

class Egg():

    num_eggs = 0

    def __init__(self, name, weight, size):
        self.name = name
        self.weight = weight
        self.size = size
        Egg.num_eggs += 1

    def hatch(self):
        Egg.num_eggs -= 1
        del self
        print("Hatched")

#Subclass of Animal
class Mammal(Animal):

    #Lets the mammal generate more mammals
    #Inheritance should mean that all attributes from above are kept
    #Including the incrementation of the animal count
    def reproduce(self):
        return Mammal("Baby " + self.name, self.weight / 10, Size.SMALL)

class Reptile(Animal):

    #Creates a non-animal object
    def reproduce(self):
        return Egg("Baby " + self.name, self.weight / 20, Size.SMALL)

#Enumeration fun
#Prints name of value in code by default
print(Size.LARGE)
#Represent with more info
print(repr(Size.LARGE))
#Name only
print(Size.LARGE.name)
#Check instance:
print(isinstance(Size.SMALL, Size))

#Working with classes
animal = Animal("Test Subject", 12.7, Size.SMALL)
animal.print_attr()
animal.print_animal_count()

tiger = Mammal("Tiger", 200.5, Size.LARGE)
tiger.print_attr()
tiger.print_animal_count()
animal.print_animal_count()

tiger.reproduce().print_attr()
animal.print_animal_count()

lizard = Reptile("Lizard", 0.3, Size.SMALL)
lizard.print_attr()
lizard.reproduce()
lizard.reproduce().hatch()

print(Egg.num_eggs)
lizard.reproduce()
print(Egg.num_eggs)

