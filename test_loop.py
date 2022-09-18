# from ast import main
# from time import time


import time
import schedule
import random


def vote():
    print("Hello")

schedule.every(4).seconds.do(vote)

while 1:
    sec = random.randint(5,10)
    schedule.run_pending()
    time.sleep(sec)
    print(sec)