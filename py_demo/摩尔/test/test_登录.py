from 摩尔.config.摩尔_配置 import 摩尔
from 摩尔.data.test_数据 import duqu
import unittest
from time import sleep

class 摩尔(unittest.TestCase,摩尔):

    shuju = duqu()

    def setUP(self):
        pass

    # def test_1(self):
    #
    #     dr = 摩尔().qingqiu()
    #     dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys(int(self.shuju[0][0]))
    #     sleep(2)
    #     dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys(self.shuju[0][1])
    #     sleep(2)
    #     dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/form/input[1]').click()
    #     until = dr.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/a/img').is_enabled()
    #     self.assertEqual(until,True)
    #     dr.quit()

    def test_2(self):

        for i in range(1,len(self.shuju)):
            dr = 摩尔().qingqiu()
            try:
                self.shuju[i][0] = int(self.shuju[i][0])
                dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys(self.shuju[i][0])
                sleep(2)
                dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys(self.shuju[i][1])
                sleep(2)
                dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/form/input[1]').click()
                sleep(1)
                wd = dr.find_element_by_xpath('//*[@id="userForm"]/div[2]/span').is_enabled()
                self.assertEqual(wd,True)
                dr.find_element_by_xpath('//*[@id="emailInput"]').clear()
                dr.find_element_by_xpath('//*[@id="passwordInput"]').clear()
                dr.quit()
            except:
                dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys(self.shuju[i][0])
                sleep(2)
                dr.find_element_by_xpath('//*[@id="passwordInput"]').send_keys(self.shuju[i][1])
                sleep(2)
                dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[1]/form/input[1]').click()
                sleep(1)
                cd = dr.find_element_by_xpath('//*[@id="userForm"]/div[2]/span').is_enabled()
                self.assertEqual(cd,True)
                dr.find_element_by_xpath('//*[@id="emailInput"]').clear()
                dr.find_element_by_xpath('//*[@id="passwordInput"]').clear()
                sleep(2)
                dr.quit()
if __name__ == '__main__':
    unittest.main()