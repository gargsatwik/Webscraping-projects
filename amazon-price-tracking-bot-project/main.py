import smtplib
import requests
import bs4
import os

URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"  #TEST LINK
AIM_PRICE = 100000              #TEST PRICE
MY_EMAIL = os.environ.get('MY_EMAIL')
PASSWORD = os.environ.get('PASSWORD')

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/121.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
}

response = requests.get(url=URL, headers=headers).text
soup = bs4.BeautifulSoup(response, "html.parser")
price = float(soup.find(class_="a-offscreen").getText().split("$")[1])
title = str(soup.find(id="productTitle").getText())

if price < AIM_PRICE:
    FINAL_MESSAGE = (f"Subject:Time to shop\n\n{title} is now {price}\n{URL}".encode("UTF-8"))
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=os.environ.get('TO_ADDRESS'),
                            msg=FINAL_MESSAGE)
