def turing_on(*var):
    """
    Turn on Turing Robot
    :param var: (bot, msg, me, cmd, turing_robot)
    :return: None
    """
    try:
        var[0].registered.enable(var[4])
        if var[1].sender not in var[2].turing:
            var[2].turing.append(var[1].sender)
        if var[1].sender == var[0].self:
            var[2].turing.append(var[1].receiver)
        var[1].reply('turing enable')
    except Exception as e:
        var[1].reply(e)


def turing_list(*var):
    """
    List the Turing Robot Terminals
    :param var: (bot, msg, me, cmd, turing_robot)
    :return: None
    """
    var[1].reply(str(var[2].turing))


def turing_kill(*var):  # var=(bot, msg, me, cmd, turing_robot)
    """
    Kill all Turing Robot processes
    :param var: (bot, msg, me, cmd, turing_robot)
    :return: None
    """
    var[2].turing = []
    var[1].reply("kill all the turing process")
    
    
def turing_mode(msg, me, bot):
    """
    Turing mode callback function
    :param msg: Message
    :param me: custom class me
    :param bot: bot
    :return: None
    """
    
    if msg.text == 'turing off':
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

