# -*- coding: UTF-8 -*- 
from basis.caseOperation import caseOperation 
class operation():
    # ***********交办**************
#     caseId =  raw_input("请输入需要转办的案件编号：",)
#     print caseId
    caseId = "CD201600012676"   #在这边填上需要交办的案件编号
    department1 = u"四川省成都市青羊区委区政府信访局"    #在这边填上需要转办的单位
    department2 = u"四川省成都市青羊区太升路街道办事处"
    As = caseOperation()
    As.forward(caseId,department1,0,0) #第一次转办，登录的账号为 admin                                      
    As.forward(caseId,department2,3,1) # 第二次转办，登录的账号为abqxfjqh
    acceptDriver = As.acceptCase(caseId,6,1)
    As.substantiveHandle(caseId,6,1)
    As.selfHandle(caseId,6,1)
    
    
    
    
    
    
        
    
