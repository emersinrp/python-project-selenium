import time
from selenium import webdriver

browser = webdriver.Chrome()

# get()
browser.get("https://www.google.com/")

# maximize_window()
browser.maximize_window()

# refresh()
browser.refresh()

# get()
browser.get("https://www.saucedemo.com/")
time.sleep(2)

# back()
browser.back()
time.sleep(2)

# forward()
browser.forward()
time.sleep(2)

# #switch_to - abrir nova janela ou aba
# browser.switch_to.new_window("tab")
# time.sleep(2)
#
# # close()
# browser.close() #fecha a janela ou aba que esta rodando no momento
# time.sleep(2)

# quit()
browser.switch_to.new_window("tab")
browser.switch_to.new_window("tab")
time.sleep(2)
browser.quit()
