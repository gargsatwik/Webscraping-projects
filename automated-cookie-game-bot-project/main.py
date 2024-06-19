from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def upgrades():
    available_money = int(driver.find_element(By.ID, value="money").text.replace(",", ""))
    upgrades_list = driver.find_elements(By.CSS_SELECTOR, value="#store b")
    cost_list = [item.text.split("\n") for item in upgrades_list]
    costs = []
    for i in range(len(cost_list) - 1):
        costs.append(int(cost_list[i][0].split(" - ")[1].replace(",", "")))
    if costs[7] <= available_money:
        driver.find_element(By.ID, value="buyTime machine").click()
    elif costs[6] <= available_money:
        driver.find_element(By.ID, value="buyPortal").click()
    elif costs[5] <= available_money:
        driver.find_element(By.ID, value="buyAlchemy lab").click()
    elif costs[4] <= available_money:
        driver.find_element(By.ID, value="buyShipment").click()
    elif costs[3] <= available_money:
        driver.find_element(By.ID, value="buyMine").click()
    elif costs[2] <= available_money:
        driver.find_element(By.ID, value="buyFactory").click()
    elif costs[1] <= available_money:
        driver.find_element(By.ID, value="buyGrandma").click()
    elif costs[0] <= available_money:
        driver.find_element(By.ID, value="buyCursor").click()


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

while True:
    time.sleep(0.01)
    cookie = driver.find_element(By.ID, value="cookie")
    cookie.click()
    upgrades()
