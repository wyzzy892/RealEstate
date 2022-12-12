# import asyncio
# from playwright.async_api import async_playwright
# from playwright.sync_api import sync_playwright
import json
from selenium.webdriver.common.by import By
from selenium import webdriver

def main():
    parsed = []
    try:
        page = webdriver.Chrome()
        for page_num in range(1, 101):
            print("page",page_num)
            page.get(f'https://www.avito.ru/kazan/kvartiry/prodam-ASgBAgICAUSSA8YQ?cd=1&p={page_num}')
            # print("wait element !!!!!!!!")
            # page.wait_for_selector('div[data-marker="item"]')
            # print("elemet find!!!!!!!")

            links = page.find_elements(By.XPATH, '//*[@data-marker="item"]/div/div[2]/div[2]/a')
            for item in links:
                parsed.append(
                        {
                            "href": item.get_attribute("href"),
                            "page": page_num
                        }
                    )
    except:
        pass    

    return parsed


data = main()
with open('data.json', 'w') as fp:
    json.dump(data, fp)
