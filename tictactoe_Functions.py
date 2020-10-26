from graphics import *


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
cir1.setFill(color_rgb(100, 0, 50))

cir2 = Circle(pt2, 50)
cir2.setFill(color_rgb(100, 0, 50))
cir3 = Circle(pt3, 50)
cir3.setFill(color_rgb(100, 0, 50))

cir4 = Circle(pt4, 50)
cir4.setFill(color_rgb(100, 0, 50))

cir5 = Circle(pt5, 50)
cir5.setFill(color_rgb(100, 0, 50))

cir6 = Circle(pt6, 50)
cir6.setFill(color_rgb(100, 0, 50))

cir7 = Circle(pt7, 50)
cir7.setFill(color_rgb(100, 0, 50))

cir8 = Circle(pt8, 50)
cir8.setFill(color_rgb(100, 0, 50))

cir9 = Circle(pt9, 50)
cir9.setFill(color_rgb(100, 0, 50))

cir1_2 = Circle(pt1, 50)
cir1_2.setFill(color_rgb(0, 100, 50))

cir2_2 = Circle(pt2, 50)
cir2_2.setFill(color_rgb(0, 100, 50))

cir3_2 = Circle(pt3, 50)
cir3_2.setFill(color_rgb(0, 100, 50))

cir4_2 = Circle(pt4, 50)
cir4_2.setFill(color_rgb(0, 100, 50))

cir5_2 = Circle(pt5, 50)
cir5_2.setFill(color_rgb(0, 100, 50))

cir6_2 = Circle(pt6, 50)
cir6_2.setFill(color_rgb(0, 110, 50))

cir7_2 = Circle(pt7, 50)
cir7_2.setFill(color_rgb(0, 100, 50))

cir8_2 = Circle(pt8, 50)
cir8_2.setFill(color_rgb(0, 100, 50))

cir9_2 = Circle(pt9, 50)
cir9_2.setFill(color_rgb(0, 100, 50))



def check_win(inputs, flag):
    winning_condittions = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9],
                           [3, 5, 7]]
    inputs.sort()

    board = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]

    for i in inputs:
        if (flag):
            board[i] = 1
        else:
            board[i] = 0

    if (board[1] + board[2] + board[3] == 3):
        print("Player 1 won!")
        exit()
    elif (board[4] + board[5] + board[6] == 3):
        print("Player 1 won!")
        exit()
    elif (board[7] + board[8] + board[9] == 3):
        print("Player 1 won!")
        exit()
    elif (board[1] + board[5] + board[9] == 3):
        print("Player 1 won!")
        exit()
    elif (board[3] + board[5] + board[7] == 3):
        print("Player 1 won!")
        exit()
    elif (board[1] + board[4] + board[7] == 3):
        print("Player 1 won!")
        exit()
    elif (board[2] + board[5] + board[8] == 3):
        print("Player 1 won!")
        exit()
    elif (board[3] + board[6] + board[9] == 3):
        print("Player 1 won!")
        exit()
    elif (board[1] + board[2] + board[3] == 0):
        print("player 2 won!")
        exit()
    elif (board[4] + board[5] + board[6] == 0):
        print("Player 2 won!")
        exit()
    elif (board[7] + board[8] + board[9] == 0):
        print("Player 2 won!")
        exit()
    elif (board[1] + board[5] + board[9] == 0):
        print("Player 2 won!")
        exit()
    elif (board[3] + board[5] + board[7] == 0):
        print("Player 2 won!")
        exit()
    elif (board[1] + board[4] + board[7] == 0):
        print("Player 1 won!")
        exit()
    elif (board[2] + board[5] + board[8] == 0):
        print("Player 1 won!")
        exit()
    elif (board[3] + board[6] + board[9] == 0):
        print("Player 1 won!")
        exit()


def getPlay(num, x_list, y_list):
    print("Player #" + str(num) + " Please chose a number: ")
    move = input()
    while (True):
        if (int(move) in x_list or int(move) in y_list):
            print("Spot already taken, try again")
            move = input()
        else:
            return (move)


def draw(x, flag):
    if (flag):
        if (x == 1):
            cir1.draw(win)
        elif (x == 2):
            cir2.draw(win)
        elif (x == 3):
            cir3.draw(win)
        elif (x == 4):
            cir4.draw(win)
        elif (x == 5):
            cir5.draw(win)
        elif (x == 6):
            cir6.draw(win)
        elif (x == 7):
            cir7.draw(win)
        elif (x == 8):
            cir8.draw(win)
        elif (x == 9):
            cir9.draw(win)

    elif (not flag):
        if (x == 1):
            cir1_2.draw(win)
        elif (x == 2):
            cir2_2.draw(win)
        elif (x == 3):
            cir3_2.draw(win)
        elif (x == 4):
            cir4_2.draw(win)
        elif (x == 5):
            cir5_2.draw(win)
        elif (x == 6):
            cir6_2.draw(win)
        elif (x == 7):
            cir7_2.draw(win)
        elif (x == 8):
            cir8_2.draw(win)
        elif (x == 9):
            cir9_2.draw(win)


def main():
    # game variables
    x = 1
    y = 1
    x_list = []
    y_list = []
    flag = False

    won = False

    while (x != 0 and not won):
        play = int(getPlay('1' if not flag else '2', x_list, y_list))
        if (not flag):
            draw(play, flag)
            x_list.append(play)
            flag = True
            check_win(x_list, flag)
        else:
            draw(play, flag)
            y_list.append(play)
            flag = False
            check_win(y_list, flag)

        if (len(x_list) + len(y_list) >= 9):
            print("Game over")
            exit()

    win.getMouse()
    win.close()


main()




