from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import json

# 1. Khai báo browser
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"E:\chromedriver_win32\chromedriver.exe")

# 2. Mở URL của post
driver.get("https://www.agoda.com/vi-vn/search?city=2758")

sleep(15)

n = 0
arr = []

SCROLL_PAUSE_TIME = 10

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height
sleep(5)

elements = driver.find_elements_by_css_selector('.PropertyCard.PropertyCardItem a')
sites = [el.get_attribute("href") for el in elements]
# print(sites)
n = n+len(sites)
print(n)
arr +=sites

# with open('links.json', 'w') as wr:
#     json.dump(sites, wr)

sleep(5)
showmore_link = driver.find_element_by_css_selector("#paginationNext")
showmore_link.click()

# 6. Đóng browser
# driver.close()

def next_page():
        elements = driver.find_elements_by_css_selector('.PropertyCard.PropertyCardItem a')
        sites = [el.get_attribute("href") for el in elements]
        global n
        global arr
        n = n+len(sites)
        print(n)
        arr+=sites
        sleep(10)
        showmore_link = driver.find_element_by_css_selector("#paginationNext")
        showmore_link.click()


def scroll_page():
        last_height = driver.execute_script("return document.body.scrollHeight")
        while True:
            # Scroll down to bottom
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script(
                "return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        sleep(10)

while True:
        scroll_page()
        next_page()
        if showmore_link ==[] :
             break

with open('links.json', 'w') as wr:
            json.dump(arr, wr)