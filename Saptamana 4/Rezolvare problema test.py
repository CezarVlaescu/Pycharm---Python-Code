string = "The Inquisitor must meet Varric on top of Skyhold's battlements to be introduced."

patches = [[5, 14, "Conquistador"], [26, 31, "King"], [43, 49, "Palace"]]
patches = sorted(patches,reverse = True)

def functie(*args):
    lista = list(string)
    for i in args[0]:
        lista[i[0]-1:i[1]] = i[2] # inlocuieste ce se afla intre numere din sublista cu elementul(cuvantul) din sublista , ex. Palace intre 43 si 49 )
    return "".join(lista)

print(functie(patches))


lista = ['Maria', 'Irina', 'Claudiu', 'Ionut', 'Irina', 'Matei', 'Irina', 'Maria', 'Claudiu']

lista_sortata = sorted(lista)
print(lista_sortata)

def count(*args):
    occurences = [lista.count(i) for i in lista]
    dictionar = dict(zip(lista, occurences))
    return dictionar
print(count(lista))

def count_max(*args):
    occurences = [lista.count(i) for i in lista]
    dictionar = dict(zip(lista, occurences))
    keymax = max(dictionar, key = lambda x: dictionar[x])
    return keymax
print(count_max(lista))

def count_min(*args):
    occurences = [lista.count(i) for i in lista]
    dictionar = dict(zip(lista, occurences))
    keymin = min(dictionar, key = lambda x: dictionar[x])
    return keymin
print(count_min(lista))



def anagram(a,b):
    if sorted(a) == sorted(b):
        return "Sunt anagrame"
    else:
        return "Nu sunt anagrame"

print(anagram('listen', 'silent'))


print(set(lista))

def palidrom(a):
    if list(a) == list(a)[::-1]:
        return "Este palidrom"
    else:
        return "Nu este palidrom"

print(palidrom('kayak'))


a = [1, 2, 4, 6, 7, 9, 10]
def find_missing(a):
    return [x for x in range(a[0], a[-1]+1) if x not in a]
print(find_missing(a))


def invers(a):
    return ''.join(list(a)[::-1])
print(invers('scoala'))

def permutations(string, step = 0):
    if step == len(string):
        print("".join(string))
    for i in range(step, len(string)):
        string_copy = [c for c in string]
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]
        permutations(string_copy, step + 1)
    return ""
print (permutations ('one'))