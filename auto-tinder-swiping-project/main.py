from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.tinder.com")
time.sleep(5)
driver.find_element(By.XPATH, value='//*[@id="t425926696"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]'
                                    '/div[2]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, value='//*[@id="t-1302454380"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/'
                                    'button').click()
time.sleep(1)
driver.find_element(By.XPATH, value='//*[@id="t-1302454380"]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]'
                                    '/button').click()
time.sleep(1)
base_window = driver.window_handles[0]
fb_login_page = driver.window_handles[1]
driver.switch_to.window(fb_login_page)
time.sleep(1)
driver.find_element(By.ID, value="email").send_keys(os.environ.get('EMAIL'))
driver.find_element(By.ID, value="pass").send_keys(os.environ.get('PASSWORD'))
time.sleep(1)
driver.find_element(By.ID, value="loginbutton").click()
driver.switch_to.window(base_window)
time.sleep(20)

while True:
    time.sleep(2)
    (driver.find_element(By.CSS_SELECTOR, value='button')).click()
