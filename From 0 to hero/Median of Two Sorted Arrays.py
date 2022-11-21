Lista1 = [1, 3]
Lista2 = [2, 4]

Merged = Lista1 + Lista2
Merged1 = sorted(Merged)
# print(Merged1)
i = 1
for i in Merged1:
    if Merged1[i] > 0:
        var = (Merged1[i] + Merged1[i+1]) / 2
        print(var)









