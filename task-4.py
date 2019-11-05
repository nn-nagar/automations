from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pynput.keyboard import Key,Controller
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import csv

driver=webdriver.Firefox()
driver.get(" https://www.sonyliv.com/")
time.sleep(10)
elm = driver.find_element_by_xpath('//img[@src="https://resources.sonyliv.com/image/fetch/h_254,w_438,c_fill,fl_lossy,f_auto,q_auto,e_contrast:30,e_brightness:10/http%3A%2F%2Fsetindiapd.brightcove.com.edgesuite.net%2F5182475815001%2F2019%2F11%2F5182475815001_6100422112001_6100416836001-th.jpg%3FpubId%3D5182475815001%26videoId%3D6100416836001"]')
elm.click()


time.sleep(300)  #After 5 Min




element = driver.find_element_by_xpath('//span[@class="vjs-icon-placeholder"]')

element.click()
time.sleep(3)

