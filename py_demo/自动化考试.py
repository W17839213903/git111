from selenium import webdriver
from time import sleep
import re
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui

dr = webdriver.Chrome()
dr.get('http://qzone.qq.com/')
sleep(2)
dr.switch_to.frame("login_frame")
sleep(2)
dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
sleep(2)
dr.find_element_by_xpath('//*[@id="u"]').send_keys('1497462492')
sleep(2)
dr.find_element_by_xpath('//*[@id="p"]').send_keys('')
sleep(2)
dr.find_element_by_xpath('//*[@id="login_button"]').click()
wd1 = dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
dr.switch_to.frame(wd1)
start = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
sleep(2)
ActionChains(dr).drag_and_drop_by_offset(start,200,0).perform()