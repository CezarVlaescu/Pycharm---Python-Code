import csv
from itertools import groupby

header = ['full_name', 'email', 'location']

names = [
   ['Anita', 'anita@email.com', 'California'],
   ['Aron', 'aron.bla@email.com', 'California'],
   ['Aron', 'aron.bla@email.com', 'California'],
   ['Cosmin', 'kox@bla.com', 'Giurgiu'],
   ['Crina', 'ggl@test.com', 'Letcani'],
   ['Bogdan', 'vox@example.com', 'Resita']
]

result = []
for i in names:
   if i not in result:
      result.append(i)

# print(result)

# with open('input.csv', 'w') as f:
#    writer = csv.writer(f)
#    writer.writerow(header)
#    writer.writerows(names)  --> Write the input

mydict = {}
for k, g in groupby(result, key=lambda x: x[0][0]):
   if k in mydict:
      mydict[k] += g
   else:
      mydict[k] = list(g)

for key in sorted(mydict):
   new = ("%s: %s" % (key, mydict[key]))
   print(new)


with open('output.csv', 'w') as f:
   writer = csv.writer(f)
   writer.writerow(sorted(mydict.keys()))
   writer.writerows(sorted(mydict.values()))
