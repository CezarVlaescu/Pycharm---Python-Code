import requests

# SELENIUM IMPORTS
from selenium import webdriver
# most basic import, needed to first have a driver

from selenium.webdriver.chrome.service import Service
# importing the service function
from selenium.webdriver.common.devtools.v102 import page

from webdriver_manager.chrome import ChromeDriverManager
# importing the ChromeDriverManager within the service function
# used for the browser object

from selenium.webdriver.common.by import By
# importing the function with which we find elements by class and ID


# PANDAS

import pandas as pd

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# SELENIUM (for opening page and finding elements)

# A) setting up program options (for Browser)
options = webdriver.ChromeOptions()
# options always needed as an object, but the name varies depending
# on the type of browser we use

options.add_experimental_option('detach', True)
# the add command for the options object is used to keep the chrome page open

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# B) opening page and working with it
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# this automatizes the opening of an URL:
# 1).Chrome is used because it is our current browser
# 2) for chrome, we use the service function, as imported above within the 'service' object
# 3) within this we install the ChromeDriverManager()
# 4) and we give the driver the 'options' as chrome_options
# browser is the object name we use to create a webdriver-type object

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# C) CREATING A FUNCTION FOR URL
# we need to get an url for EACH of the days: 20-26


def date_acquisition(day):
    return f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{day}-ianuarie-ora-13-00/"

# ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# D) INITIALIZING TABLE FORMAT

# a=int(input("Number of elements in the array:-"))
# date=list(map(str, input("Enter dates:-").strip().split()))

date = [20, 21, 23, 24, 25, 26]

def create_table_body():
    table_format = {'County Code': [], 'County': []}
    for day in date:
        table_format[f"{day}.01"] = []
    return table_format


# actually finialzining table format using method
table_format = create_table_body()

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


# E) OBTAINING TABLE FROM WEBSITE

def init_table_static_data(day):

    website_url = date_acquisition(day)
    browser.get(website_url)

    table = browser.find_element(by=By.XPATH, value='//table[1]')
    rows = table.text.split("\n")

    # where 1 is county code, 2 is county name, 3 is total number of cases

    # table_XPATH = f"//*[@id=\"post-28974\"]/div/div/table[1]/tbody/tr[{0}]/td[{1}]"

    for i, row in enumerate(rows[1:43]):
        print(row)
        # values = row.split(' ')
        # print(values)
        table_format['County Code'].append(row.split(' ')[0])
        table_format['County'].append(row.split(' ')[1])


init_table_static_data(date[0])
# literally tell the method which table to take counties and county codes from


def complete_case_number():

    for day in date:
        website_url = date_acquisition(day)
        browser.get(website_url)

        table = browser.find_element(by=By.XPATH, value='//table[1]')
        rows = table.text.split("\n")
     # where 1 is county code, 2 is county name, 3 is total number of cases

        table_XPATH = f"//*[@id=\"post-28974\"]/div/div/table[1]/tbody/tr[{0}]/td[3]"

        for i, row in enumerate(rows[1:43]):
            print(row)
            table_format[f"{day}.01"].append(row.split(' ')[2])


complete_case_number()
print(table_format)

# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# F) CREATING NEW TABLE WITH OBTAINED DATA

# dataframe Name and Age columns
df = pd.DataFrame(table_format)

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('covid statistics.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='covid statistics', index=False)

# Close the Pandas Excel writer and output the Excel file.
writer.save()











