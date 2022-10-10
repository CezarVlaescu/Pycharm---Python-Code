# Se dă un şir cu cel mult 10 caractere. Să se determine câte vocale conţine

# Cuvant = input("Scrie un cuvant : ")
# Vocale = ['a', 'e', 'i', 'o', 'u', 'ă', 'â']
# for i in list(Cuvant):
#     if len(Cuvant)<10 and i in Vocale:
#         a = list(i)
#         print(len(list(i)))
#     elif len(Cuvant) >= 10 :
#         print('Cuvant prea lung')

vocale = ['a', 'e', 'i', 'o', 'u']
Cuvant = input("Scrieti un cuvant : ")
var = 0
for litera in Cuvant :
    if litera in vocale and len(Cuvant)<10:
        var += 1
print(var)








