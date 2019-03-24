#-*- coding:gb2312 -*-
import requests
from urllib.parse import *
import re

def get_movie_url(*var):
    """
    
    :param var: (bot, msg, me, cmd, turing_robot, yolo, hero)
    :return:
    """
    try:
        msg=var[1]
        print(msg.text)
        name=msg.text[6:]
        if name=="stop":
            return False
        dict = {'keyword':name.encode("gb2312")}
        url=requests.get("http://s.ygdy8.com/plus/so.php?kwtype=0&"+urlencode(dict))
        url.encoding='gb2312'
        pattern=re.compile(r"<a href='/html/gndy/dyzz/[0-9]+/[0-9]+.html'>.*"+name+".*?</a></b></td>")
        list=re.findall(pattern,url.text)
        if list!=[]:
            for l in list:
                key="http://s.ygdy8.com/html/gndy/dyzz"+l[24:44]
                url2=requests.get(key)
                url2.encoding="gb2312"
                download=re.findall(r'href="ftp.*?">',url2.text)
                print(download)
                if download!=[]:
                    download = download[0][6:-2]
                    msg.reply(download)
                else:
                    msg.reply("Couldn't find the movie!")
            msg.reply("Over")
        else:
            msg.reply("Couldn't find the movie!")
    except Exception as e:
        print(e)
            

