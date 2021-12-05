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



def game1(b):
   x = random.randrange(1, 101)

   def back(b,c):
      c.withdraw()
      b.deiconify()

   def done(c):
      try:
         
         no=int(e1.get())
         if(no >=1 and no <=100):
             
            y=x
            
            
            if y < no:
                  l1 = Label(root1, text="The secret number is less than picked number", fg="gold", bg="black", font=("Lucida console", 15), width=60,height=1)
                  l1.place(x=400,y=300)
                             
                             
            elif y > no:
                  l1 = Label(root1, text="The secret number is greater than picked number", fg="gold", bg="black", font=("Lucida console", 15), width=60,height=1)
                  l1.place(x=400,y=300)

                             
            elif y == no:
                  l1 = Label(root1, text="You're genius! You cracked the number:D", fg="gold", bg="black", font=("Lucida console", 15), width=60,height=1)
                  l1.place(x=400,y=300)
                  l2 = Label(root1, text="------------------", fg="gold", bg="black", font=("Lucida console", 15), width=60,height=1)
                  l2.place(x=400,y=350)

                  

               
      except ValueError:
         mbox.showerror("Error", "No cheating!!")
         

   b.withdraw()
   root1 = Tk()
   root1.title("Game of trials")
   root1.configure(bg="black")
   root1.state('zoomed')

   f = Frame(root1, bg="black", borderwidth=20, relief=SUNKEN)
   f.pack()

   l = Label(f, text="Game of trials", fg="maroon", bg="white", font=("Lucida console", 30), width=60,height=2)
   l.pack()

   l1 = Label(root1, text="Crack the number;)", fg="gold", bg="black", font=("Lucida console", 15), width=60,height=1)
   l1.place(x=400,y=300)

   l2 = Label(root1, text="Pick a number between 1 and 100", fg="gold", bg="black", font=("Lucida console", 15), width=60,height=1)
   l2.place(x=400,y=350)

   e1 = Entry(root1, font=("ComicSan 10 bold", 20), width=5)
   e1.place(x=720, y=400)

   b1 = Button(root1, text="DONE", bg="green", fg="Honeydew2",width=10, overrelief=SUNKEN, font=("Calibri",15),borderwidth=2,command=partial(done,root1))
   b1.place(x=800, y=450)

   b2 = Button(root1, text="back", bg="peachpuff", fg="black",width=10, overrelief=SUNKEN, font=("Calibri",15),borderwidth=2,command=partial(back,b,root1))
   b2.place(x=700, y=550)

   root1.mainloop()
