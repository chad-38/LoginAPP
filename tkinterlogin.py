# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 13:47:42 2021

@author: Chad.Daud
"""
from tkinter import *
class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Software Access")
        Label(self.master,text="Username & Password").grid(row=1,column=1,columnspan=2, pady=4)
        Label(self.master,text="Username").grid(row=2,column=1, columnspan=1, pady=4)
        self.username=Entry(self.master, width=10).grid(row=2, column=2 )
        Label(self.master,text="Password").grid(row=3,column=1, pady=4)
        self.password=Entry(self.master, width=10).grid(row=3, column=2 )
        
        
root=Tk()
Login(root)
root.mainloop()
