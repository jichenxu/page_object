# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/5 20:44
@Auth ： chenxu
@File ：add_page.py
"""
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from page.base_page import BasePage


class AddPage(BasePage):
    def __init__(self,driver:WebDriver):
        self.driver = driver

    #添加成员
    def add_members(self,username,othername,id,phone,email,position):
        #添加姓名
        self.find(By.ID,'username').send_keys(username)
        #别名
        self.find(By.ID,'memberAdd_english_name').send_keys(othername)
        #Id
        self.find(By.ID,'memberAdd_acctid').send_keys(id)
        #性别
        self.find(By.CSS_SELECTOR,'.ww_radio').click()
        #手机号
        self.find(By.ID,'memberAdd_phone').send_keys(phone)
        #邮箱
        self.find(By.ID,'memberAdd_mail').send_keys(email)
        #职务
        self.find(By.ID,'memberAdd_title').send_keys(position)
        #保存
        self.find(By.LINK_TEXT,'保存并继续添加').click()
        sleep(3)
        return  True
    #获取成员
    def get_members(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,'.member_colRight_memberTable_td_Checkbox')))
        elements = self.finds(By.CSS_SELECTOR,'.member_colRight_memberTable_td:nth-child(2)')
        names = []
        for ele in elements:
            names.append(ele.get_attribute("title"))
        print(names)
        return names

