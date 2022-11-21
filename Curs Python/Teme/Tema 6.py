import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def date_acquisition(day):
    return f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{day}-ianuarie-ora-13-00/"

date = [20, 21, 23, 24, 25, 26]

def create_table_body():
    table_format = {'County Code': [], 'County': []}
    for day in date:
        table_format[f"{day}.01"] = []
    return table_format

table_format = create_table_body()

def init_table_static_data(day):

    website_url = date_acquisition(day)
    browser.get(website_url)

    table = browser.find_element(by=By.XPATH, value='//table[1]')
    rows = table.text.split("\n")

    # table_XPATH = f"//*[@id=\"post-28974\"]/div/div/table[1]/tbody/tr[{0}]/td[{1}]"

    for i, row in enumerate(rows[1:43]):
        print(row)
        # values = row.split(' ')
        # print(values)
        table_format['County Code'].append(row.split(' ')[0])
        table_format['County'].append(row.split(' ')[1])


init_table_static_data(date[0])

def complete_case_number():

    for day in date:
        website_url = date_acquisition(day)
        browser.get(website_url)

        table = browser.find_element(by=By.XPATH, value='//table[1]')
        rows = table.text.split("\n")

        # table_XPATH = f"//*[@id=\"post-28974\"]/div/div/table[1]/tbody/tr[{0}]/td[3]"

        for i, row in enumerate(rows[1:43]):
            print(row)
            table_format[f"{day}.01"].append(row.split(' ')[2])


complete_case_number()
print(table_format)

df = pd.DataFrame(table_format)
writer = pd.ExcelWriter('covid statistics.xls', engine='xlswriter')
df.to_excel(writer, sheet_name='covid statistics', index=False)
writer.save()













