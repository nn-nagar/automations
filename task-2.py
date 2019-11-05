from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pynput.keyboard import Key,Controller
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import csv

driver=webdriver.Firefox()
driver.get("https://www.youtube.com/watch?v=nEg6EydnqLA&feature=youtu.be")
time.sleep(2)
elm = driver.find_element_by_xpath('//button[@class="ytp-play-button ytp-button"]')

elm.click()
time.sleep(2)


