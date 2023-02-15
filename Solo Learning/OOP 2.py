# Inheratence

# class Animal:
#
#     def __init__(self):
#         print("Animal Created")
#
#     def who_i_am(self):
#         print("I'm an animal")
#
#     def feed(self):
#         print("I'm eating")
#
#
# class Dog(Animal):
#
#     def __init__(self):
#         Animal.__init__(self)
#         print("Dog Created")
#
#     def who_i_am(self): # override your method from inh class
#         print("Im a dog")
#
# my_dog = Dog()
# print(my_dog.feed())
# print(my_dog.who_i_am())

# Polymorphism

class Dog:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof"

class Cat:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says meow"


niko = Dog("Niko")
tom = Cat("Tom")
print(niko.speak())
print(tom.speak())

for pet in [niko, tom]:
    print(type(pet))
    print(pet.speak())

def pet_speak(pet):
    print(pet.speak())

print(pet_speak(niko))



