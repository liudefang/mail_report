# coding:utf-8
from selenium import webdriver
import unittest

class Test1(unittest.TestCase):
    u'''ERP登录测试'''

    @classmethod
    def setUpClass(cls):
        '''测试固件setUp的代码，主要用于测试的前期准备工作'''
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(8)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        u"""定位失败截图案例"""
        self.driver.get("https://qa1-erp.jfz.com")
        self.driver.find_element_by_xpath("//*[@name='username']").send_keys("defang1")
        self.driver.find_element_by_xpath("//*[@name='password']").send_keys("123456")
        self.driver.find_element_by_xpath("//*[@class='submit_wrap']").click()
        t = self.driver.title
        self.assertIn(u"失败用例", t)



if __name__ == "__main__":
    unittest.main()



