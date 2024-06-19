import bs4
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
soup = bs4.BeautifulSoup(response.text, "html.parser")
address_list = [item.text.split("           ")[3].removesuffix("\n") for item in soup.find_all(name="address")]
price_list = [item.text.split("+")[0].removesuffix("/mo") for item in soup.find_all(class_="PropertyCardWrapper_"
                                                                                           "_StyledPriceLine")]
anchor_tags = soup.find_all(name='a')
temp_list = [item['href'] for item in anchor_tags]
link_list = temp_list[9:]
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=os.environ.get('GOOGLE_FORM'))
for i in range(len(price_list)):
    time.sleep(1)
    (driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]'
                                         '/div/div[1]/input')).send_keys(address_list[i])
    (driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div'
                                         '/div[1]/input')).send_keys(price_list[i])
    (driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div'
                                         '/div[1]/input')).send_keys(link_list[i])
    (driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')).click()
    (driver.find_element(By.CSS_SELECTOR, value="div a")).click()
