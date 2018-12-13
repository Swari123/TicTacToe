from tkinter import *
import tkinter.messagebox
from MenuScreen import *
class TicTac:
    turn = "X"
    occupationBox = {1: "w ", 2: "e ", 3: "r ", 4: "t ", 5: "y ", 6: "u ", 7: "i ", 8: "p ", 9: " a"}
    def __init__(self, master):
        self.master = master
        master.title("Nought's and crosses")
        self.frame1 = Frame(root, width = 100, height = 100)
        self.frame2 = Frame(root, width = 100, height = 100)
        self.frame3 = Frame(root, width = 100, height = 100)
        self.frame4 = Frame(root, width = 100, height = 100)
        self.frame5 = Frame(root, width = 100, height = 100)
        self.frame6 = Frame(root, width = 100, height = 100)
        self.frame7 = Frame(root, width = 100, height = 100)
        self.frame8 = Frame(root, width = 100, height = 100)
        self.frame9 = Frame(root, width = 100, height = 100)
        self.frame1.grid(row = 0, column = 0)
        self.frame2.grid(row = 0, column = 1)
        self.frame3.grid(row = 0, column = 2)
        self.frame4.grid(row = 1, column = 0)
        self.frame5.grid(row = 1, column = 1)
        self.frame6.grid(row = 1, column = 2)
        self.frame7.grid(row = 2, column = 0)
        self.frame8.grid(row = 2, column = 1)
        self.frame9.grid(row = 2, column = 2)
        self.menu = Menu(master)
        self.master.config(menu = self.menu)
        self.HelpMenu = Menu(self.menu)
        self.menu.add_cascade(label = "HELP", menu = self.HelpMenu)
        self.HelpMenu.add_command(label = "Rules", command = self.show_Rules)
        self.frame1.bind("<Button-1>", self.box_1)
#i+=1
        self.frame2.bind("<Button-1>", self.box_2)
#i+=1
        self.frame3.bind("<Button-1>", self.box_3)
#i+=1
        self.frame4.bind("<Button-1>", self.box_4)
#i+=1
        self.frame5.bind("<Button-1>", self.box_5)
#i+=1
        self.frame6.bind("<Button-1>", self.box_6)
#i+=1
        self.frame7.bind("<Button-1>", self.box_7)
#i+=1
        self.frame8.bind("<Button-1>", self.box_8)
#i+=1
        self.frame9.bind("<Button-1>", self.box_9)
        
    def show_Rules(self):
        tkinter.messagebox.showinfo("Rules", "X starts first then keeps alternating, first to get three markers in a row wins!!")
    def box_1(self, event):
        #print("X")
            
            self.box_1_label = Label(self.frame1, text = self.turn)
            self.box_1_label.pack()
            self.occupationBox[1] = self.turn
    
   
            if self.turn == "X":
                self.turn = "O"
            elif self.turn == "O":
                self.turn = "X"
            print(self.turn)
            if self.occupationBox[1] == self.occupationBox[2] and self.occupationBox[2] == self.occupationBox[3]:
                tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[1] + " has won")
            elif self.occupationBox[4] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[6]:
                tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[4] + " has won")
            elif self.occupationBox[7] == self.occupationBox[8] and self.occupationBox[8] == self.occupationBox[9]:
                tkinter.messagebox.showinfo("Nought&Crosses", occupationBox[8] + " has won")
            elif self.occupationBox[3] == self.occupationBox[6] and self.occupationBox[6] == self.occupationBox[9]:
                tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[6] + " has won")
            elif self.occupationBox[2] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[8]:
                tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
            elif self.occupationBox[1] == self.occupationBox[4] and self.occupationBox[4] == self.occupationBox[7]:
                tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[4] + " has won")
            elif self.occupationBox[1] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[9]:
                tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
            elif self.occupationBox[3] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[7]:
                tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
   
    #status = Label(statusBarframe, text = turn+"'s turn", bd = 1, relief = SUNKEN)
    
    #status.pack(side = LEFT, fill = X)
    def box_2(self, event):
        self.box_2_label = Label(self.frame2, text = self.turn)
        self.box_2_label.pack()
        self.occupationBox[2] = self.turn
        if self.turn == "X":
            self.turn = "O"
        elif self.turn == "O":
            self.turn = "X"
    
        print(self.turn)
 #   status = Label(statusBarframe, text = turn+"'s turn", bd = 1, relief = SUNKEN)
    
 #   status.pack(side = LEFT, fill = X)
          
        if self.occupationBox[1] == self.occupationBox[2] and self.occupationBox[2] == self.occupationBox[3]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[1] + " has won")
        elif self.occupationBox[4] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[6]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[4] + " has won")
        elif self.occupationBox[7] == self.occupationBox[8] and self.occupationBox[8] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", occupationBox[8] + " has won")
        elif self.occupationBox[3] == self.occupationBox[6] and self.occupationBox[6] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[6] + " has won")
        elif self.occupationBox[2] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[8]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
        elif self.occupationBox[1] == self.occupationBox[4] and self.occupationBox[4] == self.occupationBox[7]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[4] + " has won")
        elif self.occupationBox[1] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
        elif self.occupationBox[3] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[7]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
    def box_3(self, event):
        self.box_3_label = Label(self.frame3, text = self.turn)
        self.box_3_label.pack()
        self.occupationBox[3] = self.turn
        if self.turn == "X":
            self.turn = "O"
        elif self.turn == "O":
            self.turn = "X"
    
        print(self.turn)
        if self.occupationBox[1] == self.occupationBox[2] and self.occupationBox[2] == self.occupationBox[3]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[1] + " has won")
        elif self.occupationBox[4] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[6]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[4] + " has won")
        elif self.occupationBox[7] == self.occupationBox[8] and self.occupationBox[8] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", occupationBox[8] + " has won")
        elif self.occupationBox[3] == self.occupationBox[6] and self.occupationBox[6] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[6] + " has won")
        elif self.occupationBox[2] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[8]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
        elif self.occupationBox[1] == self.occupationBox[4] and self.occupationBox[4] == self.occupationBox[7]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[4] + " has won")
        elif self.occupationBox[1] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
        elif self.occupationBox[3] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[7]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
    def box_4(self, event):
        self.box_4_label = Label(self.frame4, text = self.turn)
        self.box_4_label.pack()
        self.occupationBox[4] = self.turn
        if self.turn == "X":
            self.turn = "O"
        elif self.turn == "O":
            self.turn = "X"
    
        print(self.turn)
        if self.occupationBox[1] == self.occupationBox[2] and self.occupationBox[2] == self.occupationBox[3]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[1] + " has won")
        elif self.occupationBox[4] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[6]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[4] + " has won")
        elif self.occupationBox[7] == self.occupationBox[8] and self.occupationBox[8] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", occupationBox[8] + " has won")
        elif self.occupationBox[3] == self.occupationBox[6] and self.occupationBox[6] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[6] + " has won")
        elif self.occupationBox[2] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[8]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
        elif self.occupationBox[1] == self.occupationBox[4] and self.occupationBox[4] == self.occupationBox[7]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[4] + " has won")
        elif self.occupationBox[1] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
        elif self.occupationBox[3] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[7]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
    def box_5(self, event):
        self.box_5_label = Label(self.frame5, text = self.turn)
        self.box_5_label.pack()
        self.occupationBox[5] = self.turn
        if self.turn == "X":
            self.turn = "O"
        elif self.turn == "O":
            self.turn = "X"
        print(self.turn)
        if self.occupationBox[1] == self.occupationBox[2] and self.occupationBox[2] == self.occupationBox[3]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[1] + " has won")
        elif self.occupationBox[4] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[6]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[4] + " has won")
        elif self.occupationBox[7] == self.occupationBox[8] and self.occupationBox[8] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", occupationBox[8] + " has won")
        elif self.occupationBox[3] == self.occupationBox[6] and self.occupationBox[6] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[6] + " has won")
        elif self.occupationBox[2] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[8]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
        elif self.occupationBox[1] == self.occupationBox[4] and self.occupationBox[4] == self.occupationBox[7]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[4] + " has won")
        elif self.occupationBox[1] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
        elif self.occupationBox[3] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[7]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
    def box_6(self, event):
        self.box_6_label = Label(self.frame6, text = self.turn)
        self.box_6_label.pack()
        self.occupationBox[6] = self.turn
        if self.turn == "X":
            self.turn = "O"
        elif self.turn == "O":
            self.turn = "X"
        
        print(self.turn)
        if self.occupationBox[1] == self.occupationBox[2] and self.occupationBox[2] == self.occupationBox[3]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[1] + " has won")
        elif self.occupationBox[4] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[6]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[4] + " has won")
        elif self.occupationBox[7] == self.occupationBox[8] and self.occupationBox[8] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", occupationBox[8] + " has won")
        elif self.occupationBox[3] == self.occupationBox[6] and self.occupationBox[6] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[6] + " has won")
        elif self.occupationBox[2] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[8]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
        elif self.occupationBox[1] == self.occupationBox[4] and self.occupationBox[4] == self.occupationBox[7]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[4] + " has won")
        elif self.occupationBox[1] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
        elif self.occupationBox[3] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[7]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
    def box_7(self, event):
        self.box_7_label = Label(self.frame7, text = self.turn)
        self.box_7_label.pack()
        self.occupationBox[7] = self.turn
        if self.turn == "X":
            self.turn = "O"
        elif self.turn == "O":
            self.turn = "X"
        print(self.turn)
        if self.occupationBox[1] == self.occupationBox[2] and self.occupationBox[2] == self.occupationBox[3]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[1] + " has won")
        elif self.occupationBox[4] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[6]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[4] + " has won")
        elif self.occupationBox[7] == self.occupationBox[8] and self.occupationBox[8] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", occupationBox[8] + " has won")
        elif self.occupationBox[3] == self.occupationBox[6] and self.occupationBox[6] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[6] + " has won")
        elif self.occupationBox[2] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[8]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
        elif self.occupationBox[1] == self.occupationBox[4] and self.occupationBox[4] == self.occupationBox[7]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[4] + " has won")
        elif self.occupationBox[1] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
        elif self.occupationBox[3] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[7]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
    def box_8(self, event):
        self.box_8_label = Label(self.frame8, text = self.turn)
        self.box_8_label.pack()
        self.occupationBox[8] = self.turn
        if self.turn == "X":
            self.turn = "O"
        elif self.turn == "O":
            self.turn = "X"
        print(self.turn)
        if self.occupationBox[1] == self.occupationBox[2] and self.occupationBox[2] == self.occupationBox[3]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[1] + " has won")
        elif self.occupationBox[4] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[6]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[4] + " has won")
        elif self.occupationBox[7] == self.occupationBox[8] and self.occupationBox[8] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", occupationBox[8] + " has won")
        elif self.occupationBox[3] == self.occupationBox[6] and self.occupationBox[6] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[6] + " has won")
        elif self.occupationBox[2] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[8]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
        elif self.occupationBox[1] == self.occupationBox[4] and self.occupationBox[4] == self.occupationBox[7]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[4] + " has won")
        elif self.occupationBox[1] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
        elif self.occupationBox[3] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[7]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
    def box_9(self, event):
        self.box_9_label = Label(self.frame9, text = self.turn)
        self.box_9_label.pack()
        self.occupationBox[9] = self.turn
        if self.turn == "X":
            self.turn = "O"
        elif self.turn == "O":
            self.turn = "X"
        print(self.turn)
        if self.occupationBox[1] == self.occupationBox[2] and self.occupationBox[2] == self.occupationBox[3]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[1] + " has won")
        elif self.occupationBox[4] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[6]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[4] + " has won")
        elif self.occupationBox[7] == self.occupationBox[8] and self.occupationBox[8] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", occupationBox[8] + " has won")
        elif self.occupationBox[3] == self.occupationBox[6] and self.occupationBox[6] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[6] + " has won")
        elif self.occupationBox[2] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[8]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
        elif self.occupationBox[1] == self.occupationBox[4] and self.occupationBox[4] == self.occupationBox[7]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[4] + " has won")
        elif self.occupationBox[1] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[9]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
        elif self.occupationBox[3] == self.occupationBox[5] and self.occupationBox[5] == self.occupationBox[7]:
            tkinter.messagebox.showinfo("Nought&Crosses", self.occupationBox[5] + " has won")
        
        
        
        
            

root = Tk()
new_GAME = TicTac(root)
root.mainloop()
        
