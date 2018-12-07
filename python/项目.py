from selenium import webdriver
from time import sleep
import re
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui

dr = webdriver.Chrome()
dr.get('http://www.moore.ren/')
dr.maximize_window()
sleep(2)
