import pandas as pd
# a = [1,7,2] # afiseaza in coloana numerele si le da pozitii specifice de la 0
# variabila = pd.Series(a, index=["x", "y", "z"]) (series este o coloana din tabel, indexul inlocuieste numerele specifice fiecarui element din coloana cu ce scriem in index)
# print(variabila["y"]) (acceseaza acel element specific indexului)

# taskuri = {"ziua1": 2, "ziua2": 4, "ziua3": 1}
# variabila = pd.Series(taskuri, index=["ziua2", "ziua3"])  (putem vedea doar anumiti indexi)
# print(variabila)

# taskuri = {
#     "zile": [2,4,5],
#     "durata": [50,40,45]  (cheile reprezinta o serie)
# }
# variabila = pd.DataFrame(taskuri)
# print(variabila.loc[[0,1]])  (accesarea unui rand sau mai multe randuri)

df = pd.read_csv('date_test.csv')
print(df)