import os



def Yolo_img(msg):
    print(os.getcwd())
    if 'yolo' not in os.getcwd():
        os.chdir('./analysis/CV/yolo')
    msg.get_file(save_path="data/temp.jpg")
    msg.reply("Begin to detect object\nplease wait...")
    if os.system("./darknet detect cfg/yolov3.cfg yolov3.weights data/temp.jpg")==0:
        msg.reply_image("predictions.jpg")
    os.chdir('../../..')


def turn_hero(msg,hero):
    #msg.get_file(save_path="Hero/temp.jpg")
    print(hero)
    if os.system("python3 demo_texture.py -i " + hero
                 + " -r Hero/temp.jpg -o Hero/hero.jpg ") == 0:
        msg.reply_image("Hero/hero.jpg")
