# -*- coding: UTF-8 -*- 
from basis.caseOperation import caseOperation 
class operation():
    # ***********交办**************
    caseId = "CD201600012676"   #在这边填上需要交办的案件编号
    department1 = u"四川省成都市青羊区委区政府信访局"    #在这边填上需要交办的单位
    department2 = u"四川省成都市青羊区太升路街道办事处"
    As = caseOperation()
    As.assgin(caseId,department1,0,0) #第一次交办，登录的账号为 admin                                  
    As.assgin(caseId,department2,3,1) # 第二次交办，登录的账号为abqxfjqh
    As.acceptCase(caseId,6,1)
    As.substantiveHandle(caseId,6,1)
    As.selfHandle(caseId,6,1)
    
    
    
    
    
    
        
    
