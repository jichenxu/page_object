# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/5 20:45
@Auth ： chenxu
@File ：test_weixin.py
"""
import pytest
import yaml

from page.main_page import MainPage


class TestWeiXin:
     def setup(self):
       self.mainPage = MainPage()

     @pytest.mark.parametrize(("username", "othername","id","phone","email","position"), yaml.safe_load(open("../resouce/data.yml",encoding='utf-8')))
     def test_weixin(self,username,othername,id,phone,email,position):

         assert self.mainPage.goto_add_members().add_members(username,othername,id,phone,email,position)

     def test_members(self):
         username = "郭襄"
         members = self.mainPage.goto_address_book().get_members()
         assert username in members

     def teardown(self):
         self.mainPage.quit()
