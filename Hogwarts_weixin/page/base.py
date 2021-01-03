# coding=UTF-8
# 作者:herui
# 时间:2020/12/29 22:28
# 功能:
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class Base:
    def __init__(self, base_driver=None):
        """
        进行driver初始化,并且避免重复实例化
        :param base_driver:
        """
        # 类型声明,不是赋值
        base_driver: WebDriver
        if base_driver is None:
            # 变量加self后,类中的其他方法也可以调用该变量
            self.driver = webdriver.Chrome()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
            self.driver.maximize_window()
            self.__cookie_login()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(3)

    def __cookie_login(self):
        with open("./datas/cookie.yml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def find(self, by, value=None):
        if value is None:
            # 如果传入的是一个元组,则将元组进行解包,传参
            return self.driver.find_element(*by)
        else:
            # 如果传的为正常的参数信息,就正常传参
            return self.driver.find_element(by=by, value=value)

    def quit(self):
        self.driver.quit()

