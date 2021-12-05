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


def game2(b):

   def save(d):
      image=ImageGrab.grab(bbox=(300,0,1700,850))
      image.save("Paint.png")
      mbox.showinfo("Saved", "Painting saved in your PC")
      game2(b)
      

   def back(b,d):
      d.withdraw()
      b.deiconify()
   
   def paint(event):
      
      aa="blue"
      x1,y1=(event.x-1),(event.y-1)
      x2,y2=(event.x+1),(event.y+1)
      w.create_oval(x1,y1,x2,y2,fill=aa)


   b.withdraw()   
   root3 = Tk()
   root3.title("Game of trials")
   root3.configure(bg="black")
   root3.state('zoomed')

   f = Frame(root3, bg="white", borderwidth=20, relief=SUNKEN)
   f.pack()

   l = Label(f, text="Paint", fg="maroon", bg="white", font=("Lucida console", 30), width=60,height=2)
   l.pack()
      
   c_width=500
   c_height=500
   w=Canvas(root3,width=c_width,height=c_height,bg="peachpuff")
   w.pack(expand=YES,fill=BOTH)
   w.bind("<B1-Motion>",paint)

   b1 = Button(root3, text="back", bg="maroon", fg="black",width=10, overrelief=SUNKEN, font=("Calibri",15),borderwidth=2,command=partial(back,b,root3))
   b1.place(x=600, y=750)

   b2 = Button(root3, text="save", bg="maroon", fg="black",width=10, overrelief=SUNKEN, font=("Calibri",15),borderwidth=2,command=partial(save,root3))
   b2.place(x=800, y=750)

   root3.mainloop()

