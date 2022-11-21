class Catalog_Prajituri():
    variabila = []
    def __init__(self, nume, pret, gramaj):
        self.nume = nume
        self.pret = pret
        self.gramaj = gramaj

        lista = [self.nume, self.pret, self.gramaj]
        Catalog_Prajituri.variabila.append(lista)

    def afisare_gramaj(self):
        return sorted(self.variabila, key= lambda x: x[2])
        # print([item for item in self.variabila])
    def afisare_pret(self):
        return sorted(self.variabila, key= lambda x: x[1])

    def __str__(self):
        return f'Prajitura este {self.nume}, costa {self.pret} si are un gramaj de {self.gramaj}'

class Tort(Catalog_Prajituri):
    def __init__(self, nume, pret, gramaj, etajat = False, glazura = 'ciocolata'):
        super().__init__(nume, pret, gramaj)
        self.etajat = etajat
        self.glazura = glazura
    def __str__(self):
        return f'Prajitura este {self.nume}, costa {self.pret} si are un gramaj de {self.gramaj} grame, are glazura de {self.glazura} si este etajat {self.etajat}'

class Fursec(Catalog_Prajituri):
    pass


obj1 = Catalog_Prajituri('Amandina', 2, 300)
obj2 = Catalog_Prajituri('Ecler', 3, 200)
obj3 = Catalog_Prajituri('Cremes', 4, 400)


print(obj1)
print(obj2)
print(obj3)
print(obj3.afisare_gramaj())
print(obj3.afisare_pret())

obj4 = Tort('Elena', 10, 100, False, glazura='vanilie')
obj5 = Tort('Ana', 20, 300, True, glazura='capsuni')
obj6 = Tort('Sonia', 30, 500, True, glazura='ciocolata')

print(obj4)
print(obj5)
print(obj6)

obj4.etajat = True
print(obj4)
obj4.glazura = 'cacao'

obj7 = Fursec('Fursec ciocolata', 20, 100)
obj8 = Fursec('Fursec vanilie', 40, 500)
obj9 = Fursec('Fursec capsuni', 60, 300)

print(obj7)
print(obj8)
print(obj9)









