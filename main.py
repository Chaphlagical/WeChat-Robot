# -*- coding:utf-8 -*-
from scripts.func import *
from GUI.gui import *
import datetime

if __name__ == '__main__':
    args = parse_args()
    win = Win()
    Dir_init()
    bot = Bot(console_qr=QR_Mode[args.QR_Code], cache_path=True)
    bot.enable_puid()
    me = chat_object(cmd=[], turing=[], yolo=[], turing_key=Tuling(api_key='d9c69eac59ea4dddb70534bb63d0e712'),turn_hero=[])
    if GUI_Mode[args.gui] == True:
        Set_Win(win, bot)
    
    @bot.register(except_self=False, msg_types=TEXT)
    def init(msg):
        win.input['log'].insert(tk.END,"("+str(datetime.datetime.today())+")"+str(msg)+"\n")
        global me
        try:
            for key in func_dict.keys():
                if key in msg.text:
                    func_dict[key](bot, msg, me, cmd, turing_robot, yolo, hero)
        except Exception as e:
            print(e)
    
    
    @bot.register(chats=me.yolo, msg_types=PICTURE, except_self=False)
    def yolo(msg):
        global me
        print(msg)
        yolo_mode(msg, me)
    
    
    @bot.register(chats=me.cmd, msg_types=TEXT, except_self=False, enabled=False)
    def cmd(msg):
        global me
        cmd_mode(msg, me)
    
    
    @bot.register(chats=me.turing, except_self=False, enabled=False)
    def turing_robot(msg):
        print(msg)
        global me
        turing_mode(msg, me, bot)
    
    
    @bot.register(chats=me.turn_hero,except_self=False,enabled=True)
    def hero(msg):
        global me
        hero_mode(msg,me)
    
    
    if GUI_Mode[args.gui]==True:
        im = Image.open("/home/chaf/Program/Python/HW1/GUI/avatar.gif")
        im = ImageTk.PhotoImage(im)
        win.canvas.create_image(225, 170, image=im)
        win.loop()
    
    embed()
