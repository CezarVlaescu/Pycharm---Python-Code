# numar_mere = 3
# var1 = f"Ana are {numar_mere} mere"
# print(var1)

# var1 = f"Ana are {'22' if numar_mere > 4 else '33'}" mere {numar_mere}
# print(var1)

# numar_mere = 3
# numar_pere = 2
# var1 = "Ana are {} mere si {} pere".format(numar_mere, numar_pere)
# print(var1)

# numar_mere = 3
# numar_pere = 2
# var1 = "Ana are {1} mere si {0} pere".format(numar_mere, numar_pere)
# print(var1)

# numar_mere = 3
# numar_pere = 2
# var1 = "Ana are " + str(numar_mere) + " mere si " + str(numar_pere) + " pere"
# print(var1)

# def my_function(a,b):
#     return a + b
#
# suma = my_function(2,3)
# print(suma)

# mere = 3
# pere = 3
# def my_function(a: int, b: int = 0, c: int = 0) -> (int, int): sau def my_function(a: int, ......) -> (int, dict) pentru dictionar
#     return a + b + c, a - b - c
# suma, diferenta = my_function(mere, c = pere, b=2)
# print(suma, diferenta)

# mere = 3
# pere = 3
# def my_function(a: int, b: int = 0, c: int = 0, *args, **kwargs) -> (int, int):
#     return a + b + c, a - b - c
# suma, diferenta = my_function(mere, c = pere, b=2)
# print(suma, diferenta)

# def suma(a,b,*args,**kwargs):
#     """
#
#     :param a: primul parametru
#     :param b: al doilea
#     :param args: argumentul tip tuplu
#     :param kwargs: argumente tip cheie-valoare
#     :return: suma tuturor parametrilor
#     """
#     total = 0
#     variabila_temp = a + b
#     for i in kwargs:
#         total += i
#     print(type(kwargs))
#     for i in kwargs:
#         print(i)
#         total += i
#     return variabila_temp
#
# variabila = suma(1,2,3,4,5, c=4, d=7, e=9)
# print(variabila)

# my_var = input('Adauga un numar : ')
# try :
#     my_int = int(my_var)
#     print(my_int)
# except ValueError:
#     print('eroare de valoare')
# except Exception as e:
#     print('exceptie', e)


