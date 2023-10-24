from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

import undetected_chromedriver as uc
import pandas as pd
import csv


def rbc_parser():
    #options = uc.ChromeOptions()
    # browser = uc.Chrome(options=options)
    option = webdriver.ChromeOptions()
    option.add_argument('--headless')
    option.add_argument('--no-sandbox')
    option.add_argument("--window-size=2560,1440")
    form = 'https://companies.rbc.ru/id/1027700229193-ooo-yandeks/'
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)
    browser.get(str(form + '#finance'))

    result = []

    info = browser.find_element("xpath", "/html/body/div[6]/main/div[2]/div[1]/div/div[3]/div/div[2]/table/tbody/tr[2]")
    result.append(info.text.split('\n'))
    return result[0][-1]


print(rbc_parser())