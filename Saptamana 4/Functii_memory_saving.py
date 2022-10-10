# functii lambda - se mai numesc si functii anonime (fara def/fara nume)

# element = lambda x: x * 10 # unde x este argumentul si x * 10 este expresie
# element_2 = lambda x,y: x + y
#
""" Filter """
#
#  Program care sa returneze o lista cu numere pare dintr-o lista initiala
#  Functia filter intoarce un obiect al clasei filter rezultat prin aplicarea unei functii fiecarui elem dintr-un obiect(lista, tuplu etc. )
#
# list_1 = [1,5,4,6,11,12]
# list_2 = list(filter(lambda x: (x % 2 == 0), list_1))
# print(list_2)
# print(type(list_2))

# ex cu for loop:
#
# list_forloop = []
# for i in list_1:
#     if i % 2 == 0:
#         list_forloop.append(i)
# print(list_forloop) ( ce am scris mai sus cu lambda )

# ex cu functie clasica

# def filtrare(var):
#     if var % 2 == 0:
#         return True
#     else:
#         return False
#
# filtrari = filter(filtrare, list_1)
# print(list(filtrari)) ( la fel )

""" MAP """

# Functia map intoarce un obiect al clasei map rezultat prin aplicarea unei functii fiecarui elem dintr-un obiect(lista, tuplu etc. )
#
# list_1 = [1,5,4,6,11,12]
# list_3 = list(map(lambda x: x*2 , list_1))
# print(list_3)

""" ZIP """

# Functia Zip preia parametrii iterabili ( pot fi 0 parametrii sau mai multi parametrii ) si returneaza un obiect al clasei Zip ( iterator ) sub forma de tupluri formate din grupuri de elemente provenite din parametrii initiali
# Lungimea finala a obiectului iterabil este egala cu lungimea celei mai scurte structuri initiale.

# list_with_int = [1,2,3,4]
# list_with_str = ['one', 'two','three','four']
# list_with_decimal = [1.1,2.2,3.3]
#
# result = tuple(zip(list_with_int, list_with_str, list_with_decimal))
# print(result)
#
# result = zip()
# print(result)
# result_list = list(result)
# print(result_list)
#
# var_1, var_2, var_3 = zip(*result)
# print('val_1 = ', var_1)
# print('val_2 = ', var_2)
# print('val_3 = ', var_3)

""" COMPREHENSION LIST """

# var = 'comprehension'
#
# list_for_loop = []
# for character in var:
#     list_for_loop.append(character)
# # print(list_for_loop)
#
# # Case lambda
#
# list_map = list(map(lambda x: x, var))
# # print(list_map)
#
# # Case Comprehesion
#
# list_string = [character for character in var] # expresie for item in lista
# # print(list_string)
#
# numers_list = [x for x in range(20) if x % 2 == 0]
# print(numers_list)

""" Comprehension dictionary """

# my_dict = {1:'car', 2:'bike'}

# square_dict = dict()
# for num in range (1,11):
#     square_dict(num) == num*num
# print(square_dict)

# squad_dict = {num: num*num for num in range(1,11)}
# print(square_dict) #( expresie pentru iterator iterabil, ne da patratul )