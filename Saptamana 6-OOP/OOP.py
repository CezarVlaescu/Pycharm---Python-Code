class Super:
    def __init__(self, name='Alexandra'):
        self.nume = name
    def __str__(self):
        return f"Numele meu este {self.nume}"

class Mijloc:

    variabila_mijloc = 3
    super_variabila = 'mijloc'

    def __init__(self, name):
        self.variabila = 11

class Sub(Super, Mijloc):

    sub_variabila = 'sub'
    def __init__(self, nume="Alina"):
        super().__init__(nume)
        # self.variabila = 12

obiect = Sub("Lavinia") # clasa instantiata pentru obiect (Sub)
# print(obiect.super_variabila)
print(obiect.variabila)