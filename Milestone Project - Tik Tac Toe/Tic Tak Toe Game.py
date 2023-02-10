import random

print('Hi, my name is Caesar and this is my Tik Tac Toe Game \n Ready to play : [Yes] or [No]')

def choice(decision):
    if decision == 'Yes':
        return 'Good, game on'
    elif decision == 'No':
        return 'Have a nice day'

decision = input('Answer : ')
print(choice(decision))

row1 = ['', '', '']
row2 = ['', '', '']
row3 = ['', '', '']

def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

display(row1, row2, row3)

print("Select the player from this : player [X] or player [O]")
def players_selection(var):
    nums = [1, 2]
    player_count = random.choices(nums)
    if var == 'X':
        return 'You are player {}'.format(player_count)
    elif var == 'O':
        return 'You are player {}'.format(player_count)

var = input("Your choice : ")
print(players_selection(var))

round = 0
def rounds(round):
    while round < 9:
        round =+ 1
        return "Round {}".format(round)
print(rounds(round))










