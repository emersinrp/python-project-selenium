import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://google.com")
browser.maximize_window()
time.sleep(2)
