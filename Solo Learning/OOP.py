# class NameOfClass():
#     def __init__(self, parm1, parm2):
#         self.parm1 = parm1
#         self.parm2 = parm2
#     def function(self):
#         print

# class Dog:
#
#     # Class obj attribute
#     # Same for every instance of the class
#
#     species = "Memo" # class obj attr
#
#     def __init__(self, breed, name, spots):
#
#         # Attributes
#         # We take in the argument
#         # Assign it using self.attribute_name
#
#         self.breed = breed
#         self.name = name
#
#         # Expects a boolean True or False
#
#         self.spots = spots
#     # Operations and actions ( methods )
#
#     def bark(self, number):
#         return "woof! My name is {} and my number is {}".format(self.name, number)
#
# my_Dog = Dog(breed="Lab", name="Sparky", spots=True)
# # var = my_Dog.breed
# # var2 = my_Dog.name
# # var3 = my_Dog.spots
# var4 = my_Dog.bark(2)
# # print(var)
# # print(var2)
# # print(var3)
# print(var4)

# class Circle:
#     pi = 3.14 # class obj attr
#
#     def __init__(self, radius=1):
#
#         self.radius = radius
#         self.area = radius * radius * Circle.pi # referince of a class obj attr
#
#     # Metode
#
#     def get_circumference(self):
#         return self.radius * Circle.pi * 2
#
# my_circle = Circle()
# print(my_circle.get_circumference())
# print(my_circle.area)
#
