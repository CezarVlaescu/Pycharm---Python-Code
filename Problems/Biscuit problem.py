n = int(input('n = '))
character = ['#']
lista = ['', '', '',
         '', '', '',
         '', '', '']
if n == 3:
    lista[n-2] = character
    lista[n] = character
    lista[n+1] = character
    lista[n+2] = character
    lista[n+4] = character

print(lista)

