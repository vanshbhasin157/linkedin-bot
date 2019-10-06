from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
# import pyautogui as pag


browser = webdriver.Firefox()
browser.get('https://www.linkedin.com/home/?originalSubdomain=in')
browser.find_element_by_class_name("nav__button-secondary").click()
# for x in range(1):
user = browser.find_element_by_xpath("""//*[@id="username"]""")
user.send_keys("username")
password = browser.find_element_by_xpath("""//*[@id="password"]""")
password.send_keys("password")
browser.find_element_by_xpath("""//*[@id="app__container"]/main/div/form/div[3]/button""").click()
print("signed in")
search = browser.find_element_by_xpath("""//*[@id="ember34"]/input""")
search.send_keys(Keys.ENTER)
# apply_filter = browser.find_element_by_xpath("""//*[@id="ember11048"]""").click()
time.sleep(1)
if browser.find_element_by_xpath("""//*[@id="ember190"]""") == 
    
