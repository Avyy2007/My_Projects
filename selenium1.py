# This program will run a website on Chrome Browser and click on Vote tab
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import schedule
import random

def vote():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://mycutebaby.in/contest/participant/63256d451b90e?utm_source=wsapp_share&utm_campaign=September_2022&utm_medium=shared&utm_term=wsapp_shared_63256d451b90e&utm_content=participant')
    time.sleep(15)
    button = browser.find_element("link text", "TAP TO VOTE !")
    button.click()
    time.sleep(15)
    browser.close()

schedule.every(5).seconds.do(vote)

while 1:
    sec = random.randint(1980,2100)
    schedule.run_pending()
    time.sleep(1980)