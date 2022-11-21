# Se da sirul de numere n care contine [1, 2, 3, 4, 5, 6, 7]. Sa se insereze in acest sir dupa fiecare element par, dublul acestuia

n = [1,2,3,4,5,6,7]
for i in range(7):
    if i % 2 :
        n[i][i+1] = n[i]*2
print(n)

