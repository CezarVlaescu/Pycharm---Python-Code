# cuvant = 'o n o n a t o p e e'
# cuvant = 'o _ o _ _ _ o _ e e'
# 7 incercari

cuvant_initial = 'onomatopee'.lower()
cuvant = list('onomatopee')
print(cuvant)
for i in range(len(cuvant)) :
    if cuvant[i] != cuvant[0] and cuvant[i] != cuvant[-1]:
        # print(cuvant[0], cuvant[-1], cuvant[i])
        cuvant[i] = '_'
print(cuvant)
numar_incercari = 1
litere_incercate = set()
while numar_incercari <= 7 :
    litera = input("Alege o litera: ").lower()
    if litera in cuvant_initial and (litera == cuvant_initial[0] and litera == cuvant_initial[-1]):
        for index, valoare in enumerate(cuvant_initial):
            if litera == valoare:
                cuvant[index] = litera
    else :
        if litera == cuvant_initial[0] or litera == cuvant_initial[-1]:
            print("Ai incercat prima sau ultima litera")
        else:

            if litera not in litere_incercate:
                numar_incercari = numar_incercari + 1
                print('Litera a fost deja incercata. Ai incercat literele', ",".join(litere_incercate))
            litere_incercate.add(litera)
            if len(list(litere_incercate)) > 7:
                print(f"Ai pierdut! Cuvantul initial era : {cuvant_initial}")
                break
        if '_' not in cuvant:
            print("Ai castigat")
            break
    print(cuvant, f"Mai ai {7 - len(list(litere_incercate))} incercari")

print(cuvant)
