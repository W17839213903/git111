# from appium import webdriver
# import time
#
#
# #启动设备 连接设备
#
#
# desired_caps = {'platformName':'Android',     # 平台
#                 'platfromVersion':'6.2',      #版本    可不写   默认最新版
#                 'deviceName':'127.0.0.1:62001',    #连接的服务器地址
#                 'appPackage':'com.ss.android.ugc.aweme',    #测试的安装包
#                 'appActivity':'splash.SplashActivity'}     # 安装包的attivity
#
# driver = webdriver.Remote('htp://localhost:4723/wd/hub',desired_caps)
# time.sleep(3)
#
# print('点击抽屉屏幕')
# driver.find_element_by_id('')



# from appium import webdriver
# import time
# import unittest
# adc = {'platformName':'Android',
#        # 'platformVersion':'7.1',
#        'deviceName':'793f130b',
#        'appPackage':'com.netease.cloudmusic',
#        'appActivity':'activity.LoadingActivity'}
# driver = webdriver.Remote('http://localhost:4723/wd/hub',adc)
# time.sleep(5)
#
# print('立即体验')
# driver.find_element_by_id('com.netease.cloudmusic:id/mx').click()
# time.sleep(5)
#
# print('点击抽屉菜单')
# driver.find_element_by_id('com.netease.cloudmusic:id/py').click()
# time.sleep(5)
#
# print('立即登录')
# driver.find_element_by_id('com.netease.cloudmusic:id/abx').click()
# time.sleep(5)
#
# print('手机号登录')
# driver.find_element_by_class_name('android.widget.TextView').click()
# time.sleep(5)
#
# print('输入手机号')
# driver.find_element_by_id('com.netease.cloudmusic:id/i4').send_keys('17839217829')
# time.sleep(5)
#
# print('输入密码')
# driver.find_element_by_id('com.netease.cloudmusic:id/i2').send_keys('123456')
# time.sleep(5)
#
# print('登录')
# driver.find_element_by_id('com.netease.cloudmusic:id/pt').click()
# time.sleep(5)
#
# # wd = driver.find_element_by_id('com.netease.cloudmusic:id/ah9').is_enabled()
#
#
# driver.quit()








from appium import webdriver
import time,unittest

class Login(unittest.TestCase):
    def setUp(self):
        desired_caps = {'platformName': 'Android',
   #                'platformVersion':'6.0',
                    'deviceName': '793f130b',
                    'appPackage': 'com.netease.cloudmusic',
                    'appActivity': 'activity.LoadingActivity'}
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        time.sleep(20)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):

        print("立即体验")
        self.driver.find_element_by_id("com.netease.cloudmusic:id/mx").click()
        time.sleep(6)

        print("点击抽屉菜单")
        self.driver.find_element_by_id("com.netease.cloudmusic:id/py").click()
        time.sleep(5)

        print("立即登录")
        self.driver.find_element_by_id("com.netease.cloudmusic:id/abx").click()
        time.sleep(3)

        print("手机号登录")
        self.driver.find_element_by_id("com.netease.cloudmusic:id/pt").click()
        time.sleep(3)

        print("输入手机号")
        self.driver.find_element_by_id("com.netease.cloudmusic:id/i4").send_keys("15537831769")
        time.sleep(3)

        print("输入密码")
        self.driver.find_element_by_id("com.netease.cloudmusic:id/i2").send_keys("gao19930903")
        time.sleep(3)

        print("登录")
        self.driver.find_element_by_id("com.netease.cloudmusic:id/pt").click()
        time.sleep(3)

        # 断言
        print("点击抽屉菜单")
        self.driver.find_element_by_id("com.netease.cloudmusic:id/py").click()
        time.sleep(2)
        title = self.driver.find_element_by_id("com.netease.cloudmusic:id/ac2")
        self.assertEqual(title.text, "用户507297819")
        print("登陆成功")

    def test_login2(self):
        print("执行第二条测试")
        print("立即体验")
        self.driver.find_element_by_id("com.netease.cloudmusic:id/mx").click()
        time.sleep(6)

        print("点击抽屉菜单")
        self.driver.find_element_by_id("com.netease.cloudmusic:id/py").click()
        time.sleep(5)

        print("立即登录")
        self.driver.find_element_by_id("com.netease.cloudmusic:id/abx").click()
        time.sleep(3)

        print("手机号登录")
        self.driver.find_element_by_id("com.netease.cloudmusic:id/pt").click()
        time.sleep(3)

        print("输入手机号")
        self.driver.find_element_by_id("com.netease.cloudmusic:id/i4").send_keys("15537831769")
        time.sleep(3)

        print("输入密码")
        self.driver.find_element_by_id("com.netease.cloudmusic:id/i2").send_keys("19930903")
        time.sleep(3)

        print("登录")
        self.driver.find_element_by_id("com.netease.cloudmusic:id/pt").click()
        time.sleep(5)

        title = self.driver.find_element_by_id('com.netease.cloudmusic:id/pt')
        self.assertEqual(title.text, "登录")
        print("登陆失败")

if __name__ == '__main__':
    unittest.main()







