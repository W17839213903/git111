from 空间.data.数据 import duqu
import time
from 空间.config.空间登录 import 登录
import unittest
import HTMLTestRunnertest
from time import sleep

class 空间空(unittest.TestCase,登录):
    shuju = duqu()
    def test_1(self):
        dr = 登录().denglu()
        dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        sleep(2)
        dr.find_element_by_xpath('//*[@id="u"]').send_keys(int(self.shuju[0][0]))
        sleep(2)
        dr.find_element_by_xpath('//*[@id="p"]').send_keys(self.shuju[0][1])
        sleep(2)
        dr.find_element_by_xpath('//*[@id="login_button"]').click()
        sleep(2)
        wd = dr.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/h1/i').is_enabled()
        self.assertEqual(wd,False)
        dr.quit()
    def test_2(self):
        dr = 登录().denglu()
        for i in range(1,len(self.shuju)):

            # dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
            # sleep(2)
            dr.find_element_by_xpath('//*[@id="u"]').send_keys(int(self.shuju[i][0]))
            sleep(2)
            dr.find_element_by_xpath('//*[@id="p"]').send_keys(self.shuju[i][1])
            sleep(2)
            dr.find_element_by_xpath('//*[@id="login_button"]').click()
            cd = dr.find_element_by_xpath('/html/body/div[1]/div[2]/div/div[1]/h1/i')
            self.assertEqual(cd,True)
            dr.quit()
if __name__ == '__main__':
    unittest.main()
