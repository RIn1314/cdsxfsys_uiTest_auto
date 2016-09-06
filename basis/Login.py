# -*- coding: UTF-8 -*-
from time import sleep
import selenium.webdriver

class Login:
    
    def login(self,nameLocation,passwordLocation): #传进去两个参数：用户名位置，密码位置
        driver=selenium.webdriver.Firefox()
        userName = []
        with open("./accountInfomation/userName.txt","rb") as f: 
            for line in f:
                line =line.replace("\r\n","")
                userName.append(line)   #循环读入用户名，然后封装到数组userName里面
        userPassword = []
        with open("./accountInfomation/userPassword.txt","rb") as f: 
            for line in f:
                line =line.replace("\r\n","")
                userPassword.append(line)  #循环读入用户名，然后封装到数组userPassword里面
        base_url = []  
        with open("./accountInfomation/base_url.txt","rb+") as f: 
            for line in f:
                line =line.replace("\r\n","")
                base_url.append(line)      #循环读入网址，然后封装到数组base_url里面       
        dict = {'driver': driver, 'userName': userName[nameLocation]}
        base_url = base_url[0]
        main_frame=base_url +'/frame/main'            
        driver.get( base_url + '/login/show')
        print str(dict["userName"])+'正在尝试登录...'
        driver.find_element_by_id('userName').send_keys(userName[nameLocation])
        driver.find_element_by_id('userPwd').send_keys(userPassword[passwordLocation])
        try:
            driver.find_element_by_name('validateCode').send_keys('****')
            print '验证码正确'
        except:
            print '验证码输入错误'
        print '****正在登录****'+'\n浏览器和session信息：'+str(dict["driver"])      
        try:
            driver.find_element_by_name('submitBtn').click()
            print str(dict["userName"])+'登录成功！'
        except:
            print '登录按钮 点击失败，登录失败！'    
        try:
            driver.switch_to_alert().accept()
            print driver.switch_to_alert().text
            sleep(1)
            print driver.switch_to_alert.text     
        except:
            pass
        driver.get(main_frame)
        return dict                



