#TODO 1. : load image          
#TODO 2. : image save          
#TODO 3. : image data collect  

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import cv2


product = "텀블러"

driver = webdriver.Chrome('webcrwaling/chromedriver.exe')
url = "https://shopping.naver.com/home"
driver.get(url)
time.sleep(1)
search_textarea = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div[1]/div[1]/input").send_keys(product)
time.sleep(1)
search_button = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/div/div/div[2]/div/div[2]/div/div[2]/form/fieldset/div[1]/div[1]/button[2]").click()
time.sleep(10)

product_img = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[1]/li/div/div[1]/div/a/img").get_attribute("src")
time.sleep(10)
print(product_img)
# cv2.imread(product_img,cv2.IMREAD_COLOR)
# cv2.waitKey()
# cv2.destroyAllWindows
driver.close

