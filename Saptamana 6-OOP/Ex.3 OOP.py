class Catalog_Auto():
    def __init__(self, marca, tip):
        self.marca = marca
        self.tip = tip
        self.culoare = None

    def adaugare_culoare(self, culoare):
        self.culoare = culoare
        return self.culoare

    def afisare_culoare(self):
        return self.culoare

class Prorietati(Catalog_Auto):
    def __init__(self, marca, tip):
        super().__init__(marca, tip)
        self.scaune_incalzite = True
    def scaune(self, vreau):
        self.scaune_incalzite = vreau
        return self.scaune_incalzite
    def __str__(self):
        return f'Masina este de tip {self.tip}, marca {self.marca}, culoare {self.culoare} si are scaune incalzite {self.scaune_incalzite}'

class Blocuri(Prorietati):
    def __init__(self, marca, tip):
        super().__init__(marca, tip)
        self.Blocuri_Optice_Led = False

    def bloc(self, Blocuri_Optice_Led):
        self.Blocuri_Optice_Led = Blocuri_Optice_Led
        return self.Blocuri_Optice_Led
    def __str__(self):
        return f'Masina este de tip {self.tip}, marca {self.marca}, culoare {self.culoare} si are blocuri optice {self.Blocuri_Optice_Led} '

obj1 = Prorietati('Aro','M461')
# obj1.scaune(False)
obj1.scaune_incalzite = False
obj1.adaugare_culoare('rosu')
print(obj1.__dict__)
print(obj1)

obj2 = Blocuri('Dacia','1310')
obj2.Blocuri_Optice_Led = False
obj2.adaugare_culoare('negru')
print(obj2.__dict__)
print(obj2)

print(obj2.Blocuri_Optice_Led, obj2.culoare, obj2.marca, obj2.tip)
print(obj1.culoare, obj1.tip, obj1.marca, obj1.scaune_incalzite)




