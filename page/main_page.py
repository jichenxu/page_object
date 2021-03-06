# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/5 20:43
@Auth ： chenxu
@File ：main_page.py
"""
from time import sleep

from selenium.webdriver.common.by import By

from page.add_page import AddPage
from page.base_page import BasePage


class MainPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame"
    #添加成员
    def goto_add_members(self):
        sleep(3)
        #点击【添加成员】按钮
        self.driver.find_element(By.XPATH,'//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]').click()
        return AddPage(self.driver)

    #通讯录
    def goto_address_book(self):
        #点击【通讯录】
        self.driver.find_element(By.ID,'menu_contacts').click()
        return AddPage(self.driver)
