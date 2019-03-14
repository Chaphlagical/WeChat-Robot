from analysis.user_analysis import *
from analysis.group_analysis import *


def analysis_friends(*var):
    """
    Analysis your friends circle
    :param var: (bot, msg, me)
    :return: None
    """
    try:
        user_friends = User_Friends(var[0])
        user_friends.analysis()
        var[1].reply("Succseefully!")
    except Exception as e:
        var[1].reply(e)


def analysis_all_group(*var):
    """
    Analysis all your WeChat groups
    :param var: (bot, msg, me)
    :return: NOne
    """
    try:
        for group in var[0].groups():
            var[1].reply("analysing " + group.name)
            user_group = User_Group(var[0], group)
            user_group.analysis()
        var[1].reply("Succseefully!")
    except Exception as e:
        var[1].reply(e)


def analysis_group(*var):
    """
    Analysis the single WeChat group
    :param var: (bot, msg, me)
    :return: None
    """
    try:
        for group in var[0].groups():
            if group.name in var[1].text:
                var[1].reply("analysing " + group.name)
                user_group = User_Group(var[0], group)
                user_group.analysis()
                var[1].reply("Succseefully!")
                return
    except Exception as e:
        var[1].reply(e)
    var[1].reply("Target not exists or you haven't add it to contract")


def check_friend(*var):
    """
    Show your friend's information
    :param var: (bot, msg, me)
    :return: None
    """
    user_friends = User_Friends(var[0])
    user_friends.check(var[1])


def check_group(*var):
    """
    Show your group's information
    :param var: (bot, msg, me)
    :return: None
    """
    user_group = User_Group(var[0], var[0].groups()[0])
    user_group.check(var[1])
