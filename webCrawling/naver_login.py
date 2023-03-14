#REVIEW : auto login fail


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
#---------------------------------------
driver = webdriver.Chrome('webcrwaling/chromedriver')
url = "https://www.naver.com"
driver.get(url)
login_button = driver.find_element(By.CSS_SELECTOR,"#account > a")
login_button.click()

time.sleep(1)

user_id = driver.find_element(By.NAME, "id").send_keys("id")
user_pw = driver.find_element(By.NAME, "pw").send_keys("pw")
time.sleep(1)
login_sign_button = driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div[1]/form/ul/li/div/div[7]/button")
login_sign_button.click()
time.sleep(1)