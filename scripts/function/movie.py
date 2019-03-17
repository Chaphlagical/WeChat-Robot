#-*- coding:gb2312 -*-
import requests
import re
from urllib.parse import *
import os
from tkinter import*
from tkinter.messagebox import *
from tkinter.filedialog import askdirectory

download=""

def get_movie_url(name):
    global download
    if name=="stop":
        return False
    dict = {'keyword':name.encode("gb2312")}
    url=requests.get("http://s.ygdy8.com/plus/so.php?kwtype=0&"+urlencode(dict))
    url.encoding='gb2312'
    pattern=re.compile(r"<a href='/html/gndy/dyzz/[0-9]+/[0-9]+.html'>.*"+name+".*?</a></b></td>")
    list=re.findall(pattern,url.text)
    if list!=[]:
        key="http://s.ygdy8.com/html/gndy/dyzz"+list[0][24:44]
        url2=requests.get(key)
        url2.encoding="gb2312"
        download=re.findall(r'href="ftp.*?">',url2.text)
        if download!=[]:
            download = download[0][6:-2]
            showinfo("Tip","Get url successfully!")
        else:
            showwarning("warning","Couldn't find the movie!")
            
            
get_movie_url("蜘蛛侠")