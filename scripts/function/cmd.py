import os


def cmd_on(*var):
    """
    Turn on command mode.
    If the command mode is already enable, switch the terminal.
    :param var: (bot, msg, me, cmd)
    :return: None
    """
    
    try:
        var[0].registered.enable(var[3])
        if var[1].sender not in var[2].cmd:
            var[2].cmd.append(var[1].sender)
        if var[1].sender == var[0].self:
            var[2].cmd.append(var[1].receiver)
        var[1].reply('cmd enable')
    except Exception as e:
        var[1].reply(e)


def cmd_list(*var):
    """
    Show the terminal in cmd mode.
    :param var: (bot, msg, me, cmd)
    :return: None
    """
    var[1].reply(str(var[2].cmd))


def cmd_kill(*var):
    """
    Kill all the cmd mode process
    :param var: (bot, msg, me, cmd)
    :return: None
    """
    var[2].cmd = []
    var[1].reply("kill all cmd")


def cmd_mode(msg,me):
    """
    cmd mode callback function
    :param msg: Message
    :param me: custom class me
    :return: None
    """
    if msg.text == 'cmd off':
        try:
            msg.reply('cmd disable')
            if msg.sender in me.cmd:
                me.cmd.remove(msg.sender)
            if msg.receiver in me.cmd:
                me.cmd.remove(msg.receiver)
        except Exception as e:
            msg.reply(e)
    elif msg.text[0:3] == 'cd ':
        try:
            output = os.popen(msg.text + " && ls").read()
            os.chdir(msg.text[3:])
            msg.reply(output)
        except Exception as e:
            msg.reply(e)
    elif msg.text[0:5] == 'show ':
        try:
            output = os.popen('file ' + msg.text[5:]).read()
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
