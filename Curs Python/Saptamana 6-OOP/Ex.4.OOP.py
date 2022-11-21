class Calcul():
    def __init__(self, a=1, b=2, c=3, d=4):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def calcul(self):
        return (self.a * (self.b + 3) / self.c) * self.d

    def __str__(self):
        return f'( {self.a} * ( {self.b} + 3 )  / {self.c} ) * {self.d} = {self.calcul()}'

cal = Calcul()
print(cal)
obj1 = Calcul(3,5,7,9)
print(obj1)
obj2 = Calcul(2,4,6,8)
print(obj2)

obj3 = Calcul('ion', 3, 4, 5)
print(obj3)