import random

words = ['苟立国家生死以，岂因祸福避趋之', '闷声发大财', 'too young, too simple, sometimes naive',
         '西方哪几个国家我没去过', '美国那个华莱士，比你们高不到哪里去了，我跟他谈笑风生',
         '还是要提高自己的知识水平', '很惭愧，就做了一点微小的贡献，谢谢大家', '你们给我搞的这个，excited！',
         '一个人的成功，当然要靠自我奋斗，但是也要考虑历史进程', '中央已经钦定了，就让你当总书记', '无可奉告',
         '你问我兹瓷不兹瓷，我很明确的跟你讲，我是兹瓷的']


def hath():
    index = random.randint(0, len(words)-1)
    return words[index]
