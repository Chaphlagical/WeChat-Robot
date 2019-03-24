from scripts.hath import *
from scripts.function.cmd import *
from scripts.function.turing import *
from scripts.function.analysis import *
from scripts.function.yolo import *
from scripts.function.hero import *
from scripts.function.movie import *

# all the params look like: var=(bot, msg, me, cmd, turing_robot, yolo)

        
func_dict ={'cmd on': cmd_on, 'cmd list': cmd_list, 'cmd kill': cmd_kill,
            'turing on': turing_on, 'turing list': turing_list, 'turing kill': turing_kill,
            'hath': hath(), '蛤': hath(), '膜蛤': hath(),
            'analysis friends': analysis_friends, 'analysis all groups': analysis_all_group,
            'analysis group': analysis_group,'check friend': check_friend, 'check group': check_group,
            'yolo on': yolo_on, 'yolo off': yolo_off, 'yolo kill': yolo_kill, 'yolo list': yolo_list,
            'hero on': hero_on, 'hero list': hero_list, 'movie': get_movie_url
            }

