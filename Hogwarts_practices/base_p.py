# coding=UTF-8
# 作者:herui
# 时间:2020/12/19 16:02
# 功能:
from selenium import webdriver
import os

class Base:
    def setup(self):
        browser = os.getenv("browser")
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS()
        elif browser == 'ie':
            self.driver = webdriver.Ie()
        else:
            self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def tear_down(self):
        self.driver.quit()