# This program will open google website and then click on Gmail tab
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import schedule
import random

seconds = random.randint(4,10)

def open_gmail():
    driver_path = "C:/Users/Avi/Desktop/Python CWH/My_Folder/chromedriver_win32/chromedriver.exe"
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

    option = webdriver.ChromeOptions()
    option.binary_location = brave_path
    # option.add_argument("--incognito") OPTIONAL
    # option.add_argument("--headless") OPTIONAL

    # Create new Instance of Chrome
    browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

    browser.get("https://www.google.com/")
    time.sleep(5)
    button = browser.find_element("link text", "Gmail")
    button.click()
    time.sleep(15)
    browser.close()

schedule.every(4).seconds.do(open_gmail)

while 1:
    schedule.run_pending()
    time.sleep(seconds)