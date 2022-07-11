# structuri de date
#Liste - ordonate/mutabile
my_list = [8,2,'a',8,'4']
#my_list.pop()
#print(my_list) eliminare ultimul element din lista
# print('Mesaj')
# print(type(my_list)) # tipul unei variabile
# print(my_list[2])
# print(my_list[-1])
# print(len(my_list))
#my_list.append('CEZAR')
# print(my_list)
# print(my_list.index(8))
#my_list.insert(7, 'A')
# print(my_list[2:5])
#my_list.append(['A', 'B',3,'x',[4,7,'w']])
#print(my_list[7][4][2])
# print(my_list[2:])
# print(my_list[2::3])

#Tupluri - ordonate/imutabile(nu pot fi modificate)

#my_tuple = (8,2,'a',8,'4')
#zile_anului = ('luni','marti','miercuri','joi','vineri') nu se repeta
#zile_anului = tuple()
#print(type(zile_anului))

#lista_1 = ('George', 'Ion', 'Mihai', 'Ana', 'Ovidiu')

#lista_2 = list(lista_1)
#lista_2[1] = 'Razvan'
#lista_1 = tuple(lista_2)
#print(lista_1) ( Adaugare element in tuplu )

#(razvan, gigel, ionel) = lista_1
#print(razvan)
#print(gigel)
#print(ionel) (inlocuirea unor elemente cu altele in tupluri)

#Seturi - neordonabile/imutabile ( nu pot fi indexate sau modificate )

#set_1 = {'mar', 'para', 'banana'}
#print(set_1)
#new_set = set(my_list)
#print(new_set) Transformare lista in set

#Dictionare - ordonate/mutabile
#dict_1 = dict()
#dict_2 = {'key_1': 'valoare',
#           'key_2': 'valoare',
#           3: [1,2,3],
#           4: ('valoare_1', 'val_2') ,
#           'dict_b': {'dict_c': 3}}
#
#print(dict_2) exemplu de dictionar

# Conditionari

# varsta = int(input("Va rugam sa introduceti varsta dvs.: "))
# if varsta >= 18:
# #     print("Sunteti major")
# # else:
# #     print("Sunteti minor")
# #     if varsta == 17:
# #         print("Inca un an pana sunteti major")

# if varsta >= 65:
#     print("Varsta pensionare")
# elif varsta >=25:
#     print("Varsta facultate")
# elif varsta >=15:
#     print("Varsta liceu")
# else:
#     print("esti micut")

# varsta = True
# varsta_1 = None, 0, ''
#
# if not varsta_1 :
#     print(1)
# else:
#     print(2)

# WHILE

# print('primul print')
# i = 0
# while i < 3:
#     print('se respecta conditia')
#     print('valoarea este: ' + str(i))
#     i += 1
#     i = i + 1
# print('am ajuns la sfarsit')

#FOR

# list_1 = [1,2,3,4,5,6,7,8,9]
# for i in list_1:
#     i += 1 ( pentru fiecare i din lista_1 aduna 1)
#     list_1.append(i)
# print(list_1)

#Alte exemple cu IF

# my_var = 7
# mesaj = "Set instructiuni #3"
# if my_var < 6:
#     mesaj = "Set intructiuni #1"
# else:
#     mesaj = "Set intructiuni #2"
#
# print(my_var, mesaj)

# my_var = 7
# mesaj = "set instructiuni"
# if my_var < 6 and (mesaj := my_var):
#     print(mesaj)
# print(my_var, mesaj)

# sir = "Ana are mere"
# # for i, v in enumerate(sir):
# #     print(v, '=>>', i)
# for variabila_temporara in range(2, len(sir)):
#     print(variabila_temporara, "=>>" sir(variabila_temporara))

# dictionar = {'1': 'val', "2": "val2", "3":"val3", "2":"val22"}
# print(dictionar["2"])
# print(dictionar.get("2")) (accesarea unui index dintr-un dictionar)

# print(dictionar["2"]) ( afiseaza ultima valoare )

# dictionar[6] = 'val15'
# print(dictionar) (alta metoda de a adauga in dictionar o valoare)

# for i in dictionar.keys():
#     print(i)
# print(dictionar) ( ne afiseaza cheile, daca punem valorile pune .values, daca vrem ambele .items )

# for i in dictionar.items():
#     print(i, '=>>')
#     index, value = i
#     print(i, index, '=>>', value)

# for i in dictionar:
#     print(i, '->>', dictionar[i])
# print(dictionar)
