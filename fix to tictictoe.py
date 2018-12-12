from tkinter import *
root = Tk()
root.title("Noughts and Crosses")
turn = "X"
frame1 = Frame(root, width = 100, height = 100)
frame2 = Frame(root, width = 100, height = 100)
frame3 = Frame(root, width = 100, height = 100)
frame4 = Frame(root, width = 100, height = 100)
frame5 = Frame(root, width = 100, height = 100)
frame6 = Frame(root, width = 100, height = 100)
frame7 = Frame(root, width = 100, height = 100)
frame8 = Frame(root, width = 100, height = 100)
frame9 = Frame(root, width = 100, height = 100)
frame1.grid(row = 0, column = 0)
frame2.grid(row = 0, column = 1)
frame3.grid(row = 0, column = 2)
frame4.grid(row = 1, column = 0)
frame5.grid(row = 1, column = 1)
frame6.grid(row = 1, column = 2)
frame7.grid(row = 2, column = 0)
frame8.grid(row = 2, column = 1)
frame9.grid(row = 2, column = 2)
box_1_label = Label(frame1, text = turn)
statusBarframe = Frame(root)
statusBarframe.grid(row = 3)


def box_1(event):
    #print("X")
    global turn
    box_1_label = Label(frame1, text = turn)
    box_1_label.pack()
   
    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"
    print(turn)
    status = Label(statusBarframe, text = turn+"'s turn", bd = 1, relief = SUNKEN)
    status.pack(side = LEFT, fill = X)
   
def box_2(event):
    #print("X")
    global turn
    box_2_label = Label(frame2, text = turn)
    box_2_label.pack()
    
    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"
    
    print(turn)
    status = Label(statusBarframe, text = turn+"'s turn", bd = 1, relief = SUNKEN)
    status.pack(side = LEFT, fill = X)
def box_3(event):
    #print("X")
    global turn
    box_3_label = Label(frame3, text = turn)
    box_3_label.pack()
    
    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"
    
    print(turn)
    status = Label(statusBarframe, text = turn+"'s turn", bd = 1, relief = SUNKEN)
    status.pack(side = LEFT, fill = X)
def box_4(event):
    #print("X")
    global turn
    box_4_label = Label(frame4, text = turn)
    box_4_label.pack()
    
    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"
    
    print(turn)
    status = Label(statusBarframe, text = turn+"'s turn", bd = 1, relief = SUNKEN)
    status.pack(side = LEFT, fill = X)
def box_5(event):
    #print("X")
    global turn
    box_5_label = Label(frame5, text = turn)
    box_5_label.pack()
    
    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"
    
    print(turn)
    status = Label(statusBarframe, text = turn+"'s turn", bd = 1, relief = SUNKEN)
    status.pack(side = LEFT, fill = X)
def box_6(event):
    #print("X")
    global turn
    box_6_label = Label(frame6, text = turn)
    box_6_label.pack()
    
    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"
    
    print(turn)
    status = Label(statusBarframe, text = turn+"'s turn", bd = 1, relief = SUNKEN)
    status.pack(side = LEFT, fill = X)
def box_7(event):
    #print("X")
    global turn
    box_7_label = Label(frame7, text = turn)
    box_7_label.pack()
    
    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"
    print(turn)
    status = Label(statusBarframe, text = turn+"'s turn", bd = 1, relief = SUNKEN)
    status.pack(side = LEFT, fill = X)
def box_8(event):
    #print("X")
    global turn
    box_8_label = Label(frame8, text = turn)
    box_8_label.pack()
    
    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"
    print(turn)
    status = Label(statusBarframe, text = turn+"'s turn", bd = 1, relief = SUNKEN)
    status.pack(side = LEFT, fill = X)
def box_9(event):
    #print("X")
    global turn
    box_9_label = Label(frame9, text = turn)
    box_9_label.pack()
    
    if turn == "X":
        turn = "O"
    elif turn == "O":
        turn = "X"
    print(turn)
    status = Label(statusBarframe, text = turn+"'s turn", bd = 1, relief = SUNKEN)
    status.pack(side = LEFT, fill = X)
frame1.bind("<Button-1>", box_1)
#i+=1
frame2.bind("<Button-1>", box_2)
#i+=1
frame3.bind("<Button-1>", box_3)
#i+=1
frame4.bind("<Button-1>", box_4)
#i+=1
frame5.bind("<Button-1>", box_5)
#i+=1
frame6.bind("<Button-1>", box_6)
#i+=1
frame7.bind("<Button-1>", box_7)
#i+=1
frame8.bind("<Button-1>", box_8)
#i+=1
frame9.bind("<Button-1>", box_9)
#i+=1

    
root.mainloop()
        
   
