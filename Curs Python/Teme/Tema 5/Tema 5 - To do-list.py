import csv
import datetime
import pandas as pd


def introducere_categorii():

    while True:
        with open('categorii.txt', 'a') as file:
            file.write(f'{input("Adauga categoria: ")} \n')
            decizie = input("Doriti sa introduceti o alta categorie? (Y/N)").lower()
            if decizie == 'n':
                break
    return True

introducere_categorii()

def validare_data(data_limita):
    try:
        datetime.datetime.strptime(data_limita, '%d-%m-%Y %H:%M')
        return True
    except Exception:
        return False

def introducerea_taskurilor():
    while True:
        with open('taskuri.csv', 'a') as file:
            csv_writer = csv.writer(file, delimiter=',')
            task = input('Adauga un task: ')
            data_limita = input('Adauga o data limita: ')
            validarea_datei = validare_data(data_limita)
            while validarea_datei is False:
                print("Data nu are formatul corect")
                data_limita= input('Adaugati o noua data: ')
                validarea_datei = validare_data(data_limita)
                if validarea_datei is True:
                    break
            responsabil = input('Adauga persoana responsabila: ')
            categoria = input("Adauga categoria: ")
            with open('categorii.txt', 'r') as file:
               line = file.readlines()
            verificare = categoria.strip()
            new_list = [x.strip() for x in line]
            while verificare not in new_list:
                intr_categ = input('Categorie inexistenta. Reintrodu o alta categorie: ')
                if intr_categ:
                    categoria = intr_categ
                if intr_categ.strip() in new_list:
                    break
            csv_writer.writerow([task, data_limita, responsabil, categoria])
        decizie = input("Doriti sa introduceti un alt task? (Y/N)").lower()
        print(decizie)
        if decizie == 'n':
            break

    return True
introducerea_taskurilor()




def sortare_ascendenta_task():
    df = pd.read_csv('taskuri.csv', names = ['Task', 'Data', 'Responsabil', 'Categorie'], index_col='Task')
    return df.sort_index(ascending=True)

def sortare_descendenta_task():
    df = pd.read_csv('taskuri.csv', names=['Task', 'Data', 'Responsabil', 'Categorie'], index_col='Task')
    return df.sort_index(ascending=False)

def sortare_ascedenta_data():
    df = pd.read_csv('taskuri.csv', names=['Task', 'Data', 'Responsabil', 'Categorie'], index_col='Data')
    return df.sort_index(ascending=True)

def sortare_descendenta_data():
    df = pd.read_csv('taskuri.csv', names=['Task', 'Data', 'Responsabil', 'Categorie'], index_col='Data')
    return df.sort_index(ascending=False)

def sortare_ascendenta_responsabil():
    df = pd.read_csv('taskuri.csv', names=['Task', 'Data', 'Responsabil', 'Categorie'], index_col='Responsabil')
    return df.sort_index(ascending=True)

def sortare_descendenta_responsabil():
    df = pd.read_csv('taskuri.csv', names=['Task', 'Data', 'Responsabil', 'Categorie'], index_col='Responsabil')
    return df.sort_index(ascending=False)

def sortare_ascendenta_categorie():
    df = pd.read_csv('taskuri.csv', names=['Task', 'Data', 'Responsabil', 'Categorie'], index_col='Categorie')
    return df.sort_index(ascending=True)

def sortare_descendenta_categorie():
    df = pd.read_csv('taskuri.csv', names=['Task', 'Data', 'Responsabil', 'Categorie'], index_col='Categorie')
    return df.sort_index(ascending=False)

# functie
print("""Metode de sortare: \n
      1. sortare ascendentă task \n
      2. sortare descendentă task \n
      3. sortare ascendentă data task \n
      4. sortare descendentă data \n
      5. sortare ascendentă persoana responsabilă \n
      6. sortare descendentă persoană responsabilă \n
      7. sortare ascendentă categorie \n
      8. sortare descendentă categorie""")

metoda_sortare = input("Alegeti o metoda de sortare: ")

while int(metoda_sortare) not in range(1,9):
    print("Nu exista metoda")
    input_nou = input("Alege o metoda de sortare de la 1 la 8: ")
    metoda_sortare = input_nou
    if int(input_nou) in range(1,9):
        break
if metoda_sortare == '1':
    print(sortare_ascendenta_task())
elif metoda_sortare == '2':
    print(sortare_descendenta_task())
elif metoda_sortare == '3':
    print(sortare_ascedenta_data())
elif metoda_sortare == '4':
    print(sortare_descendenta_data())
elif metoda_sortare == '5':
    print(sortare_ascendenta_responsabil())
elif metoda_sortare == '6':
    print(sortare_descendenta_responsabil())
elif metoda_sortare == '7':
    print(sortare_ascendenta_categorie())
else:
    print(sortare_descendenta_categorie())

print("""Metode de sortare: \n
      1. sortare ascendentă task \n
      2. sortare descendentă task \n
      3. sortare ascendentă data task \n
      4. sortare descendentă data \n
      5. sortare ascendentă persoana responsabilă \n
      6. sortare descendentă persoană responsabilă \n
      7. sortare ascendentă categorie \n
      8. sortare descendentă categorie""")

metoda_sortare = input("Alegeti o metoda de sortare: ")

while int(metoda_sortare) not in range(1,9):
    print("Nu exista metoda")
    input_nou = input("Alege o metoda de sortare de la 1 la 8: ")
    metoda_sortare = input_nou
    if int(input_nou) in range(1,9):
        break
    print(metoda_sortare)

names = ['Task', 'Data', 'Responsabil', 'Categorie']

def sortare(metoda_sortare):
    directie_sortare = True
    if int(metoda_sortare) in range(1,5):
        directie_sortare = True
    elif int(metoda_sortare) in range(5,9):
        directie_sortare = False
        metoda_sortare = int(metoda_sortare) - 5
    df = pd.read_csv('taskuri.csv', names = names, index_col=names[int(metoda_sortare)-1])
    return print(df.sort_index(ascending= directie_sortare))
sortare(metoda_sortare)