#review : selector repair
#TODO : selector repair  


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
import json


driver = webdriver.Chrome('webcrawling/chromedriver')
url = "https://shopping.naver.com/home"
driver.get(url = url)

product = "텀블러"
search_box = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input").send_keys(product)
time.sleep(1)
search_button = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/form/div[1]/div/button[2]").click()
time.sleep(1)

review_button = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]/div[3]/div[1]/div[1]/div[1]/div[1]/a[4]").click()
time.sleep(1)
product_box = "/html/body/div/div/div[2]/div[2]/div[3]/div[1]/ul/div"
product_box_child = "/li/div/div[2]/div[1]/a"
product_box_price = "/li/div/div[2]/div[2]/strong/span/span[1]/span"
product_box_price2 = "/li/div/div[2]/div[2]/strong/span/span/span[2]"
product_box_review = "/li/div/div[2]/div[5]/a/em"
# product_name = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[1]/li/div/div[2]/div[1]/a").text
# product_price = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[1]/li/div/div[2]/div[2]/strong/span/span[1]/span").text
# product_link = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[1]/li/div/div[2]/div[1]/a").get_attribute("href")
# product_review = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[1]/li/div/div[2]/div[5]/a").text.replace("리뷰","")

result = {
    'name':[],
    'price':[],
    'link' : [],
    'review':[]
}

for i in range(1,5):
    product_box_path = "/div[{}]".format(i)
    product_name = driver.find_element(By.XPATH, product_box + product_box_path + product_box_child).text
    product_price = driver.find_element(By.XPATH,product_box+product_box_path+product_box_price).text
    if(product_price=='최저'):
        product_price = driver.find_element(By.XPATH,product_box+product_box_path+product_box_price2).text
    product_link = driver.find_element(By.XPATH,product_box+product_box_path+product_box_child).get_attribute("href")
    product_review = driver.find_element(By.XPATH,product_box+product_box_path+product_box_review).text.replace("리뷰","")
    result['name'].append(product_name)
    result['price'].append(product_price)
    result['link'].append(product_link)
    result['review'].append(product_review)
time.sleep(10)

with open("webcrwaling/test.json", "w", encoding='utf-8') as json_file:
    json.dump(result,json_file, indent="\t")



driver.close()

