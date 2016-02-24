#!/usr/bin/python
#coding=utf-8

import os
from Tkinter import *
import ttk
import sys
import tkMessageBox
import time

reload(sys)
sys.setdefaultencoding('utf-8')


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
        items = [i.decode('gbk') for i in items]
       
        
        #定义相关组件,先定义两个顶部Frame
        menubar = Menu(root)
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
        
    
        aboutMenu = Menu(menubar, tearoff=0)
        aboutMenu.add_command(label="关于", command=self.aboutInfo)
               
        onlineUpdateMenu = Menu(menubar, tearoff=0)
        onlineUpdateMenu.add_command(label="在线升级", command=self.onlineUpdateInfo)    
        
        helpMenu = Menu(menubar, tearoff=0)
        helpMenu.add_command(label="帮助", command=self.helpInfo)         
                
        #创建关于菜单并添加相关信息
        menubar.add_cascade(label="关于", menu=aboutMenu)
        menubar.add_cascade(label="在线升级", menu=onlineUpdateMenu)
        menubar.add_cascade(label="帮助", menu=helpMenu)
        root.config(menu=menubar)        
        
  
        #程序进入循环
        root.mainloop()
        
        
    def __refresh(self, event):
        self.lawFileName = self.law_filepath + '/' + self.select_1.get()   #self.select_1选择的法律文件
        
        
    def aboutInfo(self):
        aboutStr = "秦皇岛公安边防支队常用法律查询系统 beta版\n 作者：中国有我一定黄 \n QQ：763665453"
        tkMessageBox.showinfo("关于", aboutStr)
    
    def onlineUpdateInfo(self):
        tkMessageBox.showinfo("在线升级", "在线升级中，请稍候...")
        time.sleep(5)
        tkMessageBox.showinfo("在线升级", "升级完成")
    
    def helpInfo(self):
        tkMessageBox.showinfo("帮助", "你想要啥帮助，自己摸索吧！")
   
        
    #法律查询逻辑
        
    def __search(self):
        
        self.textbox.delete('1.0', END)
        
        file = open(self.lawFileName, mode='r')
        lawFullContent = file.read().decode('utf-8')                       #法律全文
        keyWord = self.entry_2.get()
        resaultContent = ''
        
        if keyWord == '':
            resaultContent = lawFullContent
        
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
                    beginIndex = lawFullContent.decode('utf-8')[:index1].rfind('第')
                    endIndex = lawFullContent.find('第', index1)
                    addContent = lawFullContent.decode('utf-8')[beginIndex:endIndex]
                    if addContent not in resaultContent:
                        resaultContent += addContent
        self.textbox.insert(INSERT, resaultContent)

if __name__ == "__main__":
    app = LawSearch()
