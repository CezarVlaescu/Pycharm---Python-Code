cnp = input('Introdu CNP : ')

def funct(a):
    if int(a[0]) in range(1,10):
        if int(a[0]) in my_sliced_list:
            return 'CNP M'
    return 'CNP F'
my_list = [1,2,3,4,5,6,7,8,9]
my_sliced_list = my_list[::2]
a = cnp[0]
print(funct(a))


def nastere_1(cnp):

    if int(cnp[0]) in [1,2]:
        return 'Nascut intre 1990-1999'
    elif int(cnp[0]) in [3,4]:
        return 'Nascut intre 1800-1899'
    elif int(cnp[0]) in [5,6]:
        return 'Nascut intre 2000-2029'
    elif int(cnp[0]) in [7,8]:
        return 'Persoana rezisenta'
    elif int(cnp[0]) == 9:
        return 'Strain'

print(nastere_1(cnp))

def oras(cnp):
    orase_numere = {'01': 'Alba', '02': 'Arad', '03': 'Arges', '04': 'Bacau', '05': 'Bihor', '06': 'Bistrita',
                    '08': 'Brasov'}
    if cnp[7:9] in orase_numere.keys():
        return orase_numere[cnp[7:9]]
print(oras(cnp))

def validare(cnp):
    if len(cnp) == 13 and cnp.isdigit() is True:
        return "CNP Valid"
    return "CNP Invalid"
print(validare(cnp))








