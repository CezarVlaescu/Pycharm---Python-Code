# <head> </head> (informatia despre pagina)
# <body> </body> (o sa tina informatia )

#intre aceste doua taguri se structureaza pagina web

#<table>
# <thead>
# <tr>  (randuri)
# <th>  (coloane)
# </th>
# </tr>
# <td></td>
# </thead>
# <tbody>
# <tfoot>
# </tfoot>
# </tbody>
#</table>
import pandas as pd
import requests
from bs4 import BeautifulSoup


req = requests.get('https://www.bnr.ro/Cursul-de-schimb--7372.aspx')  # colecteaza informatia de pe acea pagina
link = BeautifulSoup(req.text, 'html.parser')

main = link.find_all('div', attrs={'id' : 'contentDiv'})
# print(main)
header_list = []
dataset = []
for obj in main:
    for table_index in obj.find_all('table'):
        # print(table_index)
        for table_trs in table_index.find_all('tr'):
            # print(table_trs)
            td_list = []
            if table_trs.find_all('th'):
                header_list = [header_data.get_text() for header_data in table_trs.find_all('th')]
                # for header_data in table_trs.find_all('th'):
                #     header_list.append(header_data.get_text())
            for index, td in enumerate(table_trs.find_all('td')):
                if index == 0:
                  td_list.append(td.get_text())
                elif td.get_text() != '':
                  td_list.append(float(td.get_text().replace(',','.')))
            dataset.append(td_list)
del dataset[0]
# print(header_list,'header')
# print(dataset)

df = pd.DataFrame(dataset, columns=header_list, index=range(1,11))
print(df)
df.to_excel("CursBNR.xls", header=header_list)

# print(header_list)

