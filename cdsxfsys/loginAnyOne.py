# -*- coding: UTF-8 -*- 
from basis.Login import Login
class temp():
    L=Login()
    i = {1}          
    for x in i:
        if x == 1:
            L.login(0,0)
        elif x == 2:
            L.login(3,1) #青羊信访来信，曲浩
        elif x == 3:
            L.login(6,1) #太升路街道办，陶宏
        elif x == 4:
            L.login(7,1) #金牛信访来信，吕荣军
        else:
            L.login(11,1) #成都信访领导，张馨
                