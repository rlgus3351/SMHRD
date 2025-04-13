// import requests
from bs4 import BeautifulSoup
import html.parser

URL = "https://www.amazon.com/Logitech-Backlit-Mechanical-Keyboard-Passthrough/dp/B06XR5MWGM/ref=sr_1_5?crid=2EWPQ5LV86SNJ&keywords=logitech+keyboard+913&qid=1662290785&sprefix=logitech+keyboard+%2Caps%2C657&sr=8-5"
headers = { 'Accept-Language' : "en-US",
            'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"}
        
response = requests.get(url=URL, headers=headers)
soup = BeautifulSoup(response.text, "lxml")
price=soup.find("span", class_ = "a-offscreen").getText()