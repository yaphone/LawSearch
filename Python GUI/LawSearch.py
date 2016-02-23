#!/usr/bin/python
#coding=utf-8

import os
from Tkinter import *
import ttk


class LawSearch():

    def __init__(self):                   #初始化程序
        self.creatWidgets()
        self.getPath()
        self.lawFileName = ''
        self.keyWord = ''
        

        
        
        
    def getPath(self):  #获取当前工作路径
        path = sys.path[0]
        #判断为脚本文件还是py2exe编译后的文件，如果是脚本文件，则返回的是脚本的目录，如果是py2exe编译后的文件，则返回的是编译后的文件路径
        if os.path.isdir(path):
            return path
        elif os.path.isfile(path):
            return os.path.dirname(path)  
        

    
    
    def creatWidgets(self):
        root = Tk()
        root.title('秦皇岛市公安边防支队常用法律查询系统')   #软件标题
        
        
        
        
        #定义相关变量
        
        self.law_filepath = self.getPath() + '/law'      #法律文件路径
        self.items = os.listdir(self.law_filepath)            #法律文件列表
        items = os.listdir(self.law_filepath)        
        
              
        
        
        #定义相关组件,先定义两个顶部Frame
        topFrame = Frame(root).grid(row=0)
        contentFrame = Frame(root).grid(row=1)
        
        
        variable = StringVar(topFrame)
        variable.set("one") # default value        
        
        #菜单选项
        self.label_1 = Label(topFrame, text="请选择法律文件")
        self.select_1 = ttk.Combobox(topFrame, values=items)
        self.select_1.bind('<<ComboboxSelected>>', self.__refresh)
        self.label_2 = Label(topFrame, text="请输入关键字")
        self.entry_2 = Entry()
        self.button_1 = Button(topFrame, text="搜索", command=self.__search)
        
        #搜索结果框
        self.textbox = Text(contentFrame)
        
        
        #topFrame布局
        self.label_1.grid(row=0, column=0, padx=5)
        self.select_1.grid(row=0, column=1, padx=5)
        self.label_2.grid(row=0, column=2, padx=5)
        self.entry_2.grid(row=0, column=3, padx=5)
        self.button_1.grid(row=0, column=4, padx=5)
        
        #contentFram布局
        self.textbox.grid(columnspan=5)   #跨5列， 与topFrame对齐
        
        
        
        #程序进入循环
        root.mainloop()
        
        
    def __refresh(self, event):
        self.lawFileName = self.law_filepath + '/' + self.select_1.get()   #self.select_1选择的法律文件
        
        
        
        
    def __search(self):
        
        file = open(self.lawFileName, mode='r')
        lawFullContent = file.read()                       #法律全文
        keyWord = self.entry_2.get().encode('gbk')
        resaultContent = ''
        
        if keyWord == '':
            resaultContent = lawFullContent.decode('gbk')
        
        else:
            
            keyWordIndex = []
            index = 0
            while (index != -1):                  #文件结尾时结束查询
                index = lawFullContent.find(keyWord, index+1)
                if index != -1:
                    keyWordIndex.append(index)
            if len(keyWordIndex) == 0:
                self.textbox.insert(INSERT, '未找到相关内容')
            else:
                for index1 in keyWordIndex:
                    beginIndex = lawFullContent.find((u'第').encode('gbk'), index1)
                    endIndex = lawFullContent.rfind((u'第').encode('gbk'), index1)
                    resaultContent += lawFullContent[beginIndex:endIndex].decode('gbk')
        self.textbox.insert(INSERT, resaultContent)
                    
                                                
            
                
                

    
    

#打架

if __name__ == "__main__":
    app = LawSearch()
