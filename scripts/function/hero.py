from wxpy import*
from analysis.CV.cv import *

hero_dict=["shazam.jpg"]


def hero_on(*var):
    """
    
    :param var: (bot, msg, me, cmd, turing_robot, yolo, hero)
    :return:
    """
    try:
        var[0].registered.enable(var[6])
        if var[1].sender not in var[2].turn_hero:
            var[2].turn_hero.append(var[1].sender)
        if var[1].sender == var[0].self:
            var[2].turn_hero.append(var[1].receiver)
        var[1].reply('hero enable')
        print("hero enable")
    except Exception as e:
        var[1].reply(e)


def hero_list(*var):
    """
    
    :param var:
    :return:
    """
    var[1].reply(str(var[2].turn_hero))
    

def hero_mode(msg, me):
    """
    
    :param msg:
    :param me:
    :return:
    """
    if me.hero_num == 0:
        try:
            print(msg)
            if 'PRNet' not in os.getcwd():
                os.chdir('./analysis/CV/PRNet')
                
            if msg.type == PICTURE:
                print("get picture")
                msg.get_file(save_path="Hero/temp.jpg")
            elif msg.type == TEXT:
                if msg.text=="hero off":
                    try:
                        msg.reply('hero disable')
                        if msg.receiver in me.turn_hero:
                            me.turn_hero.remove(msg.receiver)
                        if msg.sender in me.turn_hero:
                            me.turn_hero.remove(msg.sender)
                    except Exception as e:
                        msg.reply(e)
                if msg.text=="hero kill":
                    me.turn_hero = []
                    msg.reply("kill all hero")
                else:
                    for hero in hero_dict:
                        if msg.text in hero:
                            print("process")
                            me.hero_num = 1
                            turn_hero(msg, "Hero/material/"+hero)
            me.hero_num = 0
            os.chdir('../../..')
        except Exception as e:
            me.hero_num = 0
            print(e)

