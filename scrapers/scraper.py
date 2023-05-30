from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import pandas as pd
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome('chromedriver_win32/chromedriver.exe')
# base_url = str("https://www.biogro.co.nz/find-inputs-for-organic-production-free")
base_url = str("https://biogroportal.powerappsportals.com/certified-inputs-free/")
# Specific to the case
columns = ["Input", "BioGro #", "Licensee", "Type", "Category", "Sub Type"]

def get_table(driver):
    time.sleep(5)
    # Clean table
    table = pd.read_html(str(BeautifulSoup(driver.page_source, 'html.parser')))[0]
    table.columns = columns
    return table

# Get URL
driver.get(base_url)

# First page
table = get_table(driver)

# Counter
count = 1

# Every next page
while count <= 117:
    # Find next button
    elm = driver.find_element(By.CSS_SELECTOR, '[aria-label="Next page"]')
    # Click if not disabled
    if 'disabled' in elm.get_attribute('class'):
        break
    elm.click()
    # Collect new table
    table = pd.concat([table, get_table(driver)], ignore_index=True)
    #table = table.append(get_table(driver), ignore_index=True)

    # For user
    count += 1
    print("At page number: ", count)
    print("Number of rows: ", table.count())
    print()

table.to_csv("inputs.csv", index=False)
