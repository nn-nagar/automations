from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pynput.keyboard import Key,Controller
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import csv

driver=webdriver.Firefox()
#driver = webdriver.Chrome(executable_path="C:\\Users\\hp\Desktop\\chromedriver.exe")
#driver = webdriver.Firefox(executable_path="C:\\Users\\hp\\Downloads\\geckodriver-v0.9.0-win64\\geckodriver.exe")
driver.get("https://www.wego.com/")
#time.sleep(20)
currentUrl = driver.current_url
#elm = driver.find_element_by_css_selector("#searchKeywordInput")
elm = driver.find_element_by_xpath('//input[@id="searchKeywordInput"]')[0]
#elm = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "searchKeywordInput")))
elm.click()
time.sleep(2)

elm.send_keys("pune")

elm2 = driver.find_element_by_xpath('//input[@placeholder="From"]')
elm2.click()
time.sleep(2)


# driver.get("https://www.zomato.com/pune")


# element = driver.find_element_by_xpath('//input[@id="keywords_input"]')

# element.click()
# time.sleep(3)
# element.send_keys("McDonald's")
# time.sleep(3)

# element.send_keys(Keys.DOWN)
# time.sleep(3)

# element.send_keys(Keys.ENTER)
# time.sleep(3)

# print(driver.current_url)
# currentUrl = driver.current_url

# driver.get(currentUrl)