from analysis.tools import *
import pyecharts as pye


class User_Group():
    def __init__(self,bot,group):
        self.group=group
        self.bot=bot
        self.stranges=[]
        self.friends=[]
        
    def statistics(self):
        for member in self.group.members:
            if member.is_friend:
                self.stranges.append(member)
            else:
                self.friends.append(member.is_friend)
                
    def write_data(self):
        path="./data/group/"+self.group.name
        ensure_dir(path)
        ensure_dir(path+'/avatar')
        save_avatar = False
        if count_dir(path+'/avatar') < len(self.bot.friends(update=True)):
            save_avatar = True
            
        data = open(path+"/group_members_data.md", 'wt')

        data.write("|Nick_name|Name|Frined?|Gender|Province|City|Signature|Avatar|\n")
        data.write("|---------|----|-------|------|--------|----|---------|------|\n")
        
        for member in self.group.members:
            if member.is_friend!=False:
                member=member.is_friend
            if save_avatar:
                member.get_avatar(path+'/avatar/' + member.name + '.jpg')
            data.write("|{}|{}|{}|{}|{}|{}|{}|{}| \n".format(member.nick_name, member.name,
                                                             None2unknown(judge_friend(member.is_friend)),
                                                             None2unknown(sex_verify(member.sex)),
                                                             None2unknown(member.province),None2unknown(member.city),
                                                             None2unknown(signature_verify(member.signature)),
                                                             '![](./avatar/' + member.name + '.jpg' + ')'))
        data.write(self.group.members.stats_text())
        data.close()

    def graph(self):
        path = "./data/group/" + self.group.name
        ensure_dir(path)
        ensure_dir(path+'/Graph')
        if len(self.stranges)==0:
            self.statistics()
        x=['friends','strangers']
        y=[len(self.friends),len(self.stranges)]
        pie = pye.Pie("Relationship", 'Relationship', width=1400, height=800)
        pie.add("Relationship", x, y, is_label_show=True)
        pie.render(path=path+"/Graph/Relationship.html")

    def analysis(self):
        Dir_init()
        self.statistics()
        self.write_data()
        self.graph()
        
    def check(self,msg):
        try:
            for group in self.bot.groups():
                if group.name in msg.text:
                    msg.reply("name:{}\nowner:{}\nmembers:{}\nmembers number:{}\n".format(
                        group.name,group.owner,group.members,str(len(group.members))))
        except Exception as e:
            print(e)
