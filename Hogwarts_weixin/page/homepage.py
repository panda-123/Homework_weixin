# coding=UTF-8
# 作者:herui
# 时间:2020/12/29 21:56
# 功能:
from Hogwarts_weixin.page.loginpage import LoginPage
from Hogwarts_weixin.page.registerpage import RegisterPage


class HomePage:
    def enter_login_page(self):
        return LoginPage()

    def enter_register_page(self):
        return RegisterPage()