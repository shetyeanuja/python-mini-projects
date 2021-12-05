import os
from tkinter import *
import tkinter as tk
import random
from tkinter import ttk
from PIL import Image, ImageTk
from PIL import ImageGrab
from functools import partial
from tkinter import messagebox as mbox
import winsound
from game1 import *
from game2 import *
from game3 import *


#a=root,b=root2,c=root1,d=root3,e=root4


def aglaPage(a):

   def song():
      return winsound.PlaySound("gamesong.wav",winsound.SND_LOOP | winsound.SND_ASYNC)
      
   
   a.withdraw()
   
   root2 = Tk()
   root2.title("Game")
   root2.configure(bg="black")
   root2.state('zoomed')

   f = Frame(root2, bg="black", borderwidth=20, relief=SUNKEN)
   f.pack()

   l = Label(f, text="Games", fg="maroon", bg="white", font=("Lucida console", 30), width=60,height=2)
   l.pack()
   
   b1 = Button(root2, text="Guess Number", bg="green", fg="Honeydew2",width=15, overrelief=SUNKEN, font=("Calibri",15),borderwidth=2,command=partial(game1,root2))
   b1.place(x=500, y=450)

   b2 = Button(root2, text="Paint", bg="green", fg="Honeydew2",width=15, overrelief=SUNKEN, font=("Calibri",15),borderwidth=2,command=partial(game2,root2))
   b2.place(x=700, y=450)

   b3 = Button(root2, text="stone,ppr,scissor", bg="green", fg="Honeydew2",width=15, overrelief=SUNKEN, font=("Calibri",15),borderwidth=2,command=partial(game3,root2))
   b3.place(x=900, y=450)


   song()
   

   root2.mainloop()

   
   
def game():
   
   root = Tk()
   root.title("Game")
   root.configure(bg="black")
   root.state('zoomed')

   f = Frame(root, bg="black", borderwidth=20, relief=SUNKEN)
   f.pack()

   l = Label(f, text="Games", fg="maroon", bg="white", font=("Lucida console", 30), width=60,height=2)
   l.pack()
    
   b = Button(root, text="Agla page!", fg="white",font=("Lucida console", 20), bg="Goldenrod", width=15, relief=RAISED, overrelief=SUNKEN, height=5,command=partial(aglaPage,root))
   b.place(x=650,y=300)

   root.mainloop()


game()

