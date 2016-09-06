# -*- coding: UTF-8 -*-
import pickle
from time import sleep
import selenium.webdriver
class fu():
     driver=selenium.webdriver.Firefox()
     driver.get("https://passport.bilibili.com/login")
#      driver.find_element_by_id("userIdTxt").send_keys("1286685678@qq.com")
#      driver.find_element_by_id("passwdTxt").send_keys("123321")
     driver.get("http://message.bilibili.com/#whisper/mid6459954")
#      sleep(60)
#      pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))
     driver.close()