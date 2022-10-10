# Sa se scrie un program care sa calculeze impartirea dintre trei numere. Daca valorile sunt egale, returnati de trei ori rezultatul. Impartirea la 0 va duce la rezultatul 0

def impartire(a,b,c):
    if a != b != c:
       return a/b/c
    elif a == b == c:
        return (a/b/c)*3
    elif a == 0 or b == 0 or c == 0:
        return 0

print(impartire())












