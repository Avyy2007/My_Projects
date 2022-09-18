# This program will run a website on Brave Browser and click on Vote tab
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import schedule
import random

def vote():
    driver_path = "C:/Users/Avi/Desktop/Python CWH/My_Folder/chromedriver_win32/chromedriver.exe"
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

    option = webdriver.ChromeOptions()
    option.binary_location = brave_path
    # option.add_argument("--incognito") OPTIONAL
    # option.add_argument("--headless") OPTIONAL

    # Create new Instance of Chrome
    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

    browser.get('https://mycutebaby.in/contest/participant/63256d451b90e?utm_source=wsapp_share&utm_campaign=September_2022&utm_medium=shared&utm_term=wsapp_shared_63256d451b90e&utm_content=participant')
    time.sleep(15)
    button = browser.find_element("link text", "TAP TO VOTE !")
    button.click()
    time.sleep(15)
    browser.close()

schedule.every(4).seconds.do(vote)

while 1:
    sec = random.randint(1980,2100)
    schedule.run_pending()
    time.sleep(sec)