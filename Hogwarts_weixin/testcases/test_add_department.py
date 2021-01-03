# coding=UTF-8
# 作者:herui
# 时间:2021/1/1 21:02
# 功能:
import pytest

from Hogwarts_weixin.page.mainpage import MainPage


class TestAddDepartment:
    def setup_class(self):
        self.main = MainPage()
        self.contact = self.main.enter_contacts_page()

    @pytest.mark.parametrize("name,depname",[("推云4","霍格沃兹测试")])
    def test_add_department(self, name, depname):
        res = self.contact.enter_add_department().add_department(name, depname).get_department()
        assert " ",name in res

    @pytest.mark.parametrize("name,depname", [("推云5", "测试5")])
    def test_add_department_failed(self, name, depname):
        res = self.contact.enter_add_department().add_department_failed(name, depname).get_department()
        assert " ",name not in res


    def teardown_function(self):
        self.main.enter_contacts_page()

    def teardown_class(self):
        self.main.quit()

