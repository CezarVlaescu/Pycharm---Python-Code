x = [10, 20, 20, 20]
y = [10, 20, 30, 40]
z = [10, 30, 40, 20]

target = 70

for i in range(0, 4):
    if x[i] + y[i] + z[i] == target:
        print(x[i], y[i], z[i])



