a = list(map(int, input().split()))
b = []
i = 0
while i < len(a):
    if a[i] == 2 or a[i] == 3:
        b.append(a[i])
        a[i] = 0
    else:
        i += 1
print('a = ', a)
print(len(b))
