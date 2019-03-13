from wxpy import*
from analysis.CV.cv import *

def yolo_on(*var):
    """
    Turn on yolo object detection mode
    :param var: (bot, msg, me, cmd, turing_robot, yolo)
    :return: None
    """
    try:
        var[0].registered.enable(var[5])
        if var[1].sender not in var[2].yolo:
            var[2].yolo.append(var[1].sender)
        if var[1].sender == var[0].self:
            var[2].yolo.append(var[1].receiver)
        var[1].reply('yolo enable')
    except Exception as e:
        var[1].reply(e)


def yolo_list(*var):
    """
    List the terminal in yolo mode
    :param var: (bot, msg, me, cmd, turing_robot, yolo)
    :return: None
    """
    var[1].reply(str(var[2].yolo))


def yolo_off(*var):
    """
    Turn off yolo mode
    :param var: (bot, msg, me, cmd, turing_robot, yolo)
    :return: None
    """
    try:
        var[1].reply('yolo disable')
        if var[1].receiver in var[2].yolo:
            var[2].yolo.remove(var[1].receiver)
        if var[1].sender in var[5].yolo:
            var[5].yolo.remove(var[1].sender)
    except Exception as e:
        var[1].reply(e)


def yolo_kill(*var):
    """
    Kill all yolo process
    :param var: (bot, msg, me, cmd, turing_robot, yolo)
    :return: None
    """
    var[2].yolo = []
    var[1].reply("kill all cmd")


def yolo_mode(msg, me):
    if me.yolo_num == 0:
        try:
            me.yolo_num = 1
            if msg.type == PICTURE:
                Yolo_img(msg)
            elif msg.type == VIDEO:
                Yolo_video(msg)
            me.yolo_num = 0
        except Exception as e:
            me.yolo_num = 0
            print(e)
