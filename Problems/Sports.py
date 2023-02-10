name = input("The name : ")
n = int(input("Number of people: "))
players = {}
for i in range(n):
    name = input('Name ')
    size = input('Size ')
    players[name] = size
    if name in players:
        print(players[name])
    else:
        print("There is too much")