# coding=UTF-8
# 作者:herui
# 时间:2020/12/30 19:58
# 功能:
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Hogwarts_weixin.page.base import Base


class ContactPage(Base):
    def enter_add_member(self):
        from Hogwarts_weixin.page.addmemberpage import AddMemberPage
        """添加成员页面
        :return:
        """
        WebDriverWait(self.driver,10).until(
            expected_conditions.element_to_be_clickable((By.LINK_TEXT, "添加成员")))
        # self.driver.find_element_by_css_selector(".js_has_member>.ww_operationBar>.qui_btn.ww_btn.js_add_member").click()
        self.driver.find_element_by_link_text("添加成员").click()
        return AddMemberPage(self.driver)

    def get_member(self):
        # 获取成员列表
        members = self.driver.find_elements_by_css_selector(".member_colRight_memberTable_td:nth-child(5)")
        member_list = [i.text for i in members]
        return member_list
    def enter_add_department(self):
        # 进入添加部门页面
        from Hogwarts_weixin.page.adddepartment import AddDepartment
        self.find(By.CSS_SELECTOR, ".member_colLeft_top_addBtn").click()
        self.find(By.CSS_SELECTOR, ".js_create_party").click()
        return AddDepartment(self.driver)

    def get_department(self):
        # 获取部门列表
        ele1 = self.driver.find_elements_by_css_selector(".jstree.jstree-1.jstree-default li li li")
        ele2 = self.driver.find_elements_by_css_selector(".jstree-anchor")
        res = [i.text for i in ele2+ele1]
        print(res)
        return res
