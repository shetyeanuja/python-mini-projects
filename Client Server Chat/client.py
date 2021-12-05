#client
import os
import tkinter as tk
import sqlite3
import random
from tkinter import ttk
from tkinter import messagebox as mbox
import PIL
from PIL import Image
from tkinter import *
from PIL import Image, ImageTk
from PIL import ImageGrab
import socket
#from gtts import gTTS 
#import pyttsx3 
from functools import partial
from datetime import datetime
from datetime import date
import time
cu = datetime.now()


def start():

     def end(a):
          a.destroy()

     def receive(a):
          host='localhost'
          port=9000
          s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
          s.bind((host,port))
          s.listen(1)
          c,addr=s.accept()
          mess1=c.recv(1024)
          mess1=mess1.decode()
          e0.insert(0,mess1)
          c.close()

          
     def undo(a):
          e1.delete(0,END)

     def send(a):
          host='localhost'
          port=8500
          s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
          s.connect((host,port))
          mess1=e1.get()
          s.send(mess1.encode())
          e1.delete(0,END)
          e0.delete(0,END)
          s.close()

          receive(a)


     
     root1 = Tk()
     root1.title("Chat Client")
     root1.configure(bg="peachpuff")
     root1.geometry('800x700')
     
     f = Frame(root1, bg="peachpuff", borderwidth=20, relief=SUNKEN)
     f.pack()

     l = Label(f, text="Client", fg="maroon", bg="white", font=("Lucida console", 30), width=60,height=2)
     l.pack()

     pic = PIL.Image.open("chat.jpg").convert("RGB")
     pic = pic.resize((100,100))
     pic1 = ImageTk.PhotoImage(pic)
     img_label1 = Label(root1, image=pic1)
     img_label1.image=pic1
     img_label1.place(x=330,y=240)
     img_label1.pack_propagate(0)

     lc = Label(root1, text="waiting for server to accept your request..", fg="maroon", bg="peachpuff", font=("Lucida console", 15))
     lc.place(x=170,y=150)
     
     lc = Label(root1, text="Gray button indicates waiting for server..", fg="maroon", bg="peachpuff", font=("Lucida console", 15))
     lc.place(x=170,y=200)
     
     l1 = Label(root1, text="From server:", fg="maroon", bg="peachpuff", font=("Lucida console", 15))
     l1.place(x=120,y=400)

     l2 = Label(root1, text="To server:", fg="maroon", bg="peachpuff", font=("Lucida console", 15))
     l2.place(x=120,y=500)

     e0 = Entry(root1, font=("Candara", 18), width=25)
     e0.place(x=300, y=400)
                
     e1 = Entry(root1, font=("Candara", 18), width=25)
     e1.insert(0,"Start chat..")
     e1.place(x=300, y=500)

     b1 = Button(root1, text=">>", bg="green", fg="black",width=3, overrelief=SUNKEN, font=("Calibri",15),borderwidth=2,command=partial(send,root1))
     b1.place(x=650, y=500)

     b2 = Button(root1, text="Undo", bg="maroon", fg="black",width=7, overrelief=SUNKEN, font=("Calibri",15),borderwidth=2,command=partial(undo,root1))
     b2.place(x=480, y=570)

     b3 = Button(root1, text="End chat", bg="darkkhaki", fg="black",width=10, overrelief=SUNKEN, font=("Calibri",15),command=partial(end,root1))
     b3.place(x=430, y=650)


     root1.mainloop()


start()


    

