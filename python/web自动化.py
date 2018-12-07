from selenium import webdriver
from time import sleep
import re
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui

# browser = webdriver.Firefox()
# browser = webdriver.Chrome()
# browser.get('http://www.moore.ren/')      #请求网址
# print('已打开')
# sleep(2)
#获取网站的标题 （title）
# print(browser.title)    #通常来做断言
#
# #获取网站的网址
# print(browser.current_url)   #断言 我请求的网址是否是返回的网址
#
# #设置浏览器的大小    #保证所有的测试用例在同一个环境下去测试
# browser.set_window_size(800,800)
# sleep(5)
#
# #设置浏览器的位置    #保证所有的测试用例在同一个环境下去测试
# browser.set_window_position(350,350)
# sleep(5)


#浏览器的最大化和最小化
# browser.maximize_window()    #浏览器最大化
# sleep(5)

# browser.minimize_window()    #浏览器最小化
# sleep(5)


#浏览器的前进和后退
# browser.get('https://www.jd.com')   #打开京东  休息3秒
# sleep(3)
#
# browser.back()    #后退到凤凰网  休息3秒
# sleep(3)
#
# browser.forward()  #前进道京东  休息3秒
# sleep(3)
#
#
# browser.quit()     #关闭浏览器
# print('已关闭')




# 定位方法   wedriver模拟人的行为   定为单个元素
# 1、通过id属性  定位到id=kw的位置
# （1） 输入
# browser.find_element_by_id('kw').send_keys('美女图片')
# sleep(10)
# # （2） 点击   #找到百度一下的定位框 和id属性
# browser.find_element_by_id('su').click()
# browser.quit()     #关闭浏览器

# 2、通过class属性定位  定位到class=s_ipt 的位置
# browser.find_element_by_class_name('s_ipt').send_keys('美女')
# sleep(5)
# browser.find_element_by_class_name('btn self-btn bg s_btn btnhover').click()


# 3、通过name属性定位  定位到 name = wd的位置
# browser.find_element_by_name('wd').send_keys('美女')
# sleep(5)
# browser.find_element_by_id('su').click()


# browser.find_element_by_id('root').click()
# browser.find_element_by_class_name('zp-search__input').send_keys('软件测试工程师')

# 4、link_text 通过文本定位   保证元素唯一性
# browser.find_element_by_link_text('登录').click()

# 5、partial_link_text  通过模糊文本定为
# browser.find_element_by_partial_link_text('登').click()

# 6、通过标签的名称来定位  tag_name  通常用于多个元素的定位
# browser.find_element_by_tag_name('').click()

# 7、他通过xpath 路径定位   路径标记语言  相对路径 //   绝对路径 /
# xml  可扩展标记语言   xpath 寻找xml的路径   xml作用：存储传输数据     xpath作用：
# browser.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div/span[2]/a').click()
# browser.find_element_by_xpa th('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()

# 8、通过css过滤
# browser.find_element_by_css_selector('#user-nomal > div.login-wrap > div.before-login > li.no-login > a').click()





# 定位多个元素

# wd = browser.find_elements_by_class_name('cate_menu_item')
# print(len(wd))

# 定位多个class属性的值为 menu-box 的元素  数据类型是列表
# 层级定位
# wd = browser.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_tag_name('li')
# print(len(wd))
# wd = browser.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a')
# print(wd)
# for i in wd:
    # ActionChains(browser).move_to_element(i).perform()
    # sleep(2)
# print(wd.get_attribute('rel'))   # 获取某个元素的值
# wd = browser.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').text
# print(wd)






#
#
# dr = webdriver.Chrome()
# dr.get('http://192.168.0.254')
# # sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').clear()
# # sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[1]/input').send_keys('administrator')
# # sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[2]/input').send_keys('Bane@7766')
# # sleep(2)
# a=[]
# for i in range(1,5):
#     wd = dr.find_element_by_xpath('//*[@id="checkinfo"]/img[{}]'.format(i))
#     w = wd.get_attribute('src')
#     a.append(w[-5])
# print(a)
# dr.find_element_by_xpath('//*[@id="input1"]').send_keys('{}{}{}{}'.format(a[0],a[1],a[2],a[3]))
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
# wd = dr.switch_to_alert()   #切换到弹出窗
# sleep(2)
# print(wd.text)   #获取弹出窗上的文本
# wd.accept()
# # dr.switch_to.default_content()
#
# dr.switch_to.parent_frame()
# cd = dr.find_element_by_xpath('//*[@id="mainnav_body"]/table').find_elements_by_class_name('div')
# print(cd)

# for i in cd:
#     if "防火墙" not in cd:
#         i.click()













dr = webdriver.Chrome()
dr.get('http://www.moore.ren/')
sleep(2)
print(dr.current_window_handle)     #获取窗口的句柄
dr.find_element_by_xpath('//*[@id="user-nomal"]/div[3]/div[1]/li[1]/a').click()  #找到登录窗口 会跳转
sleep(2)
# print(dr.current_window_handle)
wd = dr.window_handles   #获取所有的窗口的句柄
dr.switch_to_window(wd[-1])    #切换句柄
print(dr.current_window_handle)
dr.find_element_by_xpath('//*[@id="emailInput"]').send_keys('1111111111111') #在对切换到的句柄进行操作
dr.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/a').send_keys('17839217829')
sleep(2)
dr.find_element_by_xpath('//*[@id="userForm0"]/div[2]/input').send_keys('123456')
sleep(2)
dr.find_element_by_xpath('//*[@id="userForm0"]/div[5]/div[2]').click()




# 框架  镶嵌在web上的一个窗口
# dr = webdriver.Chrome()
# dr.get('https://i.qq.com')
# sleep(2)
# dr.switch_to.frame("login_frame")
# sleep(2)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('1497462492')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="img_out_1454952416"]').click()
#切换到 内嵌框架中  属性  只能根据：id 或者name的值定位到框架 来切换


# dr.switch_to.default_content()   #推出到最原始框架
# dr.switch_to.parent_frame()      #退出到上一个框架


# dr = webdriver.Firefox()
# dr.get('http://jwgl.kfu.edu.cn/jwmis/')
# sleep(2)
# dr.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td[1]/div[1]/table/tbody/tr/td/iframe')
# sleep(2)
# # dr.find_element_by_xpath('//*[@id="Logon"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/select').click()
# # sleep(2)
# dr.find_element_by_xpath('//*[@id="txt_asmcdefsddsd"]').send_keys('123456')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="txt_pewerwedsdfsdff"]').send_keys('123456')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="Button1"]').click()


# dr = webdriver.Chrome()
# dr.get('http://192.168.0.254')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="userLoginBox"]/form/ul/li[4]/input[1]').click()
# sleep(2)
# wd = dr.switch_to_alert()   #切换到弹出窗
# sleep(2)
# print(wd.text)   #获取弹出窗上的文本
#
# wd.accept()   #点击确定
# wd.dismiss()  #点击取消
# wd.send_keys('内容')   #想弹出框输入内容



# dr = webdriver.Chrome()
# a=[]
# dr.get('http://www.alltuu.com/')
# # dr.find_element_by_xpath('//*[@id="loginUsername"]').send_keys('123456789')
# sleep(2)
# dr.maximize_window()
# sleep(2)

#1、、、、
# wd= dr.find_element_by_xpath('/html/body/ul').text
# # print(wd)
# sleep(2)
# a.append(wd)
# b=a[0]
# c = b.split('\n')
# print(c)
# for i in c:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(2)
#     if i == '123456789@189.com':
#         dr.find_element_by_xpath('/html/body/ul/li[5]').click()
#         print('已点击')
#     else:
#         pass

# 2、、、
# wd= dr.find_element_by_xpath('/html/body/ul').find_elements_by_tag_name('li')
# print(wd)
# for i in wd:
#     if '.com' not in wd:
#         i.click()

#var q=document.documentElement.scrollTop=10000
# 控制滚动条的JavaScript代码
# 10000表示的是所有页面的高度 数字越大 滚动条越往下
# 移动滚动条   属于浏览器的  滚动条属于JavaScript脚本
# 1、根据页面的高度来
# for i in range(0,20000,500):
#     js = 'var q=document.documentElement.scrollTop={}'.format(i)    #控制JavaScript
#     sleep(2)
#     dr.execute_script(js)    #执行JavaScript脚本
# 2、根据定位到的元素 移动滚动条
# 定位一个元素
# wd = dr.find_element_by_xpath('//*[@id="app"]/div/div/section/div[2]/div[6]/div/div[3]')
# sleep(2)
# js = 'arguments[0].scrollIntoView()'    #移动到定位到的元素的位置
# sleep(2)
# dr.execute_script(js,wd)    #执行JavaScript脚本


# dr = webdriver.Chrome()
# dr.get('http://qzone.qq.com/')
# sleep(2)
# dr.maximize_window()
# sleep(2)
# dr.switch_to.frame("login_frame")
# sleep(2)
# dr.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="u"]').send_keys('14974692')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="p"]').send_keys('1321')
# sleep(2)
# dr.find_element_by_xpath('//*[@id="login_button"]').click()
# sleep(2)
# wd1 = dr.find_element_by_xpath('//*[@id="newVcodeIframe"]/iframe')
# dr.switch_to_frame(wd1)
#
# start = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
# ActionChains(dr).drag_and_drop_by_offset(start,200,0).perform()
#ActionChains 动作连    drag_移动到的元素  X Y 轴




# from selenium import webdriver
# from time import sleep
# import re
# from selenium.webdriver.common.action_chains import ActionChains
# import selenium.webdriver.support.ui as ui
# dr = webdriver.Chrome()
# dr.get('http://www.moore.ren/')
# dr.maximize_window()
# sleep(2)

# 截图
# dr.get_screenshot_as_png()
# 保存
# dr.save_screenshot('aaaaaaa.png')
# 截图并保存
# dr.get_screenshot_as_file('aaaaaaaaaaaaaaa.png')
# sleep(2)
# 强制等待 slee（2）
# 智能等待
# until = ui.WebDriverWait(dr,10)
# until.until(lambda dr:dr.find_element_by_xpath('//*[@id="user-nomal"]/div[1]/a/img').is_displayed())


# until=dr.find_element_by_xpath('//*[@id="user-nomal"]/div[1]/a/img').is_enabled()
# is_displayed  判断元素是否显示    结果：True  Flase
# is_enabled   判断元数是否为灰化状态
# print(until)
# dr.quit()


# wait = ui.WebDriverWait()
# wait.until(lambda dr:dr.find_element_by_xpath('//*[@id="user-nomal"]/div[1]/a/img')).is_displayed