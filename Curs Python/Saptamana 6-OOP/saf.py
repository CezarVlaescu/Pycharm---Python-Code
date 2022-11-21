# Tom is a bif cat that sleeps all day
# object name = Tom ('noun')
# class name = Cat ('noun')
# property = cat_size (big) ('adjective'/'adverb') is the property through which we identify object
# activity = sleep() ('verb') it is the action that the object does


# a Ferrari car goes fast

# object name = Ferari
# class name = car
# property = fast
# activity = goes

# The dog Max has 4 legs and barks loudly

# object name = Max
# class name = dog
# property = 4 legs (property annexed to the class), loudly (property annexed to the activity)
# activity = barks


class Dog():
    # the bracket is for inheritance, each class we create in Python inherits the default object 'object'
    pass
    # the class doesn't inherit anything and doesn't do anything

object_1 = Dog()
# we created an object based on a class
# we created a class instance
# what is written in the brackets are usually class attributes

print(object_1)

# stack = []
#
# def push(val):
#     stack.append(val)
#
# push(3)
# push(2)
# push(1)
# print(stack)
#
# def pop():
#     value = stack [-1]
#     del stack[-1]
#     return value
#
# print(pop())
# print(pop())
# print(pop())

class Stack:

    def __init__(self):
        # constructor that is used when instantiating class

        self.__stackList = []
        #         by adding 2 underscores, it makes the variable private
        # we cannot access the variable as easily by just saying: 'stack_object.stackList'
        # this is called encapsulation

#         makes the variable val 1 accessible in the below methods

    def push(self, val):
        # method of the class, which we can use the stackList
        self.__stackList.append(val)
        print(self.__stackList)

    def pop(self):
        # method of the class
        value = self.__stackList[-1]
        del self.__stackList[-1]
        return value


stack_object = Stack()
# we just instantiated the class Stack by using the object stack_object, when
# we do this, we access the variable of the class: empty stackList
# we first do this, instantiating class

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

# we can then use the methods defined in the class AFTER instantiating the object

print(stack_object.stackList)



class Stack2:

    def __init__(self, val1):
        # constructor that is used when instantiating class

        self.__stackList = []
        #         by adding 2 underscores, it makes the variable private
        # we cannot access the variable as easily by just saying: 'stack_object.stackList'
        # this is called encapsulation
        self.valoare1 = val1
#         makes the variable val 1 accessible in the below methods

    def push(self):
        # method of the class, which we can use the stackList
        self.__stackList.append(self.valoare1)
        print(self.valoare1)

    def pop(self):
        # method of the class
        value = self.__stackList[-1]
        del self.__stackList[-1]
        return value

stack_object2 = Stack2(4)
# if we mentioned 'valoare1' in constructor, and thus in 'self.__stackList.append(self.valoare1)'
# when we want to call the methods, we don't have to mention the value parameter
# in the method calls, but it's enough to mention it only in the object call

stack_object2.push()

print(stack_object2.pop())


class Stack3:

    def __init__(self, *val2):
        # constructor that is used when instantiating class

        self.__stackList = []
        #         by adding 2 underscores, it makes the variable private
        # we cannot access the variable as easily by just saying: 'stack_object.stackList'
        # this is called encapsulation
        self.valoare2 = val2
#         makes the variable val 1 accessible in the below methods

    def push(self):
        self.__stackList =[val for val in self.valoare2]
        # method of the class, which we can use the stackList
        print(self.valoare2)

    def pop(self):
        # method of the class
        value = self.__stackList[-1]
        del self.__stackList[-1]
        return value

stack_object3 = Stack3(3, 4, 5)

class Example:
    __counter = 0
    # class-level property, because it is defined OUTSIDE (before) methods

    def __init__(self, val=1):
        self.__first = val
        # this is a property, a private one due to the __
        # self.first = val
    #     if we have BOTH this one and the one above, because the __
    # is an access variable for private usage, so python views these first as
    # 2 separate variables

    #     if we give val a value in brackets of _init_, we don't need to input
    # anything when calling object_1

        Example.__counter += 1
    #     the fact that we use Example.__counter (the fact that we use class name)
    # means that each time we instantiate the class, the __counter property applies, adn the count increases
    # but if we used self.__counter, the count would have remained 1 no matter how many objects we create by instantiating
    # the Example class


    def set_second(self, val_2):
        self.second = val_2
        return self.second


object_1 = Example()
print(object_1)
object_2 = Example(2)

print(object_1.set_second(4))
print(object_1.__dict__)
# we want to display the object_1, for which we called the set_second function
# and then we want the output to be put in a dictionary

print(object_2.__dict__)

print(object_1.__first)
# this won't work: we can't access the private-defined variavle '__first'
# but if we want to access it:
print(object_1.Example__first)

# by using print(object_1.__dict__), we can have the '__first' property displayed
# as Example__first within the newly-formed dictionary

object_3 = Example()
object_4 = Example()
object_5 = Example()
object_5 = Example()

print(object_1.__dict__, object_1.Example__counter)
print(object_1.__dict__, object_2.Example__counter)
print(object_1.__dict__, object_3.Example__counter)
print(object_1.__dict__, object_4.Example__counter)

class Example:
    __counter = 0

    # class-level property, because it is defined OUTSIDE (before) methods

    def __init__(self, val=1):

        # this is a property, a private one due to the __
        # self.first = val
        #     if we have BOTH this one and the one above, because the __
        # is an access variable for private usage, so python views these first as
        # 2 separate variables

        #     if we give val a value in brackets of _init_, we don't need to input
        # anything when calling object_1

        if val % 2 !=0:
            self.a = 1
        else:
            self.b = 1
#         in this way, we define which attribute the constructor has, either b or a based on val's value

object_1 = Example(2)
try:
    print(object_1.a)
except AttributeError:
    pass
try:
    print(object_1.b)
except AttributeError:


 print(hasattr(Example, '__counter'))
#     this is to check if object has certain property

object_1 = Example(2)
print(hasattr(object_1, 'a'))
print(hasattr(object_1, 'b'))

# checking which property the object has based on the class if we input val=2

print(object_1.__dict__)
# this tells us the properties of the class/object but it puts them in dictionary form
print(object_1.b)

print(Example.__dict__)

class Vehicles:
    pass

class Cars (Vehicles):
    pass

class OffRoadCars (Cars):
    pass

vehicle_1 = Vehicles()
car_1 = Cars()
off_road_car_1 = OffRoadCars ()

print (issubclass(Vehicles, OffRoadCars))
# checks if Vehicles is a child of OffRoadCars cars
print(isinstance(car_1, Vehicles))
# checks if car_1 is an instance of Vehicles class

class Example1:
    def __init__(self, val):
        self.val = val

ob1 = Example1(0)
ob2 = Example1(2)
ob3 = ob1
ob3.val += 1

print(ob1 is ob2)
print(ob2 is ob3)
print(ob3 is ob1)

str1 = 'Ana are mere '
str2 = 'Ana are mere mari'
str1 += 'mari'
print(str1 == str2, str1 is str2)
# the first is True, because '==' checks ONLY for value equality
# while 'is' checks for BOTH equality of value but also of variable (also checks if the 2 variables have the
# same location in computer memory

class SuperClass:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'My name is {self.name}'

class SubClass(SuperClass):
    def __init__(self, name):
        SuperClass.__init__(self, name)
        # THIS is how we make the constructor of a subclass
        # self.name = name
    #     THIS, instead of line 50 wouldn't be enough to define a sub-class constructor
    # the name attribute is not from SELF, but it comes FROM super-class

    def __str__(self):
        return self.name

object = SubClass()
print(object)