# -*- encoding: utf-8 -*-
# @Time    : 2017/12/21 13:56
# @Author  : mike.liu
# @File    : test_demo5.py

import unittest
import time
from selenium import webdriver




class Test2(unittest.TestCase):

    def setUp(self):
        '''测试固件setUp的代码，主要用于测试的前期准备工作'''
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)
        self.driver.get("https://qa1-erp.jfz.com")

    def tearDown(self):
        '''测试结束之后的清理，一般是关闭浏览器'''

        self.driver.quit()

    def test_login(self):
        '''这里一定要以test开头'''

        self.driver.find_element_by_xpath("//*[@name='username']").send_keys("defang2")
        self.driver.find_element_by_xpath("//*[@name='password']").send_keys("123")
        self.driver.find_element_by_xpath("//*[@class='submit_wrap']").click()
        self.driver.find_element_by_xpath("//*[@id='10000012200328']/a").click()

        self.assertIn("客服系统",self.driver.page_source)
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[contains(.,'退出系统')]").click()



if __name__ == "__main__":
    unittest.main()

