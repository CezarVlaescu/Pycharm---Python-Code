def suma(x,y):
    return x + y
def scadere(x,y):
    return x - y
def impartire(x,y):
    return x / y
def inmultire(x,y):
    return x * y

print('Selectarea operatiei')
print('1.Suma')
print('2.Scadere')
print('3.Impartire')
print('4.Inmultire')

def validare(numar_1):
    while not numar_1.isdigit():
        numar_1 = input('Introdu alt numar: ')
    return float(numar_1)
while True:
    Alegere = input("Alege o operatie(1/2/3/4): ")
    if Alegere in ('1','2','3','4'):
        numar_1 = validare(input("Primul numar = "))
        numar_2 = validare(input("Al doilea nuamr = "))
        if Alegere == '1':
            print(numar_1, "+", numar_2, "=", suma(numar_1,numar_2))
        elif Alegere == '2':
            print(numar_1, "-", numar_2, "=", scadere(numar_1,numar_2))
        elif Alegere == '3':
            print(numar_1,"/",numar_2,"=",impartire(numar_1,numar_2))
        elif Alegere == '4':
            print(numar_1,"*",numar_2,"=",impartire(numar_1,numar_2))
        continuare = input("Doriti sa continuati = ")
        if continuare == 'nu':
            break
    else:
        print('Valoarea este gresita')