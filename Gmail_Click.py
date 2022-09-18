from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import schedule

def gmail_click():
    
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get('https://www.google.com/')
    time.sleep(5)
    button = browser.find_element("link text", "Gmail")
    button.click()
    time.sleep(15)
    browser.close()

schedule.every(4).seconds.do(gmail_click)

while 1:
    schedule.run_pending()
    time.sleep(5)