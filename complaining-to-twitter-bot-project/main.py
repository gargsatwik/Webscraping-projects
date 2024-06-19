import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')
DOWN = os.environ.get('DOWN')
UP = os.environ.get('UP')

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
driver.get(url="https://www.speedtest.net/")
driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()
time.sleep(60)
actual_down_speed = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                        '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]'
                                                        '/span').text
actual_up_speed = driver.find_element(By.XPATH, value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                                      '/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

TEXT = f"Hi internet provider.Why am i getting {actual_down_speed}/{actual_up_speed} when i was guaranteed {DOWN}/{UP}?"
driver.get(url="https://twitter.com/i/flow/login")
time.sleep(5)
driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div'
                                    '/div/div/div[5]/label/div/div[2]/div/input').send_keys(USERNAME)
time.sleep(0.5)
driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div'
                                    '/div/div/div[6]').click()
time.sleep(1)
driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]'
                                    '/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(PASSWORD)
driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]'
                                    '/div[2]/div/div[1]/div/div/div').click()
time.sleep(4)
driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]'
                                    '/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label'
                                    '/div[1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys(TEXT)

