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

i = 0
p_val = 0
p_myval = 0

def game3(b):

    def turn(e):
        global i
        global p_val
        global p_myval
        
        li=['stone','paper','scissor']
        my=random.choice(li)

        
        e2.delete(0,END)
        e2.insert(0,my)
        val=e1.get()
        myval=e2.get()
        
        if((val=="stone" or val=="paper" or val=="scissor") and (myval=="stone" or myval=="paper" or myval=="scissor")):
        
            if(val==myval):
                e3.delete(0,END)
                e4.delete(0,END)
                p_val = p_val + 0
                p_val1 = str(p_val)
                p_myval = p_myval + 0
                p_myval1 = str(p_myval)
                e3.insert(0,p_val1)
                e4.insert(0,p_myval1)
                
                
                        
            elif(val=='paper' and myval=='stone'):
                e3.delete(0,END)
                e4.delete(0,END)
                p_val = p_val + 1
                p_val1 = str(p_val)
                p_myval = p_myval + 0
                p_myval1 = str(p_myval)
                e3.insert(0,p_val1)
                e4.insert(0,p_myval1)
                        
            elif(val=='paper' and myval=='scissor'):
                e3.delete(0,END)
                e4.delete(0,END)
                p_val = p_val + 0
                p_val1 = str(p_val)
                p_myval = p_myval + 1
                p_myval1 = str(p_myval)
                e3.insert(0,p_val1)
                e4.insert(0,p_myval1)
                        

            elif(val=='stone' and myval=='paper'):
                e3.delete(0,END)
                e4.delete(0,END)
                p_val = p_val + 0
                p_val1 = str(p_val)
                p_myval = p_myval + 1
                p_myval1 = str(p_myval)
                e3.insert(0,p_val1)
                e4.insert(0,p_myval1)
                
                        
            elif(val=='stone' and myval=='scissor'):
                e3.delete(0,END)
                e4.delete(0,END)
                p_val = p_val + 1
                p_val1 = str(p_val)
                p_myval = p_myval + 0
                p_myval1 = str(p_myval)
                e3.insert(0,p_val1)
                e4.insert(0,p_myval1)
                        
            elif(val=='scissor' and myval=='paper'):
                e3.delete(0,END)
                e4.delete(0,END)
                p_val = p_val + 1
                p_val1 = str(p_val)
                p_myval = p_myval + 0
                p_myval1 = str(p_myval)
                e3.insert(0,p_val1)
                e4.insert(0,p_myval1)
                
            elif(val=='scissor' and myval=='stone'):
                e3.delete(0,END)
                e4.delete(0,END)
                p_val = p_val + 0
                p_val1 = str(p_val)
                p_myval = p_myval + 1
                p_myval1 = str(p_myval)
                e3.insert(0,p_val1)
                e4.insert(0,p_myval1)
            

         
            i=i+1
            if(i==5):
                if(p_val>p_myval):
                    l = Label(root4, text="YOU WON! :D", fg="gold", bg="black", font=("Lucida console", 15), width=80,height=2)
                    l.place(x=500,y=600)
                    
                    
                elif(p_val<p_myval):
                    l = Label(root4, text="I WON! :D", fg="gold", bg="black", font=("Lucida console", 15), width=80,height=2)
                    l.place(x=500,y=600)
                    
                else:
                    l = Label(root4, text="TIE! :D", fg="gold", bg="black", font=("Lucida console", 15), width=80,height=2)
                    l.place(x=500,y=600)
                    

                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e4.delete(0,END)
                p_val = 0
                p_myval = 0
                i = 0

                
        else:
            mbox.showerror("Error", "Please enter either stone, paper or scissor!!")
            e1.delete(0,END)
            e2.delete(0,END)
    

    def back(b,e):
        e.withdraw()
        b.deiconify()
    
    b.withdraw()
    root4 = Tk()
    root4.title("Game of trials")
    root4.configure(bg="black")
    root4.state('zoomed')

    f = Frame(root4, bg="white", borderwidth=20, relief=SUNKEN)
    f.pack()

    l = Label(f, text="Stone,paper,scissor", fg="maroon", bg="white", font=("Lucida console", 30), width=60,height=2)
    l.pack()

    l1 = Label(root4, text="Let's start!", fg="Indian red", bg="black", font=("Ink free",30,"bold"), width=60,height=1)
    l1.place(x=100,y=200)
    l1.after(3000, l1.destroy)

    l2 = Label(root4, text="-----Rule-----", fg="gold", bg="black", font=("Lucida console", 15), width=60,height=1)
    l2.place(x=400,y=300)

    l3 = Label(root4, text="Fill either stone,paper or scissor in left box and click ok.", fg="gold", bg="black", font=("Lucida console", 15), width=60,height=1)
    l3.place(x=370,y=350)

    e1 = Entry(root4, font=("Candara", 30), width=8)
    e1.place(x=500, y=400)

    e2 = Entry(root4, font=("Candara", 30), width=8)
    e2.place(x=800, y=400)

    e3 = Entry(root4, font=("Candara", 20),background="black",foreground="white", width=3)
    e3.place(x=550, y=550)

    e4 = Entry(root4, font=("Candara", 20),background="black",foreground="white", width=3)
    e4.place(x=850, y=550)


    b1 = Button(root4, text="back", bg="maroon", fg="black",width=10, overrelief=SUNKEN, font=("Calibri",15),borderwidth=2,command=partial(back,b,root4))
    b1.place(x=600, y=750)

    b2 = Button(root4, text="okay", bg="green", fg="black",width=5, overrelief=SUNKEN, font=("Calibri",15),borderwidth=2,command=partial(turn,root4))
    b2.place(x=715, y=400)

    
    root4.mainloop()


