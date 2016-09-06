# -*- coding: UTF-8 -*-
import os
from time import sleep
import selenium.webdriver
class excel():
    driver=selenium.webdriver.Firefox()
    driver.get("http://223.86.31.102:81/")
    driver.find_element_by_id("username").click()
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("test")
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys("111111")
    driver.find_element_by_xpath("//button[@type='button']").click()
    driver.find_element_by_link_text(u"基础信息").click()
    driver.find_element_by_css_selector("li.dropdown.open > ul.dropdown-menu.topdropdownmenu > li > a").click()
    driver.find_element_by_link_text(u"数据").click()
    driver.find_element_by_id("link_import").click()
    driver.find_element_by_link_text(u"管理员").click()
    driver.find_element_by_xpath("//div[2]/div/div").click()
    os.system(u"D:\\sub33.exe")
#      sleep(60)
#      pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
