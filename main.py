# -*- coding:utf-8 -*-
from wxpy import*
from analysis.user_analysis import*
from analysis.group_analysis import *
from scripts import hath
from analysis.CV.cv import *

Dir_init()

bot=Bot(console_qr=False,cache_path=True)
bot.enable_puid()
me=chat_object(cmd=[],turing=[],yolo=[],turing_key=Tuling(api_key='d9c69eac59ea4dddb70534bb63d0e712'))


@bot.register(except_self=False,msg_types=TEXT)
def init(msg):
    print(msg)
    global me
    if 'cmd' in msg.text:
        
        '''
        Trigger about command terminal
        '''
        
        if msg.text == 'cmd on':
            
            
            '''
            Turn on command mode
            If the command mode is already enable, switch the terminal
            '''
            
            try:
                bot.registered.enable(cmd)
                if msg.sender not in me.cmd:
                    me.cmd.append(msg.sender)
                if msg.sender == bot.self:
                    me.cmd.append(msg.receiver)
                msg.reply('cmd enable')
            except Exception as e:
                msg.reply(e)
                
        elif msg.text == 'cmd list':
            msg.reply(str(me.cmd))
            
        elif msg.text == 'cmd kill':
            me.cmd=[]
            msg.reply("kill all cmd")
    
    elif 'turing' in msg.text:
        
        '''
        Trigger about turing robot
        '''
        
        if msg.text == 'turing on':
            
            '''
            Turn on turing robot mode
            If the turing robot mode is already enable, switch the terminal
            '''
            
            try:
                bot.registered.enable(turing_robot)
                if msg.sender not in me.turing:
                    me.turing.append(msg.sender)
                if msg.sender == bot.self:
                    me.turing.append(msg.receiver)
                msg.reply('turing enable')
            except Exception as e:
                msg.reply(e)

        elif msg.text == 'turing list':
            msg.reply(str(me.turing))
        
        elif msg.text == 'turing kill':
            me.turing=[]
            msg.reply("kill all the turing process")
    
    elif '蛤' in msg.text or 'hath' in msg.text:
        '''
        Show respect to that elder through key words
        '''
        msg.reply(hath.hath())
    
    elif 'analysis' in msg.text:
        msg.reply("Begin to analysis")
        try:
            if 'friends' in msg.text:
                user_friends = User_Friends(bot)
                user_friends.analysis()
                msg.reply("Succseefully!")
                return
            elif 'all' in msg.text and 'group' in msg.text:
                for group in bot.groups():
                    msg.reply("analysing "+group.name)
                    user_group=User_Group(bot,group)
                    user_group.analysis()
                msg.reply("Succseefully!")
                return
            else:
                for group in bot.groups():
                    if group.name in msg.text:
                        msg.reply("analysing " + group.name)
                        user_group=User_Group(bot,group)
                        user_group.analysis()
                        msg.reply("Succseefully!")
                        return
        except Exception as e:
            print(e)
        msg.reply("Target not exists or you haven't add it to contract")
    
    elif 'check' in msg.text:
        if 'friend' in msg.text:
            user_friends=User_Friends(bot)
            user_friends.check(msg)
        elif 'group' in msg.text:
            user_group=User_Group(bot,bot.groups()[0])
            user_group.check(msg)
            
    elif 'yolo' in msg.text:
        
        '''
        Trigger about yolo object detection
        '''
    
        if msg.text == 'yolo on':

            '''
            Turn on yolo detection mode
            If the yolo detection mode is already enable, switch the terminal
            '''
        
            try:
                bot.registered.enable(yolo)
                if msg.sender not in me.yolo:
                    me.yolo.append(msg.sender)
                if msg.sender == bot.self:
                    me.yolo.append(msg.receiver)
                msg.reply('yolo enable')
            except Exception as e:
                msg.reply(e)
    
        elif msg.text == 'yolo list':
            msg.reply(str(me.yolo))
            
        elif msg.text == 'yolo off':
            try:
                msg.reply('yolo disable')
                if msg.receiver in me.yolo:
                    me.yolo.remove(msg.receiver)
                if msg.sender in me.yolo:
                    me.yolo.remove(msg.sender)
            except Exception as e:
                msg.reply(e)
    
        elif msg.text == 'yolo kill':
            me.yolo = []
            msg.reply("kill all cmd")
    

@bot.register(chats=me.yolo,msg_types=PICTURE or VIDEO,except_self=False)
def yolo(msg):
    print(msg)
    try:
        if msg.type==PICTURE:
            Yolo_img(msg)
        elif msg.type==VIDEO:
            Yolo_video(msg)
    except Exception as e:
        print(e)
        


@bot.register(chats=me.cmd,msg_types=TEXT,except_self=False,enabled=False)
def cmd(msg):
    global me
    if msg.text=='cmd off':
        try:
            msg.reply('cmd disable')
            if msg.sender in me.cmd:
                me.cmd.remove(msg.sender)
            if msg.receiver in me.cmd:
                me.cmd.remove(msg.receiver)
        except Exception as e:
            msg.reply(e)
    elif msg.text[0:3]=='cd ':
        try:
            output = os.popen(msg.text+" && ls").read()
            os.chdir(msg.text[3:])
            msg.reply(output)
        except Exception as e:
            msg.reply(e)
    elif msg.text[0:5]=='show ':
        try:
            output=os.popen('file '+msg.text[5:]).read()
            if 'image' in output:
                msg.reply_image(msg.text[5:])
            if 'video' in output:
                msg.reply_video(msg.text[5:])
            else:
                msg.reply_file(msg.text[5:])
        except Exception as e:
            msg.reply(e)
    
    else:
        try:
            output = os.popen(msg.text).read()
            msg.reply(output)
        except Exception as e:
            msg.reply(e)
           
            
@bot.register(chats=me.turing,except_self=False,enabled=False)
def turing_robot(msg):
    if msg.text=='turing off':
        try:
            msg.reply('turing disable')
            if msg.receiver in me.turing:
                me.turing.remove(msg.receiver)
            if msg.sender in me.turing:
                me.turing.remove(msg.sender)
        except Exception as e:
            msg.reply(e)
    elif msg.is_at or msg.sender in bot.friends():
        me.turing_key.do_reply(msg)
    

embed()










