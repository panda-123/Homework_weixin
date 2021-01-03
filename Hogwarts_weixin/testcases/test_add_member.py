# coding=UTF-8
# 作者:herui
# 时间:2020/12/30 20:11
# 功能:
import pytest

from Hogwarts_weixin.page.base import Base
from ..page.mainpage import MainPage


class TestAddMember:

    def setup_class(self):
        self.main = MainPage()

    def test_add_member(self):
        res = self.main.enter_contacts_page().enter_add_member().add_member().get_member()
        assert "13811112224" in res

    def test_add_member_failed(self):
        res = self.main.enter_contacts_page().enter_add_member().add_member_failed()
        assert "该帐号已被“大宝4”占有" in res

    def teardown_function(self):
        self.main.back_contacts_page()

    def teardown_class(self):
        self.main.quit()