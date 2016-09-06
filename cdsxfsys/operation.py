# -*- coding: UTF-8 -*- 
from basis.caseOperation import caseOperation 
from time import sleep

class operation():
    # ***********交办**************
    caseId = "CD201600002843"   #在这边填上需要交办的案件编号
    As = caseOperation()
    acceptDriver = As.acceptCase(caseId,6,1)
    As.substantiveHandle(acceptDriver, caseId)