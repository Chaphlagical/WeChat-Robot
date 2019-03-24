import tkinter as tk
from tkinter.messagebox import *
import tkinter.ttk as ttk


class Win:
    def __init__(self):
        self.tk=None
        self.canvas=None
        self.select={}
        self.input = {}
        self.object=None
        
    def init(self,title,size,bg):
        self.tk=tk.Tk()
        self.tk.title(title)
        self.tk.maxsize=size
        self.tk.minsize=size
        self.tk.resizable(width=False,height=False)
        
        self.canvas=tk.Canvas(self.tk,width=size[0],height=size[1],bg=bg)
        self.canvas.pack()
        
    def add_button(self,name,position,command,size=(4,2)):
        self.canvas.create_window(position[0],position[1],window=tk.Button(self.tk,text=name,width=size[0],height=size[1],command=command))

    def add_label(self,text,bg,position):
        self.canvas.create_window(position[0],position[1],window=tk.Label(self.tk,text=text,bg=bg))
        
    def add_selectbox(self,name,key,width,position):
        if name in self.select.keys():
            raise ERROR
        self.select[name]=tk.StringVar()
        selectbox=ttk.Combobox(self.tk,width=width,textvariable=self.select[name],state='readonly')
        selectbox['values']=key
        selectbox.current(0)
        self.canvas.create_window(position[0],position[1],window=selectbox)
        
    def get_select(self,name):
        return self.select[name].get()
    
    def add_input(self,name,size,position):
        if name in self.input.keys():
            raise ERROR
        self.input[name]=tk.Text(self.tk,width=size[0], height=size[1])
        self.canvas.create_window(position[0],position[1],window=self.input[name])
        
    def get_input(self,name):
        return self.input[name].get("0.0","end")
    
    def loop(self):
        self.tk.mainloop()

