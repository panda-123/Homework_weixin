# coding=UTF-8
# 作者:herui
# 时间:2020/12/29 21:56
# 功能:
from Hogwarts_weixin.page.base import Base
from Hogwarts_weixin.page.contactpage import ContactPage
from ..page.indexpage import IndexPage


class MainPage(Base):
    def enter_index_page(self):
        return IndexPage(self.driver)

    def enter_contacts_page(self):
        """进入通讯录页面
        :return:
        """
        self.driver.find_element_by_id("menu_contacts").click()
        return ContactPage(self.driver)

    def back_contacts_page(self):
        self.driver.find_element_by_id("menu_contacts").click()
        return ContactPage(self.driver)


    def enter_apps_page(self):
        pass

    def enter_customer_page(self):
        pass

    def enter_manageTools_page(self):
        pass

    def enter_profile_page(self):
        pass