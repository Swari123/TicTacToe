from tkinter import *

class MenuScreen:
    def __init__(self, master):
        self.master = master
        self.master.title("Nought's and Crosses")
        self.MainLabel = Label(master, text = "Nought's and Crosses!!")
        self.MainLabel.pack(side = TOP)
        self.PlayButton = Button(root, text = "New Game", command = self.CreateGame)
        self.PlayButton.pack()
    def CreateGame(self):
        self.master.destroy()
root = Tk()
main = MenuScreen(root)
