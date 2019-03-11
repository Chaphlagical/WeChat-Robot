import cv2
import numpy as np
import random

num_dict = {1: "./img/1.png", 2: "./img/2.png", 3: "./img/3.png",
            4: "./img/4.png", 5: "./img/5.png", 6: "./img/6.png",
            7: "./img/7.png", 8: "./img/8.png", 9: "./img/9.png"}

board = "./img/board.png" #(793,793,3)


def get_cord(x,y):
    x_=12+x*87
    y_=12+y*87
    return [x_,y_]


def set_num(x, y, board, num):
    num_img = cv2.imread(num_dict[num])
    start=get_cord(x,y)
    for x in range(num_img.shape[0]):
        for y in range(num_img.shape[1]):
            board[start[0]+x][start[1]+y]=num_img[x][y]
    return board

class sudu:
    def __init__(self,level):
        level=0
    
    def Create_full(self):
        sudoku = np.zeros((9, 9))
        unit=np.zeros((3, 3))
        for i in range(3):
            for j in range(3):
                num = random.randint(1, 9)
                while unit[i][j] != 0 or num in unit:
                    num = random.randint(1, 9)
                unit[i][j] = num
        sudoku[3:6, 3:6] = unit
        row=list(unit)
        col=list(unit[:, i].reshape(3, 1) for i in range(3))
        index=random.randint(1, 2)
        sudoku[5:6, 6:9] = sudoku[3:4, 0:3] = row[index]
        sudoku[3:4, 6:9] = sudoku[4:5, 0:3] = row[0 if index == 2 else 2]
        sudoku[4:5, 6:9] = sudoku[5:6, 0:3] = row[1 if index == 2 else 0]
        index = random.randint(1, 2)
        sudoku[0:3, 3:4] = sudoku[6:9, 4:5] = col[index]
        sudoku[0:3, 4:5] = sudoku[6:9, 5:6] = col[0 if index == 2 else 2]
        sudoku[0:3, 5:6] = sudoku[6:9, 3:4] = col[1 if index == 2 else 0]
        print(sudoku)
    
    def Create_struct(self):
        suduku=np.zeros((9,9))
        count=0
        while True:
            x=random.randint(0,8)
            y=random.randint(0,8)
            while suduku[x][y]!=0:
                x = random.randint(0, 8)
                y = random.randint(0, 8)
            suduku[x][y]=10
            count+=1
            if count==30:
                print(suduku)
                return
    
    def Solute(self):
        pass
    
    def Send(self):
        pass
    
    def Judge(self):
        pass
    
s=sudu(0)
s.Create_struct()