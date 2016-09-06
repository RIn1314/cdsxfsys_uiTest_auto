# -*- coding: UTF-8 -*-
from selenium.webdriver.support.ui import Select
from basis.Login import Login
import os
import selenium.webdriver
import time
from time import sleep
from selenium.webdriver.common.keys import Keys 
class caseOperation():
    def caseSelect(self,caseId):       #案件登记
        L=Login()
        DictSet = L.login(0,0)
        driver = DictSet["driver"]
        driver.switch_to_frame('leftFrame')
        driver.find_element_by_xpath("//dd[4]/div").click()
        sleep(3)
        driver.find_element_by_link_text(u"信访件查询").click()
        driver.switch_to_default_content()
        driver.switch_to_frame('rightFrame')
        Select(driver.find_element_by_id("searchTypeSelectOne0")).select_by_visible_text(u"信访事项")
        Select(driver.find_element_by_id("searchTypeSelectTwoTwo0")).select_by_visible_text(u"信访件编号")
        Select(driver.find_element_by_id("relationInputSelect0")).select_by_visible_text(u"包含有")
        driver.find_element_by_id("searchKey0").clear()
        driver.find_element_by_id("searchKey0").send_keys(caseId)
        driver.find_element_by_xpath("//input[@value='查询']").click()
        
    def letterRigister(self):               #来信登记，默认是admin登记
        print '来信登记开始'
        L=Login()
        DictSet = L.login(0,0)
        userName = DictSet["userName"]
        print "来信登记用户名为"+ userName
        driver = DictSet["driver"]
        main_handle=driver.current_window_handle
        driver.switch_to_frame('leftFrame')
        driver.find_element_by_link_text(u'待办理').click()
        driver.find_element_by_link_text(u'待办理').click()
        driver.switch_to_default_content()
        driver.switch_to_frame('rightFrame')
        try:
            driver.find_element_by_xpath("//input[@value='来信登记']").click()
        except:
            print "waring:无法找到来信登记按钮，需要进行“清除默认”和“案件登记“类型设置"
              
        allhandle=driver.window_handles
        for handle in allhandle:
            if handle != main_handle:
                driver.switch_to_window(handle)
                letter_handle=driver.current_window_handle
                assert u'来信'  in driver.title     
                driver.find_element_by_id('sbjName').clear()
                driver.find_element_by_id('sbjName').send_keys(u'测试123')
                print '找到元素‘住址’，开始填写'
                driver.find_element_by_id("multiSelect").click()
                driver.find_element_by_link_text(u"四川省").click()
                driver.find_element_by_link_text(u"成都市").click()
                driver.find_element_by_link_text(u"锦江区").click()
                driver.find_element_by_css_selector("div.close").click()
                print '找到元素‘判重’，开始判重'
                driver.find_element_by_id("judgement").click()  
                allhandles=driver.window_handles
                for handle in allhandles:
                    if handle != main_handle:
                        if handle != letter_handle:
                            driver.switch_to_window(handle)
                            try:
                                assert u'判重' in driver.title
                            except:
                                print '无法定位到判重页面'   
                            driver.close()
                            print '判重页面已正常关闭' 
                            driver.switch_to_window(letter_handle)       
                            Select(driver.find_element_by_id('sbjSex')).select_by_visible_text(u'女')
                            Select(driver.find_element_by_id("sbjCredentialsType")).select_by_visible_text(u"居民身份证")
                            driver.find_element_by_id('petitionDefendantName').clear()
                            driver.find_element_by_id('petitionDefendantName').send_keys(u'测试受信人456')
                            Select(driver.find_element_by_id('matterBelongSystemCode')).select_by_visible_text(u"军队武警")
                            driver.find_element_by_id('belongAreaInput').click()
                            driver.find_element_by_css_selector('#stock_province_item3 > ul.area-list > li > a').click()
                            driver.find_element_by_css_selector('#stock_city_item3  > ul.area-list > li > a').click()
                            driver.find_element_by_css_selector("#belongArea-store-selector > div.close").click()
                            driver.find_element_by_id('cateMultiSelect').click()
                            driver.find_element_by_link_text(u"农村农业").click()
                            driver.find_element_by_link_text(u"村务管理").click()
                            driver.find_element_by_link_text(u"集体资产管理").click()
                            driver.find_element_by_css_selector("option[value=\"01\"]").click()
                            Select(driver.find_element_by_id("petitionPurposeCode")).select_by_visible_text(u"申诉")
                            driver.find_element_by_css_selector("option[value=\"02\"]").click()
                            Select(driver.find_element_by_id("petitionTypeCode")).select_by_visible_text(u"传真")
                            driver.find_element_by_id("FollowPersons").clear()
                            driver.find_element_by_id("FollowPersons").send_keys(u"测试随访人789")
                            driver.find_element_by_xpath("(//input[@name='longpendingCaseFlag'])[1]").click()  
                            driver.find_element_by_xpath("(//input[@name='threeCrossoverThreeDivionFlag'])[1]").click()
                            driver.find_element_by_xpath("(//input[@name='dcdbFlag'])[2]").click()#flag为1，就有督察督办标志。
                            Select(driver.find_element_by_id("hotIssuesCode")).select_by_visible_text(u"农民工工资")
                            Select(driver.find_element_by_id("petitionReasonCode")).select_by_visible_text(u"干部作风")
                            driver.find_element_by_id("petitionContent").clear()
                            driver.find_element_by_id("petitionContent").send_keys(u"petitionContent!!这是内容摘要!!")
                            driver.find_element_by_id("petitionRemark").clear()
                            driver.find_element_by_id("petitionRemark").send_keys(u"petitionRemark，这是内容备注!!")
                            driver.find_element_by_id("registerForm").click()
                            driver.find_element_by_id("tipOk").click()
                            print '来信登记成功' 
                            try:
                                driver.switch_to_window(main_handle)
                                assert u'信息管理' in driver.title
                                driver.quit()
                            except:
                                print('没有正常关闭来信登记窗口')           
                                               
    def contradictionCaseRigister(self):      #矛盾排查登记
        
        L=Login()
        DictSet = L.login(0,0)
        driver = DictSet["driver"]
        main_handle = driver.current_window_handle
        driver.switch_to_frame("leftFrame")
        driver.find_element_by_xpath("//dd[10]/div").click()   
        driver.find_element_by_link_text(u"待处理").click()
        driver.switch_to_default_content()
        driver.switch_to_frame('rightFrame')
        driver.find_element_by_xpath("//input[@value='矛盾排查登记']").click()
        allhandle = driver.window_handles
        for handle in allhandle:
            if handle != main_handle:
                driver.switch_to_window(handle)
#                 contradictionCaseRigister_handle=driver.current_window_handle  如果要关闭矛盾排查案件页面，就使用吧
                assert u'矛盾' in driver.title
                driver.find_element_by_id("cSbjName").clear()
                driver.find_element_by_id("cSbjName").send_keys("ceshi1")
                driver.find_element_by_id("cSbjTelephone").clear()
                driver.find_element_by_id("cSbjTelephone").send_keys("321312")
                driver.find_element_by_id("multiSelect").click()
                driver.find_element_by_link_text(u"四川省").click()
                driver.find_element_by_link_text(u"成都市").click()
                driver.find_element_by_link_text(u"锦江区").click()
                driver.find_element_by_css_selector("div.close").click()
                driver.find_element_by_id("cTitle").clear()
                driver.find_element_by_id("cTitle").send_keys(u"这是矛盾排查的标题")
                driver.find_element_by_id("cLeaderBelong").clear()
                driver.find_element_by_id("cLeaderBelong").send_keys("321312")
                driver.find_element_by_id("cContent").clear()
                driver.find_element_by_id("cContent").send_keys(u"这是矛盾排查的内容")
                Select(driver.find_element_by_id("categoryId")).select_by_visible_text(u"涉法涉诉问题")
                Select(driver.find_element_by_id("cLeaderId0")).select_by_visible_text(u"彭泽君")
                driver.find_element_by_id("smsContent0").clear()
                driver.find_element_by_id("smsContent0").send_keys(u"这是包案领导的短信提醒信息")
                driver.find_element_by_id("registerForm").click()
                driver.find_element_by_id("tipOk").click()
                
    def assgin(self,caseId,department,nameLocation,passwordLocation):  #交办
        caseId = caseId
        department = department
        L=Login()        
        DictSet =L.login(nameLocation,passwordLocation)
        driver = DictSet["driver"]
        userName = DictSet["userName"]
        main_handle = driver.current_window_handle
#        print "开始对案件：" +caseId+ "进行交办。" + "交办人为：" + userName +"。"
        
        driver.switch_to_frame('leftFrame') 
        driver.find_element_by_link_text(u"待办理").click()
        driver.find_element_by_link_text(u"待办理").click()
        driver.find_element_by_link_text(u"待办理").click()
        driver.find_element_by_link_text(u"待办理").click()     
        driver.switch_to_default_content()
        driver.switch_to_frame("rightFrame")
        driver.find_element_by_link_text("案件编号").click()
        driver.find_element_by_link_text(caseId).click()
        try:
            driver.find_element_by_id("getAssign").click()
            print "案件为" + caseId+ "的交办已经被"+ "用户" +userName+ "接受"
        except:
            pass
        Select(driver.find_element_by_id("handleMethod")).select_by_visible_text(u"交办")
        driver.find_element_by_id("assignDesDep").clear()
        driver.find_element_by_id("assignDesDep").send_keys(department)
        sleep(2)
        driver.find_element_by_xpath("//li[1]/div").click()                                       #新修改的下拉框

        driver.find_element_by_xpath(u"//input[@value='办理']").click()
        allhandles = driver.window_handles
        for handle in allhandles:
            if handle != main_handle:
                driver.switch_to_window(handle)
                try:        
                    driver.find_element_by_id("assignOpinion").send_keys(u"这是交办" + str(time.localtime()))
                    driver.find_element_by_id("assignSubmit").click()
                    driver.find_element_by_id("tipOk").click()
                except:
                    print "ERROR:没有交办成功"   

    def forward(self,caseId,department,nameLocation,passwordLocation):      #转办
        caseId = caseId
        department = department
        L=Login()        
        DictSet =L.login(nameLocation,passwordLocation)
        driver = DictSet["driver"]
        userName = DictSet["userName"]
        main_handle = driver.current_window_handle
        
        driver.switch_to_frame('leftFrame') 
        driver.find_element_by_link_text(u"待办理").click()
        driver.find_element_by_link_text(u"待办理").click()     
        driver.switch_to_default_content()
        driver.switch_to_frame("rightFrame")
        driver.find_element_by_link_text("案件编号").click()
        driver.find_element_by_link_text(caseId).click()
        try:
            driver.find_element_by_id("agreeForward").click()
            print "案件为" + caseId+"的交办已经被"+"用户"+userName+"接受"
        except:
            pass
        Select(driver.find_element_by_id("handleMethod")).select_by_visible_text(u"转办")
        driver.find_element_by_id("depNameText").clear()
        driver.find_element_by_id("depNameText").send_keys(department)
        driver.find_element_by_css_selector("em").click()
        driver.find_element_by_xpath(u"//input[@value='办理']").click()
        allhandles = driver.window_handles
        for handle in allhandles:
            if handle != main_handle:
                driver.switch_to_window(handle)
                try:        
                    driver.find_element_by_id("opinion").send_keys(u"这是转办" + str(time.localtime()))
                    driver.find_element_by_xpath(u"//input[@value='提交']").click()
                    driver.find_element_by_id("tipOk").click()
                except:
                    pass   
                
    def acceptCase(self,caseId,nameLocation,passwordLocation):       #接受案件
        caseId = caseId
        L=Login()
        DictSet =L.login(nameLocation,passwordLocation)
        driver = DictSet["driver"]
        userName = DictSet["userName"]
        driver.switch_to_frame('leftFrame')
        driver.find_element_by_link_text(u"待办理").click()
        driver.find_element_by_link_text(u"待办理").click()
        driver.switch_to_default_content()
        driver.switch_to_frame("rightFrame")
#         driver.find_element_by_link_text("案件编号").click()
        driver.find_element_by_link_text(caseId).click()
        try:
            driver.find_element_by_id("getAssign").click()
            print "案件为" + caseId+"的交办已经被"+"用户"+userName+"接受"   
        except:
            pass
        try:
            driver.find_element_by_id("agreeForward").click()
            print "案件为" + caseId+"的交办已经被"+"用户"+userName+"接受"
        except:
            pass         
        
        return driver
    
    def substantiveHandle(self,caseId,nameLocation,passwordLocation):      #实体性受理出具，包含上传附件
        L = Login()
        DictSet = L.login(nameLocation, passwordLocation)
        driver = DictSet["driver"]
        userName = DictSet["userName"]
        caseId =caseId
        main_handle = driver.current_window_handle
        try:
            driver.switch_to_frame('leftFrame') 
            driver.find_element_by_link_text(u"待办理").click()
            driver.find_element_by_link_text(u"待办理").click()
            driver.find_element_by_link_text(u"待办理").click()
            driver.find_element_by_link_text(u"待办理").click()     
            driver.switch_to_default_content()
            driver.switch_to_frame("rightFrame")
            driver.find_element_by_link_text("案件编号").click()
            driver.find_element_by_link_text(caseId).click()
            print "开始对：" + caseId+"案件出具实体性处理意见书"+"出具用户 ："+userName+"。"
            Select(driver.find_element_by_id("handleMethod")).select_by_visible_text(u"实体性受理")
            driver.find_element_by_xpath(u"//input[@value='办理']").click()
            allhandles = driver.window_handles
            for handle  in allhandles:
                if handle != main_handle:
                    driver.switch_to_window(handle)
                    caseDetail_handle = driver.current_window_handle
                    driver.find_element_by_id("petitionContent").clear()
                    driver.find_element_by_id("petitionContent").send_keys(u"这是实体性受理内容。")
                    driver.find_element_by_id("time1").click()
                    driver.find_element_by_link_text("29").click()
                    driver.find_element_by_id("uploadfile4").click()
                    driver.switch_to_alert().accept()#请上传图片附件alert
                    driver.switch_to_alert().accept()#附件还能上传几个alert
                    allhandles = driver.window_handles
                    for handle in allhandles:
                        if handle != caseDetail_handle:
                            if handle != main_handle:
                                driver.switch_to_window(handle)
                                print driver.title
                                driver.find_element_by_link_text(u'增加文件').click()
                                os.system(u"D:\\sub.exe")
                                driver.find_element_by_link_text(u'开始上传').click()    
                                driver.switch_to_alert().accept()
                                driver.switch_to_window(caseDetail_handle)
                                driver.find_element_by_xpath(u"//input[@value='否']").click()
                                print "案件：" + caseId+"出具实体性处理意见书成功"+"出具用户 ："+userName+"。"
                                driver.switch_to_window(main_handle)
                                return driver
        except:
            pass                   
                            
    #自办操作（包含上传附件），不打开driver，接受一个driver，这个driver必须可以自办。                                                      
    def selfHandle(self,caseId,nameLocation,passwordLocation):
        L = Login()
        DictSet = L.login(nameLocation, passwordLocation)
        driver = DictSet["driver"]
        userName = DictSet["userName"]
        caseId =caseId
        main_handle = driver.current_window_handle
        driver.switch_to_frame('leftFrame') 
        driver.find_element_by_link_text(u"待办理").click()
        driver.find_element_by_link_text(u"待办理").click()
        driver.find_element_by_link_text(u"待办理").click()
        driver.find_element_by_link_text(u"待办理").click()     
        driver.switch_to_default_content()
        driver.switch_to_frame("rightFrame")
        driver.find_element_by_link_text("案件编号").click()
        driver.find_element_by_link_text(caseId).click()      
        try:
            Select(driver.find_element_by_id("handleMethod")).select_by_visible_text(u"自办")
            print "开始对：" + caseId+"案件出具自办处理意见书。"+"出具用户 ："+userName+"。"
        except:
            print "没有选择到自办，请确认是否出具了实体性受理"      
        driver.find_element_by_xpath(u"//input[@value='办理']").click()
        allhandles = driver.window_handles
        for handle  in allhandles:
            if handle != main_handle:
                driver.switch_to_window(handle)
                caseDetail_handle = driver.current_window_handle
                driver.find_element_by_id("reflectOpinion").clear()
                driver.find_element_by_id("reflectOpinion").send_keys(u"此为反映问题问题。") 
                driver.find_element_by_id("handleOpinion").clear()
                driver.find_element_by_id("handleOpinion").send_keys(u"此为自办处理情况问题。")
                driver.find_element_by_id("objDepartment").clear()
                driver.find_element_by_id("objDepartment").send_keys(u"申请复查单位")
                driver.find_element_by_id("sendTime").click()
                driver.find_element_by_link_text("30").click()  
                driver.find_element_by_id("sendUserName").clear()
                driver.find_element_by_id("sendUserName").send_keys(u"申请人姓名")
                driver.find_element_by_id("sendUserPhone").clear()
                driver.find_element_by_id("sendUserPhone").send_keys(u"申请人电话")
                driver.find_element_by_id("replyUnit").click()    
                driver.switch_to_alert().accept()#请上传图片附件的alert
                driver.switch_to_alert().accept()#附件还能上传几个的alert
                allhandles = driver.window_handles
                for handle in allhandles:
                    if handle != caseDetail_handle:
                        if handle != main_handle:
                            driver.switch_to_window(handle)  
                            print driver.title
                            driver.find_element_by_link_text(u'增加文件').click()
                            os.system(u"D:\\sub.exe")
                            driver.find_element_by_link_text(u'开始上传').click()    
                            driver.switch_to_alert().accept()
                            driver.switch_to_window(caseDetail_handle)
                            driver.switch_to_alert().accept()
                            sleep(0.5)
                            driver.find_element_by_xpath(u"//input[@value='否']").click()
                            driver.switch_to_window(main_handle)
                            print "案件：" + caseId+"出具自办处理意见书成功"+"出具用户 ："+userName+"。"
                            return driver                           
#     def letterRigister2(self):
#          无法处理模态窗口，暂时不用此方法
#         
#         L=Login()
#         DictSet = L.login(0,0)
#         driver = DictSet["driver"]
#         main_handle=driver.current_window_handle
#         driver.switch_to_frame('leftFrame')
#         driver.find_element_by_link_text(u'待办理').click()
#         driver.find_element_by_link_text(u'待办理').click()
#         driver.switch_to_default_content()
#         driver.switch_to_frame('rightFrame')
#         try:
#             driver.find_element_by_xpath("//input[@value='来信登记']").click()
#         except:
#             driver.switch_to_default_content()
#             driver.switch_to_frame('topFrame')
#             driver.find_element_by_link_text(u"清除偏好").click()
#             driver.switch_to_alert().accept()
#             driver.switch_to_default_content()
#             driver.switch_to_frame('rightFrame')
#             driver.switchTo().active_element()
#           
#             print driver.switchTo.active_element().GetText()
#             link = driver.find_element_by_xpath("//input[@value='案件登记']")
#             driver.find_element_by_xpath("//input[@value='案件登记']").click()
#             driver.execute_script('$(registerType[2]).click()', link)
#             driver.switch_to_alert().accept()
#             sleep(5)
#             driver.find_element_by_xpath("(//input[@value='     来     信     登     记        '").click()
# #             driver.find_element_by_xpath("(//input[@value=’来访登记‘").click()
# #             driver.find_element_by_xpath("(//input[@value=’网上投诉‘").click()
#             driver.find_element_by_id("Submit").click()
#             driver.switch_to_alert().accept()
    def report(self,caseId,nameLocation,passwordLocation):  #出具情况报告
        #情况报告，自己开启driver
        caseId = caseId
        L=Login()
        DictSet =L.login(nameLocation,passwordLocation)
        driver = DictSet["driver"]
#         userName = DictSet["userName"]
        driver.switch_to_frame('leftFrame')
        main_handle = driver.current_window_handle
        driver.find_element_by_link_text(u"待办理").click()
        driver.find_element_by_link_text(u"已办结").click()
        driver.switch_to_default_content()
        driver.switch_to_frame("rightFrame")
#         driver.find_element_by_link_text("案件编号").click()
        driver.find_element_by_link_text(caseId).click()
        try:
            Select(driver.find_element_by_id("handleMethod")).select_by_visible_text(u"情况报告")
            Select(driver.find_element_by_id("reportToDepartments")).select_by_visible_text(u"四川省成都市青羊区人民法院")
#             driver.find_element_by_id("reportToDepartments").send_keys(u"青羊")
#             driver.find_element_by_id("reportToDepartments").click()
#             driver.find_element_by_css_selector("em").click()
            driver.find_element_by_xpath(u"//input[@value='办理']").click()   
        except:
            pass
        allhandles = driver.window_handles
        for handle in allhandles:
            if handle != main_handle:
                driver.switch_to_window(handle)
                try:        
                    driver.find_element_by_id("reportTitle").send_keys(u"这是情况报告" + str(time.localtime()))
                    driver.find_element_by_id("reportHandleOpinion").send_keys(u"情况报告的内容" )
                    driver.find_element_by_id("report").click()
                except:
                    pass               
        return driver
    def visitRigister(self):     #来访登记
        print '来访登记开始'
        L=Login()
        DictSet = L.login(0,0)
        userName = DictSet["userName"]
        print "来访登记用户名为"+ userName
        driver = DictSet["driver"]
        main_handle=driver.current_window_handle
        driver.switch_to_frame('leftFrame')
        driver.find_element_by_link_text(u'待办理').click()
        driver.find_element_by_link_text(u'待办理').click()
        driver.switch_to_default_content()
        driver.switch_to_frame('rightFrame')
        try:
            driver.find_element_by_xpath("//input[@value='来访登记']").click()
        except:
            print '无法找到来访登记按钮，请查时候需要进行“清除默认”和“案件登记“类型设置。'
              
        allhandle=driver.window_handles
        for handle in allhandle:
            if handle != main_handle:
                driver.switch_to_window(handle)
                letter_handle=driver.current_window_handle
                assert u'来访'  in driver.title      
                driver.find_element_by_id('sbjName').clear()
                driver.find_element_by_id('sbjName').send_keys(u'测试123')
                print '找到元素‘住址’，开始填写'
                driver.find_element_by_id("multiSelect").click()
                driver.find_element_by_link_text(u"四川省").click()
                driver.find_element_by_link_text(u"成都市").click()
                driver.find_element_by_link_text(u"锦江区").click()
                driver.find_element_by_css_selector("div.close").click()
                print '找到元素‘判重’，开始判重'
                driver.find_element_by_id("judgement").click()  
                allhandles=driver.window_handles
                for handle in allhandles:
                    if handle != main_handle:
                        if handle != letter_handle:
                            driver.switch_to_window(handle)
                            try:
                                assert u'判重' in driver.title
                            except:
                                print '无法定位到判重页面'   
                            driver.close()
                            print '判重页面已正常关闭' 
                            driver.switch_to_window(letter_handle)       
                            Select(driver.find_element_by_id('sbjSex')).select_by_visible_text(u'女')
                            Select(driver.find_element_by_id("sbjCredentialsType")).select_by_visible_text(u"居民身份证")
#                             driver.find_element_by_id('petitionDefendantName').clear()
#                             driver.find_element_by_id('petitionDefendantName').send_keys(u'测试受信人456')
                            Select(driver.find_element_by_id('matterBelongSystemCode')).select_by_visible_text(u"军队武警")
                            driver.find_element_by_id('belongAreaInput').click()
                            driver.find_element_by_css_selector('#stock_province_item3 > ul.area-list > li > a').click()
                            driver.find_element_by_css_selector('#stock_city_item3  > ul.area-list > li > a').click()
                            driver.find_element_by_css_selector("#belongArea-store-selector > div.close").click()
                            driver.find_element_by_id("FollowPersons").clear()
                            driver.find_element_by_id("FollowPersons").send_keys("1")
                            driver.find_element_by_id("casePeopleNum").clear()
                            driver.find_element_by_id("casePeopleNum").send_keys("2")
                            driver.find_element_by_id('cateMultiSelect').click()
                            driver.find_element_by_link_text(u"农村农业").click()
                            driver.find_element_by_link_text(u"村务管理").click()
                            driver.find_element_by_link_text(u"集体资产管理").click()
                            Select(driver.find_element_by_id("petitionPurposeCode")).select_by_visible_text(u"申诉")
                            driver.find_element_by_id("FollowPersons").clear()
                            driver.find_element_by_id("FollowPersons").send_keys(u"测试随访人789")
                            driver.find_element_by_xpath("(//input[@name='longpendingCaseFlag'])[1]").click()  
                            driver.find_element_by_xpath("(//input[@name='threeCrossoverThreeDivionFlag'])[1]").click()
                            driver.find_element_by_xpath("(//input[@name='dcdbFlag'])[2]").click()#flag为1，就有督察督办标志。
                            Select(driver.find_element_by_id("hotIssuesCode")).select_by_visible_text(u"农民工工资")
                            Select(driver.find_element_by_id("petitionReasonCode")).select_by_visible_text(u"干部作风")
                            driver.find_element_by_id("petitionContent").clear()
                            driver.find_element_by_id("petitionContent").send_keys(u"petitionContent!!这是内容摘要!!")
                            driver.find_element_by_id("petitionRemark").clear()
                            driver.find_element_by_id("petitionRemark").send_keys(u"petitionRemark，这是内容备注!!")
                            driver.find_element_by_id("registerForm").click()
                            driver.find_element_by_id("tipOk").click()
                            print '来访登记成功' 
                            try:
                                driver.switch_to_window(main_handle)
                                assert u'信息管理' in driver.title
                                driver.quit()
                            except:
                                print '没有正常关闭来访登记窗口'    
      
                
                
                
            
        
        
        
        
            
         
         
                    
                
 

                
                
                  
                                    
        
 
        