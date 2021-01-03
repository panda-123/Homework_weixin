# coding=UTF-8
# 作者:herui
# 时间:2020/12/29 22:12
# 功能:
from Hogwarts_weixin.page.addmemberpage import AddMemberPage
from Hogwarts_weixin.page.base import Base


class IndexPage(Base):
    def enter_add_member_by_index(self):
        self.driver.find_element_by_link_text("添加成员")
        return AddMemberPage(self.driver)
