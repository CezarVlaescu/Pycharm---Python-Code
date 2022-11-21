# file = open('data.txt','r+')
# file.write("hello ana")
# file.close() # ( inchidere fisier )

# r (read) -> citim, nu adaugam informatie, este valoarea cu care vine default(functia open),daca fisierul nu exista apare eroarea
# w (write) -> scriem in fisier, daca nu exista fisierul il adauga
# a (append) -> scriem in fisier, daca exista ceva in fisier, adauga la final ( ca append la siruri )
# r+ -> deschide fisierul cu drept de scriere, citire

# file = open('data1.txt', 'w')
# try:
#     file.write("hello")
# finally:
#     file.close()

# with open('data2.txt', 'w') as file :
#     file.write("Hello 2")

# with open('data.txt', 'r') as file:
#     for line in file.readlines():
#         print(line)

# with open('data.txt', 'r') as file:
#     while True:
#         line = file.readline()
#         if not line:
#             break
#         print(line)

import csv

# with open('fisiercsv.csv', 'r') as csv_file:
#     rows = csv.reader(csv_file, delimiter=',')
#     for row in rows:
#         print(row)

# new_cars = [
#     ['Dacia', 'Logan', 2005,75],
#     ['Renault', 'Clio', 2005, 75]
# ]
# with open('fisiercsv.csv', 'a') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter=',')
#     for new_car in new_cars:
#         csv_writer.writerow(new_car) # adaugarea unor elemente noi in coloane


