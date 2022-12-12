import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re

def parser(data, browser):
    browser.get(f'{data["href"]}')

    data_flat = []
    data_building = []
    data_position = []
    data_price = []

    div_about_flat = browser.find_element(By.CSS_SELECTOR, 'div[data-marker="item-view/item-params"]')

    if div_about_flat:
        list_props = div_about_flat.find_element(By.CSS_SELECTOR, 'ul').find_elements(By.CSS_SELECTOR, 'li')
        for  item in list_props:
            data_flat.append(" ".join(item.text.split()).lower())


    div_about_building = browser.find_element(By.CSS_SELECTOR, 'div[class*="style-item-view-house-params"]')
    if div_about_building:
            for item in div_about_building.find_element(By.CSS_SELECTOR, 'ul').find_elements(By.CSS_SELECTOR, 'li'):
                data_building.append(" ".join(item.text.split()).lower())


    div_position = browser.find_elements(By.CSS_SELECTOR, 'span[class*="style-item-address-georeferences-item"]')
    if div_position:
        for item in div_position: 
            data_position.append(" ".join(item.text.split()).lower())

    price = browser.find_element(By.CSS_SELECTOR, 'span[itemprop="price"]')
    if price:
        data_price.append(" ".join(price.get_attribute("content").split()).lower())

    return {
            "url": data["href"],
            "flat": data_flat, 
            "building": data_building, 
            "position":data_position, 
            "price": data_price
            }


with open("data.json") as fp:
    data = json.load(fp)

list_flat_info = []
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('log-level=3')
driver = webdriver.Chrome(chrome_options=options)
for item in data[:]:
    try:
        flat_info = parser(item, driver)
        list_flat_info.append(flat_info)
        with open(f"data_flat_list.json","w") as fp:
            json.dump(list_flat_info, fp)
    except:
        pass



