# coding=UTF-8
# 作者:herui
# 时间:2020/12/30 19:57
# 功能:
from Hogwarts_weixin.page.addmembercheck import AddMemberCheck
from Hogwarts_weixin.page.base import Base
from Hogwarts_weixin.page.contactpage import ContactPage


class AddMemberPage(Base):
    def add_member(self):
        """
        实现添加成员
        :return: 返回断言方法
        """
        self.driver.find_element_by_id("username").send_keys("大宝4")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("dabao4")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("13811112224")
        self.driver.find_element_by_link_text("保存").click()
        return ContactPage(self.driver)

    def add_member_failed(self):
        """
        添加成员失败
        :return:
        """
        self.driver.find_element_by_id("username").send_keys("大宝4")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("dabao4")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("13811112224")
        # res = self.driver.find_element_by_css_selector("#memberAdd_acctid+.ww_inputWithTips_tips").text
        ele = self.driver.find_elements_by_css_selector(".ww_inputWithTips_tips")
        res = [i.text for i in ele]
        self.driver.find_element_by_link_text("首页").click()
        self.driver.find_element_by_css_selector('[node-type="cancel"]').click()
        return res