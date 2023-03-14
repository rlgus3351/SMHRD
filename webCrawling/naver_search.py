from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
import json

product = "gaming mouse"


# --------------------------------------------------
driver = webdriver.Chrome('webcrawling/chromedriver')
url = "https://www.naver.com"
driver.get(url)
time.sleep(1)
search_box = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div/div[3]/form/fieldset/div/input").send_keys(product)
search_box_button = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div/div[3]/form/fieldset/button").click()
time.sleep(1)
product_element = "/html/body/div[3]/div[2]/div/div[1]/section[1]/div[1]/div[3]/div[1]/div[1]/ul"
product_element2 = "/div/div/div[1]/div[1]/strong"
product_explain = "/div/div/a"

# 크롤링 결과값 넣을 딕셔녀리형태
result = {
    'name':[],
    'price':[],
}

# 반복문을 통한 값 찾기
for i in range(1,6,1):
    price_path = "/li[{}]".format(i)
    price = driver.find_element(By.XPATH, product_element+price_path+product_element2)
    name = driver.find_element(By.XPATH, product_element+price_path+product_explain)
    result["name"].append(name.text)
    result["price"].append(price.text+"원")

# print(result)
# 가격 표시
for i in range(5):
    price_name = result["name"][i]
    price = result["price"][i] +"원"
    print(f"{price_name}: {price}원")

with open("webcrwaling/product.json", "w", encoding='utf-8') as json_file:
    json.dump(result,json_file, indent="\t")
driver.quit()



