# -*- coding:utf-8 -*-
from scripts.func import *

Dir_init()
bot = Bot(console_qr=False, cache_path=True)
bot.enable_puid()
me = chat_object(cmd=[], turing=[], yolo=[], turing_key=Tuling(api_key='d9c69eac59ea4dddb70534bb63d0e712'))


@bot.register(except_self=False, msg_types=TEXT)
def init(msg):
    print(msg)
    global me
    try:
        for key in func_dict.keys():
            if key in msg.text:
                func_dict[key](bot, msg, me, cmd, turing_robot, yolo)
    except Exception as e:
        print(e)


@bot.register(chats=me.yolo, msg_types=PICTURE or VIDEO, except_self=False)
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
    global me
    turing_mode(bot, me, msg)


embed()



