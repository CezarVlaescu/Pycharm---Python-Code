# Max este o pisica mare care doarme toata ziua
# object name = Max ( substantiv )
# class name = Pisica ( substantiv )
# property = mare ( marimea psicii ) ( adjectiv/adverb )
# activity = doarme ( verb )

# O masina Dacia merge repede.
# object name = Dacia
# class name = Masina
# propriety = repede
# activity = merge
#
# class Dog:
#     pass
#
# obiect_1 = Dog()
# print(obiect_1)

stackList = []

def push(val):
    stackList.append(val)

push(3)
push(2)
push(1)
print(stackList)

def pop():
    valoare = stackList[-1]
    del stackList[-1]
    return valoare

print(pop())
print(pop())
print(pop())

class Stack:

    # def __init__(self):
    #     self.__stackList = []

    def __init__(self, *val1):
        # print('Hi')
        self.__stackList = []
        self.valoare1 = val1

    def push(self):
        self.__stackList = [val for val in self.valoare1]
        print(self.valoare1)

    def pop(self):
        valoare = self.__stackList[-1]
        del self.__stackList[-1]
        return valoare


obiect_stiva = Stack()
# print(obiect_stiva.__stackList)
obiect_stiva.push()
print(obiect_stiva.pop())

