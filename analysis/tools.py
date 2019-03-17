import jieba
import os


class chat_object:
    """
    The class content operation terminal and param
    """
    def __init__(self, cmd=None, turing=None, turing_key=None, yolo=None, turn_hero=None):
        self.cmd = cmd
        self.turing = turing
        self.turing_key = turing_key
        self.yolo = yolo
        self.yolo_num = 0
        self.turn_hero=turn_hero
        self.hero_num = 0


def sex_verify(sex):  # turn 1 or 2 or none to gender
    """
    Turn num to string
    :param sex: gender
    :return: 'male' or 'female' or 'unknown'
    """
    if sex == 1:
        return 'male'
    elif sex == 2:
        return 'female'
    else:
        return 'unknown'


def place_verify(place, dict_):  # counting and adding the places
    """
    Counting the place and save in the dict
    :param place: name of the place
    :param dict_: the place dict
    :return: None
    """
    if place not in dict_.keys():
        dict_[place] = 1
    else:
        dict_[place] += 1


def signature_verify(signature):  # or I can't make .md file successfully
    """
    Replace the '\n' in the signature by '<br>'
    :param signature: Signature
    :return: string
    """
    try:
        return signature.replace("\n", "<br>")
    except:
        return None


def count_dir(path):
    """
    counting the number of files in the path
    :param path: path
    :return: num
    """
    count = 0
    for file in os.listdir(path):
        count += 1
    return count


def cut_word(signature):
    """
    Cut the sentence into words
    :param signature: signature
    :return: words list
    """
    signature = signature
    words = ''.join(signature)
    res_list = jieba.cut(words, cut_all=True)
    return res_list


def judge_friend(is_friend):
    """
    Verify if friend
    :param is_friend:
    :return: 'yes' or 'no'
    """
    if is_friend:
        return 'yes'
    else:
        return 'no'


def None2unknown(str):
    """
    Turn None to 'unknown'
    :param str:
    :return: string
    """
    if str is None:
        return 'unknown'
    else:
        return str


def ensure_dir(path):
    """
    If the path isn't exist, create it
    :param path:
    :return: None
    """
    if not os.path.exists(path):
        os.mkdir(path)
        print("Create ", path, '\n')


def Dir_init():
    """
    Create the basic path
    :return: None
    """
    paths = ['./data', './data/user', './data/user/Graph',
             './data/user/avatar', './data/group', './data/offical_account']
    add_path = ""
    counting = 1
    for path in paths:
        if not os.path.exists(path):
            os.mkdir(path)
            add_path += '({}) '.format(str(counting)) + path + "\n"
            counting += 1
    if len(add_path) > 0:
        print("New add:\n", add_path)


def city_in_province(bot, province):
    """
    Create city dictionary from province list
    :param bot:
    :param province:
    :return: city_dict
    """
    city = {}
    for person in bot.friends():
        if person.province == province:
            if person.city + '市' in city.keys():
                city[person.city + '市'] += 1
            else:
                city[person.city + '市'] = 1
    return city

