from pyecharts import Map
import pyecharts as pye
from pyecharts import WordCloud
from analysis.tools import *



class User_Friends:
    def __init__(self, bot):
        self.bot = bot
        self.sex = {'male': 0, 'female': 0, 'unknown': 0}
        self.province = {}
        self.city = {}
        self.signature = []
    
    def statistics(self, save_avatar=False):
        for friend in self.bot.friends(update=True):
            self.sex[sex_verify(friend.sex)] += 1
            place_verify(friend.province, self.province)
            place_verify(friend.city, self.city)
            self.signature.append(friend.signature)
            if save_avatar:
                ensure_dir('./data/user/avatar')
                friend.get_avatar("./data/user/avatar/" + friend.name + '.jpg')
    
    def write_data(self):
        save_avatar = False
        ensure_dir('./data/user/avatar')
        if count_dir("./data/user/avatar") < len(self.bot.friends(update=True)):
            save_avatar = True
        ensure_dir('./data/user')
        data = open("./data/user/user_friends_data.md", 'wt')
        data.write("|Nick_name|Name|Gender|Province|City|Signature|Avatar|\n")
        data.write("|---------|----|------|--------|----|---------|------|\n")
        for friend in self.bot.friends(update=True):
            if save_avatar:
                friend.get_avatar('./data/user/avatar/' + friend.name + '.jpg')
            data.write("|{}|{}|{}|{}|{}|{}|{}| \n".format(friend.nick_name, friend.name, sex_verify(friend.sex),
                                                          None2unknown(friend.province), None2unknown(friend.city),
                                                          None2unknown(signature_verify(friend.signature)),
                                                          '![](./avatar/' + friend.name + '.jpg' + ')'))
        data.write(self.bot.friends().stats_text())
        data.close()

    def graph(self):
        if len(self.province)==0:
            self.statistics()
        x = ["male", "female", "unknown"]
        y = [self.sex['male'],self.sex['female'],self.sex['unknown']]
        pie = pye.Pie("Gender",'Gender',width=1400,height=800)
        pie.add("Gender", x, y, is_label_show=True)
        pie.render(path="./data/user/Graph/Gender.html")
        map = Map("China", 'China', width=1400, height=800)
        map.add("China", self.province.keys(), self.province.values(), visual_range=[0, 50], maptype='china', is_visualmap=True,
                visual_text_color='#000')
        map.render(path="./data/user/Graph/China.html")

        max_province=max(self.bot.friends().stats()['province'], key=self.bot.friends().stats()['province'].get)
        city = city_in_province(self.bot, max_province)
        map = Map(max_province, max_province, width=1400, height=800)
        map.add(max_province, city.keys(), city.values(), visual_range=[0, 50], maptype=max_province,
                is_visualmap=True,
                visual_text_color='#000')
        map.render(path="./data/user/Graph/"+max_province+".html")
        
        words_list=cut_word(self.signature)
        words = ' '.join(words_list)
        words=words.split(" ")
        w = words
        for i in words:
            if len(i)<=1:
                w.remove(i)
            try:
                w.remove('span')
                w.remove('class')
                w.remove('emoji')
                w.remove('emoji1f389')
            except:
                pass
        dict_w={}
        for i in w:
            if i not in dict_w.keys():
                dict_w[i]=1
            else:
                dict_w[i]+=1
        wordcloud = WordCloud(width=1400, height=800)
        wordcloud.add("Signature", dict_w.keys(), dict_w.values(), word_size_range=[20, 100])
        wordcloud.render(path="./data/user/Graph/Signature.html")

    def analysis(self):
        Dir_init()
        self.statistics()
        self.write_data()
        self.graph()
    
    def check(self,msg):
        for friend in self.bot.friends():
            if friend.name in msg.text:
                msg.reply("nick_name:{}\nname:{}\nsex:{}\nprovince:{}\ncity:{}\nsignature:{}".format(
                    friend.nick_name, friend.name, sex_verify(friend.sex),
                    None2unknown(friend.province), None2unknown(friend.city),
                    None2unknown(signature_verify(friend.signature))))
                msg.reply_image('./data/user/avatar/' + friend.name + '.jpg')
