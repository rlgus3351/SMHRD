#todo : 네이버 검색창에 "봄여행" 키워드를 입력한 후 검색을 실행하세요.


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
# ---------------------------------------------------------------------------------------------------------------------------------------------------

keyword = '봄여행'
url = "https://www.naver.com"
driver = webdriver.Chrome("webcrawling/chromedriver")
driver.get(url)
time.sleep(1)
search_box= driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div/div[3]/form/fieldset/div/input").send_keys(keyword)
time.sleep(1)
serach_button = driver.find_element(By.XPATH,"/html/body/div[2]/div[2]/div[1]/div/div[3]/form/fieldset/button").click()
test_url = driver.page_source
soup = BeautifulSoup(test_url, 'lxml')
print(soup)
