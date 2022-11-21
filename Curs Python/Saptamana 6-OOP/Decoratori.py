# class Dog:
#     legs_no = 4  # variabila de clasa / atribut de clasa
#     def __init__(self, name):
#         self.__name = name
#
#     # def change_name(self,name):
#     #     self.name = name
#     #     return self.name
#
#     @property
#     def nume(self):
#         return self.__name
#
#     # @staticmethod # nu depinde de instanta clasei ( self )
#     # def speak():
#     #     return "Bark Bark"
#
#     @nume.setter
#     def nume(self, prenume):
#         self.__nume = prenume
#
#     @nume.deleter
#     def nume(self):
#         del self.__nume
#
#     def __str__(self):
#         return str(self.__name)
#
# caine = Dog('Rex') # ( instantiem o clasa )
# rasa = Dog("Max")
# caine.nume = 'John'
# print(caine.nume)
# del caine.nume
# print(caine, caine.name)
# print(rasa)
# print(Dog.name)
# print(caine.change_name("Lisa"))
# print(caine.speak(), Dog.speak())
# caine.legs_no = 3
# print(rasa.legs_no)
# print(caine.legs_no, Dog.legs_no)

# def decorator_simplu(parametru):
#     print(f"Apelam functia {parametru.__name__}")
#     return parametru
#
# # @decorator_simplu  # (denumirea functie devine parametru in decorator)
# def functie_simpla():
#     return "Buna seara"
#
# @decorator_simplu
# def functie_complexa():
#     return "Noapte buna"
#
# # print(functie_simpla())
# # print(functie_complexa())

# Exemplu cu 2 decoratori

# def decorator_depozit(functia_noastra):
#     def ambalaj_no(material):
#         return f"Ambalam produse din {functia_noastra.__name__} cu {material}"
#     return ambalaj_no
#
# @decorator_depozit
# def impachetare_carti(*args):
#     return args
#
# # print(impachetare_carti("Amintiri din copilarie", "Baltagul"))
# print(impachetare_carti("Amintiri din copilarie"))

# Exemplu cu 3 decoratori

# def decorator_depozit(material):
#     def ambalaj_no(functia_noastra):
#         def ambalaj_intern(*carte):
#             return f"Ambalam produse din {functia_noastra.__name__} cu {material} care contine "\
#                    f'carte { ','.join(x for x in carte)}'
#
#         return ambalaj_intern
#     return ambalaj_no
#
# @decorator_depozit('hartie')
# def impachetare_carti(*nume):
#     return nume
#
# print(impachetare_carti("Amintiri din copilarie", "Baltagul"))
# # print(impachetare_carti("Amintiri din copilarie"))

# Problema

# def decorator(simbol):
#   def adauga_simbol(functie):
#       def functie_upper(parametru):
#           return parametru.upper() + simbol if parametru.upper()[-1] == '.' else parametru.upper() + simbol # (concatenare adauga . la finalul propozitie)
#       return functie_upper
#   return adauga_simbol
#
# @decorator(".")
# def functie(propozitie):
#     return propozitie
#
# print(functie('Ana are mere'))

# Problema

# import time
#
# def calculeaza_timpul(functia):
#     def functie_interioara(*param):
#         inceput = time.time()
#         functia(*param)
#         sfarsit = time.time()
#         print(f"Timpul total de executie : {sfarsit - inceput}")
#         return functia(*param)
#     return functie_interioara
#
# @calculeaza_timpul
# def adunare(*args):
#     suma = 0
#     for i in args:
#         suma += i
#     return suma
#
# print(adunare(1, 2, 3))