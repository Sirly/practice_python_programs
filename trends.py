from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Firefox()

def wait():
    page_state = browser.execute_script('return document.readyState;')
    while page_state != 'complete':
        page_state = browser.execute_script('return document.readyState;')
        
year = 2009
month = 1
while year < 2017:
    url = 'https://trends.google.com/trends/explore?date={}-01-01%20{}-12-31&q=bitcoin'.format(year,year)
    browser.get(url)
    wait()
    browser.find_element_by_xpath("//button[@ng-click='setupClickOutside()']").click()
    wait()
    browser.find_element_by_xpath("//button[@ng-click='export()']").click()
