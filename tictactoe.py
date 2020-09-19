from graphics import *
winning_condittions = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
x = 1
y = 1
x_list = []
y_list = []
flag = True
won = False
win = GraphWin("MY window", 1000, 1000)
win.setBackground(color_rgb(0, 0, 0))
pt1 = Point(250, 250)
pt2 = Point(500, 250)
pt3 = Point(750, 250)
pt4 = Point(250, 500)
pt5 = Point(500, 500)
pt6 = Point(750, 500)
pt7 = Point(250, 750)
pt8 = Point(500, 750)
pt9 = Point(750, 750)
cir1 = Circle(pt1, 50)
cir1.setFill(color_rgb(100,0,50))

cir2 = Circle(pt2, 50)
cir2.setFill(color_rgb(100,0,50))
cir3 = Circle(pt3, 50)
cir3.setFill(color_rgb(100,0,50))

cir4 = Circle(pt4, 50)
cir4.setFill(color_rgb(100,0,50))

cir5 = Circle(pt5, 50)
cir5.setFill(color_rgb(100,0,50))

cir6 = Circle(pt6, 50)
cir6.setFill(color_rgb(100,0,50))

cir7 = Circle(pt7, 50)
cir7.setFill(color_rgb(100,0,50))

cir8 = Circle(pt8, 50)
cir8.setFill(color_rgb(100,0,50))

cir9 = Circle(pt9, 50)
cir9.setFill(color_rgb(100,0,50))

cir1_2 = Circle(pt1, 50)
cir1_2.setFill(color_rgb(0,100,50))

cir2_2 = Circle(pt2, 50)
cir2_2.setFill(color_rgb(0,100,50))

cir3_2 = Circle(pt3, 50)
cir3_2.setFill(color_rgb(0,100,50))

cir4_2 = Circle(pt4, 50)
cir4_2.setFill(color_rgb(0,100,50))

cir5_2 = Circle(pt5, 50)
cir5_2.setFill(color_rgb(0,100,50))

cir6_2 = Circle(pt6, 50)
cir6_2.setFill(color_rgb(0,110,50))

cir7_2 = Circle(pt7, 50)
cir7_2.setFill(color_rgb(0,100,50))

cir8_2 = Circle(pt8, 50)
cir8_2.setFill(color_rgb(0,100,50))

cir9_2 = Circle(pt9, 50)
cir9_2.setFill(color_rgb(0,100,50))

while(x != 0 and not won):
    if(flag):
        flag = False
        x = int(input("enter num P1: "))
        x_list.append(x)
        if (x == 1):
            cir1.draw(win)
        elif(x == 2):
            cir2.draw(win)
        elif(x == 3):
            cir3.draw(win)
        elif(x == 4):
            cir4.draw(win)
        elif(x == 5):
            cir5.draw(win)
        elif(x == 6):
            cir6.draw(win)
        elif(x == 7):
            cir7.draw(win)
        elif(x == 8):
            cir8.draw(win)
        elif(x == 9):
            cir9.draw(win)
        if(x_list in winning_condittions):
            won = True
            print("Player 1 has won\n")
            win.getMouse()
            win.close()
    elif(not flag):
        y = int(input("enter num P2: "))
        y_list.append(y)
        flag = True
        if (y == 1):
            cir1_2.draw(win)
        elif (y == 2):
            cir2_2.draw(win)
        elif (y == 3):
            cir3_2.draw(win)
        elif (y == 4):
            cir4_2.draw(win)
        elif (y == 5):
            cir5_2.draw(win)
        elif (y == 6):
            cir6_2.draw(win)
        elif (y == 7):
            cir7_2.draw(win)
        elif (y == 8):
            cir8_2.draw(win)
        elif (y == 9):
            cir9_2.draw(win)
        if(y_list in winning_condittions):
            won = True
            print("player 2 has won")
            win.getMouse()
            win.close()

win.getMouse()
win.close()
