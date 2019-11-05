from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pynput.keyboard import Key,Controller
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import csv

driver=webdriver.Firefox()
#driver = webdriver.Firefox(executable_path="C:\\Users\\hp\\Downloads\\geckodriver-v0.9.0-win64\\geckodriver.exe")
driver.get("https://www.facebook.com//")
time.sleep(2)
elm = driver.find_element_by_xpath('//input[@name="email"]')

elm.click()
time.sleep(2)

elm.send_keys("pankajtiwarisgi@gmail.com")

elm1 = driver.find_element_by_xpath('//input[@name="pass"]')

elm1.click()
time.sleep(2)

elm1.send_keys("9015081299")

elm1.send_keys(Keys.ENTER)
time.sleep(3)

