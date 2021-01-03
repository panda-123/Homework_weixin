# coding=UTF-8
# 作者:herui
# 时间:2021/1/1 20:57
# 功能:
from selenium.webdriver.common.by import By

from Hogwarts_weixin.page.base import Base
from Hogwarts_weixin.page.contactpage import ContactPage


class AddDepartment(Base):
    def add_department(self, name, depname):
        # 添加部门成功
        self.input_name(name)
        self.select_department(depname)
        self.submit()
        return ContactPage(self.driver)

    def add_department_failed(self, name, depname):
        # 添加部门失败
        self.input_name(name)
        self.select_department(depname)
        self.cancel()
        return ContactPage(self.driver)

    def input_name(self, name=None):
        # 设置部门名称
        self.find(By.CSS_SELECTOR, "[name='name']").send_keys(name)
        return self

    def select_department(self, depname="霍格沃兹测试"):
        # 选择部门
        self.driver.find_element_by_css_selector(".js_parent_party_name+.ww_btn_Dropdown_arrow").click()
        # .jstree.jstree-2.jstree-default 该元素中 jstree-2数字会随着机构数量而变化
        # self.find(By.CSS_SELECTOR, ".jstree.jstree-2.jstree-default li li:nth-child("+ str(num) +")").click()
        # 选不到一级父机构
        # self.find(By.CSS_SELECTOR,
        #           ".member_tag_dialog_inputDlg ul li+[aria-level='2']:nth-child("+str(num)+")").click()
        self.driver.find_element_by_xpath(
            '//*[@class="member_tag_dialog_inputDlg"]//*[contains(text(),"'+depname+'")]').click()
        return self

    def submit(self):
        # 保存
        self.find(By.LINK_TEXT, "确定").click()
        return self

    def cancel(self):
        # 取消
        self.find(By.LINK_TEXT, "取消").click()
        return self