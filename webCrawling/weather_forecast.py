from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pyperclip
#---------------------------------------
driver = webdriver.Chrome('webcrwaling/chromedriver')
url = "https://weather.naver.com/today"
driver.get(url)
temperature = driver.find_element(By.CSS_SELECTOR,"#now > div > div.weather_area > div.weather_now > div > strong")
print(temperature.text)