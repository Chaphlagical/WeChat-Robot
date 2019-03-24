from GUI.gui_class import *
from wxpy import*
from PIL import Image,ImageTk
from tkinter.messagebox import *


'''bot = Bot(console_qr=False, cache_path=True)
bot.enable_puid()

win=Win()'''

def Get_Friend(win,bot):
    win.input['object'].delete('1.0','end')
    win.object=win.get_select('friend')
    if win.object!=bot.self.name:
        win.input['object'].insert(tk.END,win.object)
    win.tk.update()
    win.tk.update_idletasks()
    pass


def Get_Group(win,bot):
    win.input['object'].delete('1.0', 'end')
    win.object = win.get_select('group')
    win.input['object'].insert(tk.END, win.object)
    win.tk.update()
    win.tk.update_idletasks()
    

def Send_msg(win,bot):
    obj=bot.friends().search(win.get_input('object'))
    if len(obj)==0:
        obj=bot.groups().search(win.get_input('object'))
    if len(obj)==0:
        showerror("Error","couldn't find the friend or group!")
    obj[0].send(win.get_input('chat'))
    win.input['chat'].delete('1.0', 'end')
    win.tk.update()
    win.tk.update_idletasks()
    
    
def Save(win,bot):
    f=open("chat.log","wt")
    f.write(win.get_input('log'))
    f.close()
    showinfo("tips","Chatting Record save")


def Set_Win(win,bot):
    win.init(title="WeChat Robot by Chaf", size=(500, 600), bg='white')
    win.object=bot.friends()[0]
    win.add_selectbox('friend',[i.name for i in bot.friends()],width=5,position=(100,200))
    win.add_selectbox('group', [i.name for i in bot.groups()], width=20, position=(160, 240))
    win.add_button('Send',(100,580),command=lambda :Send_msg(win,bot),size=(4,1))
    win.add_button('Save',(370,580),command=lambda :Save(win,bot),size=(4,1))
    win.add_button(' friends ', (40, 200), command=lambda :Get_Friend(win,bot),size=(4,1))
    win.add_button(' groups ', (40, 240), command=lambda :Get_Group(win,bot),size=(4,1))
    win.add_input('object',size=(28,1),position=(130,280))
    win.add_input('chat', size=(28, 15), position=(130, 430))
    win.add_input('log', size=(28, 15), position=(370, 430))

