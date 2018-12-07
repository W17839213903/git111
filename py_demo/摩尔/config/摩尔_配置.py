from selenium import webdriver
from time import sleep
from 摩尔.data.test_数据 import duqu
class 摩尔():
    shuju = duqu()
    def qingqiu(self):
        url = 'http://www.moore.ren/'
        dr = webdriver.Firefox()
        dr.get(url)
        dr.maximize_window()
        dr.find_element_by_css_selector('body > div.footer20151217 > div.bottom-reg-nav.bottom-float-reg-nav.footer-style > div > div.toLogin > a').click()
        sleep(2)
        wd = dr.window_handles
        sleep(2)
        # print(wd)
        dr.switch_to.window(wd[-1])
        sleep(2)
        # print(dr.current_window_handle)
        # for i,j in self.shuju:
        #     # print(i,j)
        #     try:
        #         i = int(i)
        #         dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys('{}'.format(i))
        #         sleep(2)
        #         dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('{}'.format(j))
        #         sleep(2)
        #         dr.find_element_by_xpath('//*[@id="emailInput"]').clear()
        #         dr.find_element_by_xpath('//*[@id="passwordInput"]').clear()
        #     except:
        #         dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys('{}'.format(i))
        #         sleep(2)
        #         dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys('{}'.format(j))
        #         sleep(2)
        #         dr.find_element_by_xpath('//*[@id="emailInput"]').clear()
        #         dr.find_element_by_xpath('//*[@id="passwordInput"]').clear()
        #         sleep(2)
        return dr


# 摩尔().qingqiu()


