#!/usr/bin/python
#coding=utf-8

import os
from Tkinter import *
import ttk


class LawSearch():

    def __init__(self):                   #初始化程序
        self.creatWidgets()
    
    def creatWidgets(self):
        root = Tk()
        root.title('秦皇岛市公安边防支队常用法律查询系统')   #软件标题
        
        
        
        
        #定义相关变量
        
        items = ['one', 'tow', 'three']
              
        
        
        #定义相关组件,先定义两个顶部Frame
        topFrame = Frame(root).grid(row=0)
        contentFrame = Frame(root).grid(row=1)
        
        
        variable = StringVar(topFrame)
        variable.set("one") # default value        
        
        #菜单选项
        label_1 = Label(topFrame, text="请选择法律文件")
        select_1 = ttk.Combobox(topFrame, values=items)
        label_2 = Label(topFrame, text="请输入关键字")
        entry_2 = Entry()
        button_1 = Button(topFrame, text="搜索")
        
        #搜索结果框
        textbox = Text(contentFrame)
        
        
        #topFrame布局
        label_1.grid(row=0, column=0, padx=5)
        select_1.grid(row=0, column=1, padx=5)
        label_2.grid(row=0, column=2, padx=5)
        entry_2.grid(row=0, column=3, padx=5)
        button_1.grid(row=0, column=4, padx=5)
        
        #contentFram布局
        textbox.grid(columnspan=5)   #跨5列， 与topFrame对齐
        
        
        
        
        
        #程序进入循环
        root.mainloop()
    
    
    



if __name__ == "__main__":
    app = LawSearch()
