from selenium import webdriver
from time import sleep
from 空间.data.数据 import duqu

class 登录():
    shuju = duqu()
    # print(shuju)
    def denglu(self):
        dr = webdriver.Firefox()
        dr.get('http://qzone.qq.com/')
        sleep(2)
        dr.switch_to.frame("login_frame")
        sleep(2)
        dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        sleep(2)
        return dr

# 登录().denglu()
