# -*- coding: UTF-8 -*- 
from basis.caseOperation import caseOperation
from basis.Login import Login
import time 

class operation():
    # ***********来信登记**************
    for i in range(1):
            o = caseOperation()
            o.letterRigister()
#以下是展示函数            
    L=Login()        #展示账号的最新的三个信访件
    DictSet =L.login(0,0)         #在此处登录账号
    driver = DictSet["driver"]
    userName = DictSet["userName"]
    main_handle = driver.current_window_handle
    driver.switch_to_frame('leftFrame') 
    driver.find_element_by_link_text(u"待办理").click()
    driver.find_element_by_link_text(u"待办理").click()
    driver.switch_to_default_content()
    driver.switch_to_frame("rightFrame")
    driver.find_element_by_link_text("案件编号").click()
    newLetter =[]
    driver.get_screenshot_as_file("D://screenshot//rigister.png") #截图
    for j in range(1,4): 
            line =  driver.find_element_by_xpath("//form[@id='searchForm']/div/table/tbody/tr["+str(j)+"]/td[2]/a/font").text
            line = str(line)
            newLetter.append(line)
    print "登记的前三个最新的案件编号为:"+str(newLetter)        
 
            
     
            
