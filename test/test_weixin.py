# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/5 20:45
@Auth ： chenxu
@File ：test_weixin.py
"""
import shelve
from time import sleep

import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
     @pytest.mark.skip
     def test_cookies(self):
         # option = Options()
         # option.debugger_address = "127.0.0.1:9222"
         # self.driver = webdriver.Chrome(options=option)
         self.driver = webdriver.Chrome()
         self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
         #cookies = self.driver.get_cookies()
         cookies = [{'domain': '.qq.com', 'expiry': 1620221528, 'httpOnly': False, 'name': '_gat', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': True, 'value': '29807030181260470'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': True, 'value': '8v5bqsk'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850954847467'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': True, 'value': 'GAcW9_16kP3sP9Y3_5UV7GfqYA4StuZhJNI0n9oBt6DF3nLAZAYKQnUyp5aPisWW'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970325011434433'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': True, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': True, 'value': 'a7617125'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': True, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1620307869, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.871635060.1620200420'}, {'domain': 'work.weixin.qq.com', 'expiry': 1620231955, 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': False, 'value': '6i7qdku'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': True, 'value': 'direct'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': True, 'value': 'dc7mLDvc20hhczwLjKegaTE4YsdFK2oiYT33zpLsP7jBdcnq_Yf_DJ9A27NZKov7CGLqRtwNpk45pp3C9iQi-X9urzvD8r-g72RVcQPEZa-OEcQkiTrZ0obHP0GFfzV_xuB_o8fRgMTk6vLyHCrzpsXx01hzUrsftLGfGtcsPmqZaK_fj4Y9Ny_7SFdn8n7l0rxcjl8QXRbBgdIo7rI8M6FcXerS0kKNT9KbpxoUzL9cp8UNbnzXEFJ9JVcBHn4eOhYEVni0FBctEo84qi0Rag'}, {'domain': '.qq.com', 'expiry': 1683293469, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.2061398850.1620011906'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850954847467'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': True, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1622813470, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
         print(cookies)
         for cookie in cookies:
              if 'expiry' in cookie.keys():
                  cookie.pop('expiry')
              self.driver.add_cookie(cookie)
         self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
         sleep(10)
     @pytest.mark.skip
     def test_dbs(self):
         cookies = [{'domain': '.qq.com', 'expiry': 1620221528, 'httpOnly': False, 'name': '_gat', 'path': '/',
                     'secure': False, 'value': '1'},
                    {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/',
                     'secure': True, 'value': '29807030181260470'},
                    {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'ww_rtkey', 'path': '/', 'secure': True,
                     'value': '8v5bqsk'},
                    {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/',
                     'secure': False, 'value': '1688850954847467'},
                    {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/',
                     'secure': True, 'value': 'GAcW9_16kP3sP9Y3_5UV7GfqYA4StuZhJNI0n9oBt6DF3nLAZAYKQnUyp5aPisWW'},
                    {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/',
                     'secure': False, 'value': '1970325011434433'},
                    {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/',
                     'secure': True, 'value': ''},
                    {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/',
                     'secure': True, 'value': 'a7617125'},
                    {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/',
                     'secure': True, 'value': '0'},
                    {'domain': '.qq.com', 'expiry': 1620307869, 'httpOnly': False, 'name': '_gid', 'path': '/',
                     'secure': False, 'value': 'GA1.2.871635060.1620200420'},
                    {'domain': 'work.weixin.qq.com', 'expiry': 1620231955, 'httpOnly': True, 'name': 'ww_rtkey',
                     'path': '/', 'secure': False, 'value': '6i7qdku'},
                    {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/',
                     'secure': True, 'value': 'direct'},
                    {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/',
                     'secure': True,
                     'value': 'dc7mLDvc20hhczwLjKegaTE4YsdFK2oiYT33zpLsP7jBdcnq_Yf_DJ9A27NZKov7CGLqRtwNpk45pp3C9iQi-X9urzvD8r-g72RVcQPEZa-OEcQkiTrZ0obHP0GFfzV_xuB_o8fRgMTk6vLyHCrzpsXx01hzUrsftLGfGtcsPmqZaK_fj4Y9Ny_7SFdn8n7l0rxcjl8QXRbBgdIo7rI8M6FcXerS0kKNT9KbpxoUzL9cp8UNbnzXEFJ9JVcBHn4eOhYEVni0FBctEo84qi0Rag'},
                    {'domain': '.qq.com', 'expiry': 1683293469, 'httpOnly': False, 'name': '_ga', 'path': '/',
                     'secure': False, 'value': 'GA1.2.2061398850.1620011906'},
                    {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/',
                     'secure': False, 'value': '1688850954847467'},
                    {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/',
                     'secure': True, 'value': '1'},
                    {'domain': '.work.weixin.qq.com', 'expiry': 1622813470, 'httpOnly': False, 'name': 'wwrtx.i18n_lan',
                     'path': '/', 'secure': False, 'value': 'zh'}]
         db = shelve.open("../mydbs/cookies")
         db["cookies"] = cookies
