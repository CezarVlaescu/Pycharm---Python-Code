from itertools import groupby



names = [
   ['Anita', 'anita@email.com', 'California'],
   ['Aron', 'aron.bla@email.com', 'California'],
   ['Aron', 'aron.bla@email.com', 'California'],
   ['Cosmin', 'kox@bla.com', 'Giurgiu'],
   ['Crina', 'ggl@test.com', 'Letcani'],
   ['Bogdan', 'vox@example.com', 'Resita']
]

mydict = {}
for k, g in groupby(names, key=lambda x: x[0][0]):
   if k in mydict:
      mydict[k] += g
   else:
      mydict[k] = list(g)

# print(mydict)

for key in sorted(mydict):
   print("%s: %s" % (key, mydict[key]))