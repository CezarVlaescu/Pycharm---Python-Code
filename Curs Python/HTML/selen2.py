from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.bnr.ro/files/xml/nbrfxrates2021.html')

table_head = driver.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/thead')
print(table_head.text)
table_body = driver.find_element(by=By.XPATH, value='//*[@id="Data_table"]/table/body')
print(table_body.text)

header = table_head.text.split('\n')
body = table_body.text.split('\n')

body_rows = []
counter = 0
for i in range(0,len(body), len(header)):
    counter = i
    body_rows.append(body[counter : counter+len(header)])

# print(body_rows, 'AAAAAAAAAA')

# TABEL GENERAT PE COLOANE

# df = pd.DataFrame(body_rows, columns=header)
# with ExcelWriter('TABEL_BNR_2021.xlsx') as writer:
#     df.to_excel(writer, index=0)

# body_columns = []
# for i in range(len(header)):
#     body_columns.append({i: []})
# body_columns_list = len(body_columns)
# counter = 0
# for j in body:
#     body_columns[counter % body_columns_list].append(j)
#     counter += 1