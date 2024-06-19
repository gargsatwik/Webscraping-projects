from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv


EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')
ACCOUNT = os.environ.get('ACCOUNT')

load_dotenv()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.instagram.com/")
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(EMAIL)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(PASSWORD)
driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
time.sleep(5)
try:
    save_login_prompt = driver.find_element(By.XPATH, "//div[contains(text(), 'Not Now')]")
    save_login_prompt.click()
except:
    pass
try:
    notifications_prompt = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
    notifications_prompt.click()
except:
    pass
driver.find_element(By.CLASS_NAME, 'x1n2onr6').click()
driver.find_element(By.CLASS_NAME, 'x1lugfcp').send_keys(ACCOUNT)
