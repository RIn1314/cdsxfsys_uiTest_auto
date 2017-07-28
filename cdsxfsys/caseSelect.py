# -*- coding: UTF-8 -*- 
from basis.caseOperation import caseOperation
from Tkinter import *

class caseSelect():
    #案件查询
    def create_window(self, master):

        b2 = Button(master, text = '开始查询')
        b2.grid(row = 6,column = 0, columnspan = 3)
        b2.bind('<Button-1>',self.button_click)
              
        e = StringVar()
        self.e1 = Entry(master,width = 30,textvariable = e ) 
        e.set('             在此输入信访件编号')
        
        self.e1.grid(row = 3,column = 0, columnspan = 3)
               
        Label(master,
              fg = 'red',
              bg = 'SystemButtonShadow',
              width = 40,
              height = 2, 
              text = '成都正式系统').grid(row = 0, column = 0, columnspan = 3)
         
    def button_click(self,event):       
        caseId =  self.e1.get()
        o = caseOperation()
        o.caseSelect(caseId)
        
if '__main__' == __name__:
    root = Tk()
    caseSelect = caseSelect()
    caseSelect.create_window(root)
    root.resizable(False, False)   
    root.geometry('300x100+10+10')    
    root.title('案件查询')      
    root.iconbitmap('redSaber.ico')
    root.mainloop()
    





