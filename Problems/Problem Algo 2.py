def make_list(number):
    names = []
    for item in number:
        names.append(input("Enter : "))
    print(names)

number = int(input("How many : "))
names = make_list(number)
for name in names:
    if name[1] == 'a':
        print('Yes')



