# Word = ' c i n g a t o a r e a '
# Word = ' c _ _ _ a _ _ a _ _ a
# 5 incercari

word = list('cingatoarea')
word_completed = 'cingatoarea'.lower()
print(word)
for i in range(len(word)):
    if word[i] != word[0] and word[i] != word[-1]:
        word[i] = '_'
print(word)
numar_incercari = 5
litere_incercate = set()
while numar_incercari <= 5:
    litera = input('Alege o litera : ').lower()
    if litera in range(len(word_completed)) and litera != word_completed[0] and litera != word_completed[-1]:
        for index, valoare in enumerate(word_completed):
            if litera == valoare:
                word[index] = litera
    else:
        if litera == word_completed[0] or litera == word_completed[-1]:
            print('Mai incearca')
print(word_completed)


