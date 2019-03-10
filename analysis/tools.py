import jieba
import os

class chat_object:
    def __init__(self,cmd=None,turling=None,turling_key=None):
        self.cmd=cmd
        self.turling=turling
        self.turling_key=turling_key
        

def sex_verify(sex):  # turn 1 or 2 or none to gender
    if sex == 1:
        return 'male'
    elif sex == 2:
        return 'female'
    else:
        return 'unknown'


def place_verify(place, dict_):  # counting and adding the places
    if place not in dict_.keys():
        dict_[place] = 1
    else:
        dict_[place] += 1


def signature_verify(signature):  # or I can't make .md file successfully
    try:
        return signature.replace("\n", "<br>")
    except:
        return None
    

def count_dir(path):
    count = 0
    for file in os.listdir(path):
        count += 1
    return count

def cut_word(signature):
    signature = signature
    words = ''.join(signature)
    res_list = jieba.cut(words, cut_all=True)
    return res_list

def judge_friend(is_friend):
    if is_friend==False:
        return 'no'
    else:
        return 'yes'
    
def None2unknown(str):
    if str==None:
        return 'unknown'
    else:
        return str

def ensure_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)
        print("Create ",path,'\n')

def Dir_init():
    paths=['./data','./data/user','./data/user/Graph',
           './data/user/avatar','./data/group','./data/offical_account']
    add_path=""
    counting=1
    for path in paths:
        if not os.path.exists(path):
            os.mkdir(path)
            add_path+='({}) '.format(str(counting))+path+"\n"
            counting+=1
    if len(add_path)>0:
        print("New add:\n",add_path)

def city_in_province(bot,province):
    city={}
    for person in bot.friends():
        if person.province==province:
            if person.city+'市' in city.keys():
                city[person.city+'市']+=1
            else:
                city[person.city+'市']=1
    return city
