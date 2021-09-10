from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from price_parser import Price
from bs4 import BeautifulSoup
import time
import re

class Scrapper:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.browser = webdriver.Chrome('chromedriver', options=self.options)

    def shutdown(self):
        self.browser.quit()

    def shopee(self, url, type):
        self.browser.get(url)

        s = time.time()
        try:
            WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, "randomstring"))
            )
        except Exception as e:
            print(e)
        finally:
            pass
        print(time.time() - s)

        html = self.browser.page_source
        soup = BeautifulSoup(html, "html.parser")

        result = {}
        if type == 'item':
            result = self.shopee_item(soup)
        if type == 'shop':
            result = self.shopee_shop(soup)

        # browser.quit()
        return result
    
    def shopee_item(self, soup):
        result = {}

        try:
            name = soup.find("div", class_="attM6y")
            result['name'] = name.get_text()
            price = soup.find("div", class_="Ybrg9j")
            result['price'] = Price.fromstring(price.get_text()).amount_float
            stock = soup.find("div", class_="_90fTvx")
            result['stock'] = int(re.search(r'tersisa (.*?) buah', str(stock)).group(1))
            desc = soup.find("div", class_="_3yZnxJ")
            result['desc'] = desc.get_text()
            main_img = soup.find("div", class_="_3Q7kBy")
            result['main_img'] = re.search(r'url\("(.*?)"\);', str(main_img["style"])).group(1)
            imgs = soup.findAll("div", class_="_12uy03")
            list_img = []
            for img in imgs:
                list_img.append(re.search(r'url\("(.*?)"\);', str(img["style"])).group(1))
            result["imgs"] = list_img
            # category = soup.find("div", class_="")
            # weight = soup.find("div", class_="")
        except Exception as e:
            print(e)
        
        return result

    def shopee_shop(self, soup):
        result = {}

        try:
            name = soup.find("h1", class_="section-seller-overview-horizontal__portrait-name")
            result['name'] = name.get_text()
            logo = soup.find("img", class_="shopee-avatar__img")
            result['logo'] = logo['src']
            pcount = soup.find("div", class_="section-seller-overview__item-text-value")
            result['product_count'] = int(pcount.get_text())
            tagline = soup.find("div", class_="shop-page-shop-description").find("span")
            result['tagline'] = tagline.get_text()
        except Exception as e:
            print(e)
            
        return result
