import pandas as pd

# a = {"x": 1, "y": 7, "z": 2}
# variabila = pd.Series(a, index=['x','y'])
# print(variabila)

# data= {
#     "key1": [0,1,2],
#     "key2": [3,4,5]
# }
# variabila = pd.DataFrame(data, index=['linie1', 'linie2', 'linie3'])
# print(variabila.loc['linie2'])
# df = pd.read_excel('CursBnrBis.xls')
# for x in df.index:
#     if float(df.loc[x,'AED']) < 1.2:
#         df.drop(x, implace=True)
# # print(df.corr()) ( corelatia )
# print(df.describe)(afiseaza o matrice)

# import matplotlib.pyplot as plot
# df.plot(kind="scatter", x='AED', y='100 HUF')
# plot.show()

df = pd.read_csv('test.csv')
# df.dropna(implace=True)
df.fillna(0, inplace=True)
# df['AL'].fillna(0,inplace=True)
df.replace(':', 0, inplace=True)
df.replace(':', 0, inplace=True)
print(df.transpose())
df.to_excel('test1.xls')


