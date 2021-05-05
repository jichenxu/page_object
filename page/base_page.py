# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/5 20:31
@Auth ： chenxu
@File ：base_page.py
"""
import shelve

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    base_url = ""
    def __init__(self,driver:WebDriver=None):
        if driver == None:
            #复用浏览器，需要设置 option.debugger_address
            # option = Options()
            # option.debugger_address = "127.0.0.1:9222"
            # self.driver = webdriver.Chrome(options=option)
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(10)
        else:
            self.driver = driver
        if self.base_url != "":
            self.driver.get(self.base_url)
            db = shelve.open("../mydbs/cookies")
            cookies = db["cookies"]
            for cookie in cookies:
                if 'expiry' in cookie.keys():
                    cookie.pop('expiry')
                self.driver.add_cookie(cookie)
            self.driver.get(self.base_url)

    def find(self,locator,value):
        return self.driver.find_element(locator,value)

    def finds(self, locator, value):
        return self.driver.find_elements(locator, value)

    def quit(self):
        self.driver.quit()

