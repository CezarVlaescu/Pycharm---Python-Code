class Student():
    def __init__(self, nume, absente, *note):
        self.note = note
        self.absente = absente
        self.nume = nume
    def __str__(self):
        return f'Studentul {self.nume} are notele {self.note} si {self.absente} absente'
    def media_artitmetica(self):
        for i in self.note:
            m = sum(i)/2
            return m


obj = Student('Gheorghe', 3, 8, 9, 6)
print(obj)
obj2 = Student('Vasile', 2, [6, 7, 8])
print(obj2.media_artitmetica())