# Importing Important packages
import os
from tkinter import *
import tkinter as tk
import sqlite3
import random
from tkinter import ttk
from PIL import Image, ImageTk
from PIL import ImageGrab
from functools import partial
from tkinter import messagebox as mbox
from tkcalendar import *
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from datetime import datetime
from datetime import date
import time

cu = datetime.now()

x = random.randrange(1000, 9999)
#----------------------------------------------------------------------------------------------------------------------------------------------
def aboutus():
    root8 = Tk()
    root8.title("About Us")
    root8.iconbitmap('Railway.ico')
    root8.configure(bg="black")

    f = Frame(root8, height=1300, width=1275, bg="black")
    f.pack()
    m = Message(f, text=''' This python project is made by Hitesh Dhameja, Anuja Shetye, Shubhra Jena and Dinesh Gulabani.
     The project aims at booking railway tickets online for long distance journeys. It is just a demonstration purpose project and hence the station 
     names & ticket cost have been taken randomly! Make sure to give a valid real email id as we are sending real mails regarding bookings. Plz note
      that NO real amount in deducted or refunded. The project is inspired from UTS and IRCTC booking.
     Approximate duration to built it was around 2 months. And yes, do not travel without tickets;)''',
                width=500, font=("Times 10 bold"), fg="white", bg="VioletRed4")
    m.pack()

    root8.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------
#c5 is the mail from login page
# Page for viewing booked ticket
def mybooking(a,c5):

    def this(b):
        b.destroy()
        a.deiconify()

    def ss(b):
        
        #to send ticket over mail
        def screenshot(e):
            image=ImageGrab.grab(bbox=(0,0,2000,1000))
            image.save("PrintTicket.png")
            img=open("PrintTicket.png",'rb').read()
            msg=MIMEImage(img,name=os.path.basename("PrintTicket.png"))
            fromaddress = "Enter valid email id"
            toaddress = c5
            password = "Enter password of that email id"
            msg['From'] = fromaddress
            msg['To'] = toaddress
            msg['Subject'] = "Indian Railway Reservation System - Your E-Ticket "
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddress, password)
            server.send_message(msg)
            server.quit()
            rootss.destroy() 
            mbox.showinfo("Information","Ticket sent to your email")
               
        
        a1 = view_booking.focus()
        b1 = view_booking.item(a1)
        rootss = Tk()
        rootss.title("Ticket")
        rootss.iconbitmap('Railway.ico')
        rootss.state('zoomed')
        rootss.configure(bg="orange")
        ff = Frame(rootss, bg="orange", borderwidth=20, relief=SUNKEN)
        ff.place(x=0, y=0, width=1000, height=1300)

        l32 = Label(ff, text="INDIAN RAILWAYS", fg="turquoise3", bg="maroon", font=("Lucida console", 30),
                  width=54, height=2)
        l32.pack()


        l8 = Label(ff, text="Class", fg="black", bg="IndianRed4", font=("Candara Light", 18, "bold"))
        l8.place(x=100, y=140)
        e8 = Label(ff,text= b1["values"][9], font=("Candara Light", 15), bg="yellow", width=10)
        e8.place(x=100, y=200)

        l6 = Label(ff, text="Ticket Type", fg="black", bg="IndianRed4", font=("Candara Light", 18, "bold"))
        l6.place(x=300, y=140)
        e6 = Label(ff,text= b1["values"][8], font=("Candara Light", 15), bg="yellow", width=8)
        e6.place(x=300, y=200)
        
        l7 = Label(ff, text="Type", fg="black", bg="IndianRed4", font=("Candara Light", 18, "bold"))
        l7.place(x=500, y=140)
        e7 = Label(ff,text=b1["values"][7], font=("Candara Light", 15), bg="yellow", width=5)
        e7.place(x=500, y=200)

        l5 = Label(ff, text="Date of Travel", fg="black", bg="IndianRed4", font=("Candara Light", 18, "bold"))
        l5.place(x=650, y=140)
        e5 = Label(ff,text=b1["values"][6], font=("Candara Light", 15), bg="yellow", width=8)
        e5.place(x=650, y=200)

        l0 = Label(ff, text="Booking Number", fg="black", bg="IndianRed4", font=("Candara Light", 18, "bold"))
        l0.place(x=100, y=300)
        e0 = Label(ff,text=b1["values"][1], font=("Candara Light", 15), bg="yellow", width=13)
        e0.place(x=100, y=360)

        l20 = Label(ff, text="Confirmation", fg="black", bg="IndianRed4", font=("Candara Light", 18, "bold"))
        l20.place(x=400, y=300)
        e20 = Label(ff, text="Confirmed", font=("Candara Light", 15), bg="yellow", width=13)
        e20.place(x=400, y=360)

        l3 = Label(ff, text="From", fg="black", bg="OliveDrab4", font=("Candara Light", 18, "bold"))
        l3.place(x=50, y=420)
        e3 = Label(ff,text=b1["values"][4], font=("Candara Light", 17), bg="yellow", width=35)
        e3.place(x=50, y=480)
        
        l4 = Label(ff, text="To", fg="black", bg="OliveDrab4", font=("Candara Light", 18, "bold"))
        l4.place(x=50, y=550)
        e4 = Label(ff,text=b1["values"][5], font=("Candara Light", 17), bg="yellow", width=35)
        e4.place(x=50, y=610)

        e8 = Label(ff,text=b1["values"][8] + "\nTicket", font=("Bahnschrift Condensed", 25,"bold"), bg="yellow", width=7)
        e8.place(x=1000, y=140)


        l4 = Label(ff, text="Printed at "+time.strftime('%H:%M:%S')+" on "+"%s-%s-%s" % (cu.day, cu.month, cu.year), fg="black", bg="SeaGreen4", font=("Candara Light", 15, "bold"))
        l4.place(x=672, y=610)

        b1 = Button(ff,text="Print",bg="grey82",fg="black",font="ComicSan 15 bold",command=partial(screenshot,rootss))
        b1.place(x=600,y=650)
        rootss.mainloop()

        
    
    #for cancelling booked ticket
    def reject(c5,r,t):
        global y
        global x
        v = str(x)
        z = x/2
        z1 = str(z)
        a1 = view_booking.focus()
        b1 = view_booking.item(a1)
        u1 = b1["values"][1]
        u = str(u1)
        m = b1["values"][2]
        n = str(m)
        j = mbox.askokcancel("DELETION","ARE YOU SURE YOU WANT TO CANCEL BOOKING ? \n\n Your 50% of paid Amount will be deducted on cancellation of Ticket")
        print(j)
        if j == True:
            conn = sqlite3.connect('anuja.db')
            conn.execute('DELETE from book where name=?',(n,))
            conn.commit()
            conn.close()
            body = ''' Your Ticket from ''' + r + ''' to ''' + t + '''\nTicket no: ''' + u + ''' has been Successfully Cancelled. \n As per Rules and Regulations of IndianRailways... 
            \n From the total Amount Paid Rs. ''' + v + ''' only 50% amount will be refunded back. \n The Remaining Amount Rs. ''' + z1 + ''' will be credited back within 48 hours 
            according to IST \n\n Have a good day!!! \n Thank you'''
            body1 = str(body)
            msg = MIMEText(body1)
            fromaddress = "Enter valid email id"
            toaddress = c5
            password = "Enter password of that email id"
            msg['From'] = fromaddress
            msg['To'] = toaddress
            msg['Subject'] = "Indian Railway Reservation System - Cancellation Of Ticket "
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddress, password)
            server.send_message(msg)
            server.quit()
            root7.destroy()
            mybooking(a,c5)
        else:
            pass
        
    conn = sqlite3.connect('anuja.db')
    c = conn.cursor()
    c.execute('SELECT * FROM book where email=?',(c5,))
    row= c.fetchall()
        
    if(len(row)>=1):
        
        a.withdraw()
        root7 = Tk()
        root7.title("My Bookings")
        root7.iconbitmap('Railway.ico')
        root7.state('zoomed')#wxh
        root7.configure(bg="grey50")

        table_frame = Frame(root7, bg="grey50", borderwidth=20, relief=SUNKEN)
        table_frame.place(x=0, y=0, width=1279, height=750)

        hs = Scrollbar(table_frame, orient=HORIZONTAL)
        hs.pack(side=BOTTOM, fill=X)
        vs = Scrollbar(table_frame, orient=VERTICAL)
        vs.pack(side=RIGHT, fill=Y)

        view_booking = ttk.Treeview(table_frame, columns=("email", "tkno", "n", "m", "fd", "td", "dot", "ad", "tt", "ct", "pm"),
                                        xscrollcommand=hs.set, yscrollcommand=vs.set)
        hs.config(command=view_booking.xview)
        vs.config(command=view_booking.yview)
        view_booking.heading("email", text='Email_id')
        view_booking.heading("tkno", text='Ticket_No')
        view_booking.heading("n", text='Name')
        view_booking.heading("m", text='Mobile')
        view_booking.heading("fd", text='From')
        view_booking.heading("td", text='To')
        view_booking.heading("dot", text='Date of Travel')
        view_booking.heading("ad", text='Type')
        view_booking.heading("tt", text='Ticket Type')
        view_booking.heading("ct", text='Class Type')
        view_booking.heading("pm", text='Payment Mode')
        view_booking["show"] = "headings"
        view_booking.pack(fill=BOTH, expand=1)

        view_booking.column("email", width=100)
        view_booking.column("tkno", width=100)
        view_booking.column("n", width=100)
        view_booking.column("m", width=100)
        view_booking.column("fd", width=200)
        view_booking.column("td", width=200)
        view_booking.column("dot", width=100)
        view_booking.column("ad", width=100)
        view_booking.column("tt", width=100)
        view_booking.column("ct", width=100)
        view_booking.column("pm", width=100)
        view_booking["show"] = "headings"

        for r in row:
            view_booking.insert("",tk.END,values=r)

        b1 = Button(root7,text="Cancel",bg="goldenrod4",fg="black",font="ComicSan 15 bold",command=partial(reject,c5,row[0][4],row[0][5]))
        b1.place(x=300,y=584)
        b2 = Button(root7,text="Print Ticket",bg="goldenrod4",fg="black",font="ComicSan 15 bold",command=partial(ss,root7))
        b2.place(x=568,y=584)
        b2 = Button(root7,text="Back",bg="goldenrod4",fg="black",font="ComicSan 15 bold",command=partial(this,root7))
        b2.place(x=861,y=584)
        

        root7.mainloop()
    else:
        mbox.showinfo("Information","No bookings yet.")
        a.deiconify()
        
            
        

#---------------------------------------------------------------------------------------------------------------------------------------------
# Page for booking ticket
def book(a,c5):
    global x
    x1 = str(x) #payment

    # mailing user about his booked ticket status
    def mail(v,n):


        body1 = '''Thanks for Booking with Indian Railway Reservation System . \n\nPayment receieved...Thanks for booking
                    \n We recieved your payment Rs-''' + x1 + ''' through ''' + str(v) + '''\n\nHappy Journey!!!'''
        body = str(body1)
        msg = MIMEText(body)
        fromaddress = "Enter valid email id"
        toaddress = c5
        password = "Enter password of that email id"
        msg['From'] = fromaddress
        msg['To'] = toaddress
        msg['Subject'] = "Indian Railway Reservation System - Ticket Booked Successfully "
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddress, password)
        server.send_message(msg)
        server.quit()
        n.destroy()

    def success(v,n):
        conn = sqlite3.connect('anuja.db')
        c = conn.cursor()
        c.execute('UPDATE book SET payment_type =? WHERE email=?',(x1,c5))
        conn.commit()
        conn.close()
        mbox.showinfo("Payment receieved","Thanks for booking...!!! We recieved your payment Rs: "+ x1 +" through "+str(v)+" .Booking Info have been on your mail.")
        mail(v,n)


    def payment():
        root14 = Tk()
        root14.title("RAILWAY RESERVATION SYSTEM")
        root14.iconbitmap('Railway.ico')
        root14.state('zoomed')
        root14.configure(bg="black")

        f41 = Frame(root14, bg="black", borderwidth=20, relief=SUNKEN)
        f41.pack()

        l41 = Label(f41, text="INDIAN RAILWAY RESERVATION", fg="turquoise4", bg="white", font=("Lucida console", 30),
                  width=60,height=2)
        l41.pack()

        l411 = Label(root14, text="PAYMENT DETAILS :", bg="goldenrod4", fg="white", font="ComicSan 20 bold")
        l411.place(x=100, y=150)
        l4211 = Label(root14, text="Payment Type :", bg="RosyBrown4", fg="white", font=("ComicSan 15 bold", 12))
        l4211.place(x=200, y=300)
        e4110 = ttk.Combobox(root14, font=("ComicSan 10 bold", 12), width=30, state="readonly")
        e4110["values"] = ('Netbanking', 'Debit Card', 'Credit Card')
        e4110.current(0)
        e4110.place(x=370, y=300)
        b413 = Button(root14, text="PAY", fg="white", bg="VioletRed4", relief=RAISED, overrelief=SUNKEN, width=25,
                    height=3,command=partial(success,e4110.get(),root14))
        b413.place(x=600, y=500)


    def this(b):
        b.destroy()
        a.deiconify()

    # Inserting booking details in book table
    def this1(b):
        if e3.get() == e4.get():
            mbox.showerror("Place Error","Source and Destination Cannot be same!!!")


        if datetime.strptime(e5.get(),'%m/%d/%y') <= datetime.strptime('05/03/20','%m/%d/%y') :
            mbox.showwarning("LockDown Decision","Due to lockdown you cannot book ticket before \n 3rd May 2020...")

        else:
            y = random.randrange(1000000, 99999999)
            y1 = str(y)
            nm = e1.get()
            mb = e2.get()
            fr = e3.get()
            to = e4.get()
            d = e5.get()
            ad = e6.get()
            tt = e8.get()
            ct = e9.get()

            try:
                conn1 = sqlite3.connect('anuja.db')
                c1 = conn1.cursor()
                c1.execute('Select * from book')
                ram = c1.fetchall()
                print(ram)
                conn1.commit()
                conn1.close()

                conn = sqlite3.connect('anuja.db')
                c = conn.cursor()
                c.execute('INSERT INTO book VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',(c5, y1, nm, mb, fr, to, d, ad, tt, ct,0))
                c.execute('SELECT * FROM book')
                row=c.fetchall()
                for r in row:
                    print(r)
                conn.commit()
                conn.close()

            except sqlite3.OperationalError as e:
                print(e)
                mbox.showerror("Mismatch found","Invalid Name or Mob No:")

            e1.delete(0, END)
            e2.delete(0, END)
            e3.delete(0, END)
            e4.delete(0, END)
            e5.delete(0,END)
            e6.current(0)
            e8.current(0)
            e9.current(0)
            b.withdraw()
            book(a,c5)



    a.withdraw()
    root4 = Tk()
    root4.title("RAILWAY RESERVATION SYSTEM")
    root4.iconbitmap('Railway.ico')
    root4.state('zoomed')
    root4.configure(bg="black")

    f = Frame(root4, bg="black", borderwidth=20, relief=SUNKEN)
    f.pack()

    l = Label(f, text="INDIAN RAILWAY RESERVATION", fg="turquoise4", bg="white", font=("Lucida console", 30), width=60,
              height=2)
    l.pack()

    l1 = Label(root4, text="BOOKING DETAILS :", bg="goldenrod4", fg="white", font="ComicSan 16 bold")
    l1.place(x=100, y=150)
    l2 = Label(root4, text="Full Name :", bg="RosyBrown4", fg="white", font=("ComicSan 10 bold", 12))
    l2.place(x=455, y=210)
    l3 = Label(root4, text="Mobile No :", bg="turquoise3", fg="white", font=("ComicSan 10 bold", 12))
    l3.place(x=455, y=250)
    l4 = Label(root4, text="Source :", bg="RosyBrown4", fg="white", font=("ComicSan 10 bold", 12))
    l4.place(x=455, y=290)
    l5 = Label(root4, text="Destination :", bg="turquoise3", fg="white", font=("ComicSan 10 bold", 12))
    l5.place(x=455, y=330)
    l6 = Label(root4, text="Date of Travel :", bg="RosyBrown4", fg="white", font=("ComicSan 10 bold", 12))
    l6.place(x=455, y=370)
    l7 = Label(root4, text="Type :", bg="turquoise3", fg="white", font=("ComicSan 10 bold", 12))
    l7.place(x=455, y=410)
    l9 = Label(root4, text="Ticket Type :", bg="RosyBrown4", fg="white", font=("ComicSan 10 bold", 12))
    l9.place(x=455, y=450)
    l10 = Label(root4, text="Class Type :", bg="turquoise3", fg="white", font=("ComicSan 10 bold", 12))
    l10.place(x=455, y=490)


    e1 = Entry(root4, font=("ComicSan 10 bold", 12), width=30)
    e1.place(x=585, y=210)
    e1.focus_set()
    e2 = Entry(root4, font=("ComicSan 10 bold", 12), width=30)
    e2.place(x=585, y=250)
    e3 = ttk.Combobox(root4, font=("ComicSan 10 bold", 12), width=30, state="readonly")
    e3["values"] = ('Goa (Goa Express)', 'West Bengal(Dibru Rajdhani Express)', 'Pune(Nizamuddin Duronto Express)',
                    'Goa(Mandovi Express)', 'Mumbai(Indian Maharaja Deccan)', 'Kanyakumari(Island Express)',
                    'Haryana(Himalayan Queen)', 'Jammu(Jammu Mail)', 'Bangalore(Golden Chariot)',)
    e3.place(x=585, y=290)
    e4 = ttk.Combobox(root4, font=("ComicSan 10 bold", 12), width=30, state="readonly")
    e4["values"] = ('Karnataka (Goa Express)', 'Assam(Dibru Rajdhani Express)', 'New_Delhi(Nizamuddin Duronto Express)',
                    'Mumbai(Mandovi Express)', 'Delhi(Indian Maharaja Deccan)', 'Kerala(Island Express)',
                    'Himachal Pradesh(Himalayan Queen)', 'Udhampur(Jammu Mail)', 'Goa(Golden Chariot)',)
    e4.place(x=585, y=330)
    e5 = DateEntry(root4, font=("ComicSan 10 bold", 12), width=30, year=2020)
    e5.place(x=585, y=370)
    e6 = ttk.Combobox(root4, font=("ComicSan 10 bold", 12), width=30, state="readonly")
    e6["values"] = ('Adult', 'Child')
    e6.current(0)
    e6.place(x=585, y=410)
    e8 = ttk.Combobox(root4, font=("ComicSan 10 bold", 12), width=30, state="readonly")
    e8["values"] = ('Journey', 'Return')
    e8.current(0)
    e8.place(x=585, y=450)
    e9 = ttk.Combobox(root4, font=("ComicSan 10 bold", 12), width=30, state="readonly")
    e9["values"] = ('First Class', 'AC Chair Car', 'AC 3-Tier', 'Sleeper')
    e9.current(0)
    e9.place(x=585, y=490)

    b1 = Button(root4, text=" Book Another Ticket/Proceed for Payment ", fg="white", bg="VioletRed4", relief=RAISED, overrelief=SUNKEN,
                width=40,height=3, command=partial(this1,root4))
    b1.place(x=300, y=600)
    b2 = Button(root4, text="BACK", fg="white", bg="VioletRed4", width=14, relief=RAISED, overrelief=SUNKEN, height=2,
                command=partial(this,root4))
    b2.place(x=1020, y=150)
    b3 = Button(root4, text="FINAL PAYMENT", fg="white", bg="VioletRed4", relief=RAISED, overrelief=SUNKEN, width=20,
                height=3,command=payment)
    b3.place(x=800, y=600)

    root4.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------
# Home page
def home(a, c5): # passing login pg,email from login page

    
    # logout from home page
    def this(b):
        b.destroy()
        login()

    # my profile page
    def this1(b):

        # update profile
        def updation(d,old):
            name=e1.get()
            mob=e2.get()
            pas=e4.get()
            gen=e5.get()
            date=e6.get()

            conn = sqlite3.connect('anuja.db') #Changing the name in user table also if name is changed here
            c = conn.cursor()
            c.execute('UPDATE book SET name=? WHERE name=?',(name,old))
            conn.commit()
            conn.close()

            conn = sqlite3.connect('anuja.db')
            c=conn.cursor()
            c.execute('UPDATE user SET name=?,mobile=?,password=?,gender=?,dob=? WHERE email=?',(name,mob,pas,gen,date,em))
            d.destroy()
            mbox.showinfo("Update","Successfully Updated!!!")
            conn.commit()
            conn.close()


        #view password
        def view(d):
            e4 = Entry(root10, font=("Candara Light", 20), bg="pink", width=10)
            e4.insert(0, row[0][3])
            e4.place(x=618, y=360)
            
            

        em = c5
        conn = sqlite3.connect('anuja.db')
        c = conn.cursor()
        c.execute('SELECT * FROM user where email=?', (em,))
        row = c.fetchall()

        root10 = Tk()
        root10.title("My Profile")
        root10.iconbitmap('Railway.ico')
        root10.state('zoomed')
        root10.configure(bg="black")

        l1 = Label(root10, text="Name :", fg="black", bg="VioletRed4", font=("Candara Light", 20, "bold"))
        l1.place(x=455, y=150)
        l2 = Label(root10, text="Mobile :", fg="black", bg="VioletRed4", font=("Candara Light", 20, "bold"))
        l2.place(x=455, y=220)
        l3 = Label(root10, text="Email :", fg="black", bg="VioletRed4", font=("Candara Light", 20, "bold"))
        l3.place(x=455, y=290)
        l4 = Label(root10, text="Password :", fg="black", bg="VioletRed4", font=("Candara Light", 20, "bold"))
        l4.place(x=455, y=360)
        l5 = Label(root10, text="Gender :", fg="black", bg="VioletRed4", font=("Candara Light", 20, "bold"))
        l5.place(x=455, y=430)
        l6 = Label(root10, text="DOB :", fg="black", bg="VioletRed4", font=("Candara Light", 20, "bold"))
        l6.place(x=455, y=500)

        e1 = Entry(root10, font=("Candara Light", 20), bg="AliceBlue", width=15)
        e1.place(x=618, y=150)
        e1.focus_set()
        e2 = Entry(root10, font=("Candara Light", 20), bg="AliceBlue", width=15)
        e2.place(x=618, y=220)
        e3 = Label(root10,text= row[0][2], font=("Candara Light", 20), bg="AliceBlue", width=30)
        e3.place(x=618, y=290)
        e4 = Entry(root10, font=("Candara Light", 20), bg="AliceBlue", width=10,show="*")
        e4.place(x=618, y=360)
        b1 = Button(root10, text="View Password", width=10,height=1, bg="BlueViolet",fg="black", relief=RAISED, overrelief=SUNKEN,
                  borderwidth=0,command=partial(view,root10))
        b1.place(x=779, y=368)
        e5 = Entry(root10, font=("Candara Light", 20), bg="AliceBlue", width=15)
        e5.place(x=618, y=430)
        e6 = Entry(root10, font=("Candara Light", 20), bg="AliceBlue", width=15)
        e6.place(x=618, y=500)

        b2 = Button(root10, text="EDIT", width=16, height=2, bg="GreenYellow", relief=RAISED, overrelief=SUNKEN,
                  borderwidth=4,command=partial(updation,root10,row[0][0]))
        b2.place(x=571, y=570)

        e1.insert(0, row[0][0])
        e2.insert(0, row[0][1])
        e4.insert(0, row[0][3])
        e5.insert(0, row[0][4])
        e6.insert(0, row[0][5])

        conn.commit()
        conn.close()
        root10.mainloop()
        

    a.destroy()
    root3 = Tk()
    root3.title("RAILWAY RESERVATION SYSTEM")
    root3.iconbitmap('Railway.ico')
    root3.state('zoomed')
    root3.configure(bg="grey50")
    
    f1 = Frame(root3, bg="black", borderwidth=20, relief=SUNKEN)
    f1.pack(side=LEFT, fill=Y, expand=True)
    f2 = Frame(root3, bg="black", borderwidth=20, relief=SUNKEN)
    f2.pack(side=TOP)

    l = Label(f2, text="INDIAN RAILWAY RESERVATION", fg="turquoise3", bg="white",font=("Lucida console",30),
              width=45,height=2)
    l.pack()

    b1 = Button(f1, text="PLAN_MY_JOURNEY", bg="VioletRed4", fg="white", overrelief=SUNKEN, width=20, height=3,
                command=partial(book, root3,c5))
    b1.pack(pady=50)
    b2 = Button(f1, text="MY_BOOKINGS", bg="VioletRed4", fg="white", width=20, overrelief=SUNKEN, height=3,
                command=partial(mybooking,root3,c5))
    b2.pack(pady=50)

    b3 = Button(f1, text="About Us", bg="VioletRed4", fg="white", overrelief=SUNKEN, width=20, height=3, command=aboutus)
    b3.pack(pady=50)

    b4 = Button(f1, text="My Profile", bg="VioletRed4", fg="white", overrelief=SUNKEN, width=20, height=3,
                command=partial(this1,root3))
    b4.pack(pady=50)

    b5 = Button(root3, text="LOGOUT", fg="white", bg="turquoise4", width=20, height=3, command=partial(this, root3))
    b5.place(x=1048, y=132)

### YAHAN IMAGE AYEGA train.jpg AS A BACKGROUND
    raw_image = Image.open("train.jpg")
    raw_image = raw_image.resize((900, 300))
    img = ImageTk.PhotoImage(raw_image)
    img_label = Label(root3, image=img)
    img_label.place(x=450, y=210)
    img_label.pack_propagate(0)

    l2 = Label(root3, text="www.indianrail.gov.in says", bg="grey50", fg="black", font="ComicSan 16 bold")
    l2.place(x=450, y=538)
    l3 = Label(root3, text="""India has some of the most spectacular and unforgettable rail journeys in the world.
          Here you experience a simple way to way to find out everything you need to know in one easy place.
          There's no better way to enjoy India's outback, cities, coastal towns and regional areas in comfort. """, font="Arial 9")
    l3.place(x=450, y=574)



    root3.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------
# Function to open window for first time users..a=root(login),b=root1(signup),cc=root9(confm pg)
def signup(a):
    m1 = random.randrange(1000, 9999)
    mes = str(m1)

    def confirmation(b):

        def otpcheck(cc):
            if mes == ge7.get():
                n = ge1.get()
                m = ge2.get()
                e = ge3.get()
                p = ge4.get()
                g = ge5.get()
                d = ge6.get()

                conn = sqlite3.connect('anuja.db')
                c = conn.cursor()
                c.execute('INSERT INTO user VALUES (?,?,?,?,?,?)', (n, m, e, p, g, d))
                c.execute('SELECT * from user')
                for r in c:
                    print(r)

                conn.commit()
                conn.close()

                mbox.showinfo("Information",
                              "Congrats! " + ge1.get().upper() + " You have successfully registered on " +
                              "%s-%s-%s" % (cu.day, cu.month, cu.year) + " at " + time.strftime('%H:%M:%S'))
                cc.destroy()
                a.deiconify()

            else:
                mbox.showerror('OTP ERROR', 'INVALID OTP ENTERED')

    
        root9 = Tk()
        root9.title("RAILWAY RESERVATION SYSTEM")
        root9.iconbitmap('Railway.ico')
        root9.state('zoomed')
        root9.configure(bg="grey50")

        f11 = Frame(root9, bg="black", borderwidth=20, relief=SUNKEN)
        f11.place(x=0, y=0, width=1279, height=1300)

        g0 = Label(f11, text="INDIAN RAILWAY RESERVATION", fg="dark blue", bg="white", font=("Lucida console", 32),
                  width=60, height=2)
        g0.pack()

        g1 = Label(f11, text='Full Name:', bg="RosyBrown4", fg="white", font=("ComicSan 10 bold",12))
        g1.place(x=200, y=200)
        ge1 = Entry(f11, font=("ComicSan 10 bold",12), width=30)
        ge1.insert(0,e1.get())
        ge1.place(x=370, y=200)

        g2 = Label(f11, text='Mobile No:', bg="turquoise3", fg="white", font=("ComicSan 10 bold",12))
        g2.place(x=200, y=250)
        ge2 = Entry(f11,font=("ComicSan 10 bold",12), width=30)
        ge2.insert(0,e2.get())
        ge2.place(x=370, y=250)

        g3 = Label(f11, text="Email ID: ", bg="RosyBrown4", fg="white", font=("ComicSan 10 bold",12))
        g3.place(x=200, y=300)
        ge3 = Entry(f11,font=("ComicSan 10 bold",12), width=30)
        ge3.insert(0,e3.get())
        ge3.place(x=370, y=300)

        g4 = Label(f11, text="Password: ", bg="RosyBrown4", fg="white", font=("ComicSan 10 bold",12))
        g4.place(x=200, y=350)
        ge4 = Entry(f11, font=("ComicSan 10 bold",12), width=30, show="*")
        ge4.insert(0, e5.get())
        ge4.place(x=370, y=350)

        g5 = Label(f11, text="Gender: ", fg="white", bg="turquoise3", font=("ComicSan 10 bold",12))
        g5.place(x=200, y=400)
        ge5 = Entry(f11,  font=("ComicSan 10 bold",12),width=30)
        ge5.insert(0,e6.get())
        ge5.place(x=370, y=400)

        g6 = Label(f11, text="DOB: ", fg="white", bg="RosyBrown4", font=("ComicSan 10 bold",12))
        g6.place(x=200, y=450)
        ge6 = Entry(f11,  font=("ComicSan 10 bold",12),width=30)
        ge6.insert(0,e_dob.get())
        ge6.place(x=370, y=450)

        g7 = Label(f11, text="ENTER YOUR OTP: ", fg="white", bg="RosyBrown4", font=("ComicSan 10 bold",12))
        g7.place(x=200, y=500)
        ge7 = Entry(f11, font=("ComicSan 10 bold",12),width=30)
        ge7.place(x=370, y=500)

        b123 = Button(f11, text="SUBMIT", width=24,height=3, bg="green", relief=RAISED, overrelief=SUNKEN, borderwidth=6,
                    command=partial(otpcheck,root9))
        b123.place(x=500, y=600)
        
        b.destroy()

        root9.mainloop()

            
    #get otp from mail, add user details to db
    def otp(b):
        
        try:
            body = '''Congratulations for Connecting With Indian Railway Reservation System!!!..... \n Your OTP(One Time Password) is ''' + mes
            msg = MIMEText(body)
            fromaddress = "Enter valid email id"
            toaddress = e3.get()
            password = "Enter password of that email id"
            msg['From'] = fromaddress
            msg['To'] = toaddress
            msg['Subject'] = "Indian Railway Reservation System - Email Verification OTP "
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(fromaddress, password)
            server.send_message(msg)
            mbox.showinfo("Information", "OTP has been sent to your Email-id")
            server.quit()
           
            confirmation(b)
            
            
        except smtplib.SMTPRecipientsRefused:
            mbox.showerror("Invalid Email-id","No such email-id...\n\n Please check your email-id")
            e3.delete(0,END)
        
        
    # back to login page
    def this1(b):
        b.destroy()
        a.deiconify()
        
    #check email repeated? passw matches?..call otp method
    def this(b):

        n = e1.get()
        m = e2.get()
        e = e3.get()
        p = e5.get()
        g = e6.get()
        d = e_dob.get()
        
        conn = sqlite3.connect('anuja.db')
        c = conn.cursor()
        c.execute('SELECT email from user where email=?', (e3.get(),));
        r = c.fetchall()
        
        if e4.get() != e5.get():
            label = Label(f, text="Confirm password doesn't match with password!", bg="maroon", fg="white",
                          font="ComicSan 10 bold")
            label.place(x=700, y=400)
            e4.delete(0, END)
            e5.delete(0, END)
            label.after(4000, label.destroy)

        
        elif len(r) == 1:
            mbox.showerror("Error", "Cannot Register with same email-id again")
            e3.delete(0,END)
            
        else:
            otp(b)
            
    
                    
    a.withdraw()
    root1 = Tk()
    root1.title("RAILWAY RESERVATION SYSTEM")
    root1.iconbitmap('Railway.ico')
    root1.state('zoomed')
    root1.configure(bg="grey50")
    
    f = Frame(root1, bg="black", borderwidth=20, relief=SUNKEN)
    f.place(x=0, y=0, width=1550, height=1500)

    l = Label(f, text="INDIAN RAILWAY RESERVATION", fg="turquoise3", bg="white", font=("Lucida console", 32),
              width=60, height=2)
    l.pack()    

    l1 = Label(f, text='Full Name :', bg="RosyBrown4", fg="white", font=("ComicSan 10 bold", 12))
    l1.place(x=330, y=200)
    e1 = Entry(f, font=("ComicSan 10 bold",12), width=30)
    e1.place(x=510, y=200)
    e1.focus_set()

    l2 = Label(f, text='Mobile No :', bg="turquoise3", fg="white", font=("ComicSan 10 bold", 12))
    l2.place(x=330, y=250)
    e2 = Entry(f, font=("ComicSan 10 bold",12), width=30)
    e2.place(x=510, y=250)

    l3 = Label(f, text="Email ID : ", bg="RosyBrown4", fg="white", font=("ComicSan 10 bold", 12))
    l3.place(x=330, y=300)
    e3 = Entry(f, font=("ComicSan 10 bold",12), width=30)
    e3.place(x=510, y=300)

    l4 = Label(f, text="Password : ", bg="turquoise3", fg="white", font=("ComicSan 10 bold", 12))
    l4.place(x=330, y=350)
    e4 = Entry(f, font=("ComicSan 10 bold",12), width=30, show="*")
    e4.place(x=510, y=350)

    l5 = Label(f, text="Confirm password : ", bg="RosyBrown4", fg="white", font=("ComicSan 10 bold", 12))
    l5.place(x=330, y=400)
    e5 = Entry(f, font=("ComicSan 10 bold",12), width=30, show="*")
    e5.place(x=510, y=400)

    l6 = Label(f, text="Gender : ", fg="white", bg="turquoise3", font=("ComicSan 10 bold", 12))
    l6.place(x=330, y=450)
    e6 = ttk.Combobox(f, font=("ComicSan 10 bold",12), width=10, state="readonly")
    e6["values"] = ('Female', 'Male', 'Others')
    e6.current(0)
    e6.place(x=510, y=450)

    l7 = Label(f, text="DOB : ", fg="white", bg="RosyBrown4", font=("ComicSan 10 bold",12))
    l7.place(x=330, y=500)
    e_dob = DateEntry(f, font=("ComicSan 10 bold",12), width=22, year=2020)
    e_dob.place(x=510, y=500)

    tick = BooleanVar()
    check = Checkbutton(f,font=("ComicSan 10 bold",9), text="I agree the Terms and Conditions (*T&C)", bg="grey75", 
                        variable=tick)
    check.select()
    check.place(x=400, y=560)

    b1 = Button(f, font=("ComicSan 10 bold",11), text="SUBMIT", width=13,height=2, bg="green", relief=RAISED, overrelief=SUNKEN, borderwidth=4,
                command=partial(this,root1))
    b1.place(x=850, y=610)

    b2 = Button(f, text="Back", width=12, bg="green", relief=RAISED, overrelief=SUNKEN, borderwidth=4,height=2,
                    command=partial(this1, root1))
    b2.place(x=1037, y=116)

    
    root1.mainloop()

#------------------------------------------------------------------------------------------------------------------------------------------------
# Login Page
def login():
    
    # Check whether email or password exists
    def check(a):
        e = e1.get()
        p = e2.get()
        conn = sqlite3.connect('anuja.db')
        c = conn.cursor()
        c.execute('SELECT email, password FROM user where email=? and password=?', (e, p,))
        r = c.fetchall()
        if (len(r) == 1):
            e1.delete(0, END)
            e2.delete(0, END)
            home(a,e)
        else:
            mbox.showwarning("Error", "Invalid email or password!!")

        conn.commit()
        conn.close()

    # for forgot password
    def forgot():
        e = e1.get()
        conn = sqlite3.connect('anuja.db')
        c = conn.cursor()
        c.execute('SELECT  password FROM user where email=?', (e,))
        r = c.fetchall()
        if (len(r) == 1):
            mbox.showinfo("Password", r)
        else:
            mbox.showwarning("Error", "Invalid email!!")

        conn.commit()
        conn.close()

    root = Tk()
    root.title("RAILWAY RESERVATION SYSTEM")
    root.iconbitmap('Railway.ico')
    root.state('zoomed')
    
    f = Frame(root, bg="black", borderwidth=20, relief=SUNKEN)
    f.place(x=0, y=0, width=1550, height=1500)

    l = Label(f, text="INDIAN RAILWAY RESERVATION", fg="turquoise3", bg="maroon", font=("Lucida console", 30),
              width=54, height=2)
    l.pack()
    
### YAHAN IMAGE AYEGA abc.jpg BACKGROUND MEI
    
    image = Image.open("abc.jpg")
    image = image.resize((1279, 800))
    photo = ImageTk.PhotoImage(image)
    img_label = Label(f, image=photo)
    img_label.pack()
    img_label.pack_propagate(0)

    l1 = Label(f, text="EMAIL :", bg="grey55", fg="black", font=("ComicSan 10 bold", 17))
    l1.place(x=450, y=310)
    e1 = Entry(f, font=("ComicSan 10 bold", 17), width=28)
    e1.place(x=630, y=310)
    e1.focus_set()

    l2 = Label(f, text="PASSWORD :", bg="grey55", fg="black", font=("ComicSan 10 bold", 17))
    l2.place(x=450, y=370)
    e2 = Entry(f, font=("ComicSan 10 bold", 17), width=28, show="*")
    e2.place(x=630, y=370)

    b1 = Button(f, text="forget password ? ", bg="black", fg="red", overrelief=SUNKEN, font="ComicSan 10 bold",
                borderwidth=0,command=forgot)
    b1.place(x=829, y=435)

    b2 = Button(f, text="SUBMIT", bg="green", width=34, height=2, borderwidth=4, relief=RAISED, overrelief=SUNKEN,
                command=partial(check,root))
    b2.place(x=565, y=530)

    b3 = Button(f, text="DON'T HAVE AN ACCOUNT ? SIGN UP", width=34, height=2, borderwidth=4, relief=RAISED,
                overrelief=SUNKEN, bg="green", command=partial(signup,root))
    b3.place(x=565, y=600)
    l21 = Label(f, text="Copyright © 2020 - www.railway.in. All Rights Reserved ", fg="black", font=("ComicSan 10 bold", 10))
    l21.place(x=800, y=690)
    l22 = Label(f, text="Site best viewed in IE 6 and above" , fg="black",
                font=("ComicSan 10 bold", 10))
    l22.place(x=840, y=730)
    

    root.mainloop()

#-------------------------------------------------------------------------------------------------------------------------------------------
# START
def start():
    root5 = Tk()
    root5.title("RAILWAY RESERVATION SYSTEM")
    root5.iconbitmap('Railway.ico')
    root5.state('zoomed')

    f = Frame(root5, bg="grey86")
    f.place(x=0, y=0, width=2000, height=1300)

###YAHAN IMAGE AYEGA l1.jpg EKDAM TOP LEFT CORNER ME AS THE LOGO

    image = Image.open("l1.jpg")
    image = image.resize((150,112))
    photo = ImageTk.PhotoImage(image)

    l0 = Label(text="Indian Railway Catering and Tourism Corporation Limited\n\nA Government of India Enterprise", bg="coral4", width="370", height="5",
          font=("Arial CYR", 14))
    l0.pack()
    l1 = Label(root5, image=photo)

    l1.place(x=0, y=0)
    Label(text="").pack()
    Label(text="").pack()
    Label(text="Please help Indian railways and Government of India in moving towards a digitized and cashless economy. Eradicate black money ",
          bg="darkgoldenrod", width="300", height="2", font=("Arial CYR", 13)).pack()
    Label(text="").pack()
    Label(text="").pack()


    c = Canvas(root5, height=263, width=400)
    c.pack()

###YAHAN IMAGE AYEGA frontimage.jpg IN THE RECTANGLE SPACE

    img = Image.open("frontpagetrain.jpg")
    img = img.resize((402,272))
    img = ImageTk.PhotoImage(img)
    c.create_image(1, 1, anchor=NW, image=img)
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="").pack()
    Label(text="Experience Our Service...", width="300", height="2", bg="AntiqueWhite4", font=("Arial CYR", 15)).pack()
    Label(text='''India has some of the most spectacular and unforgettable rail journeys in the world.
          Here you experience a simple way to way to find out everything you need to know in one easy place.
          There's no better way to enjoy India's outback, cities, coastal towns and regional areas in comfort.'''
          , width="300", height="4", bg="AntiqueWhite4", font=("Arial CYR", 9)).pack()
    f.pack_propagate(0)

    root5.after(1000, root5.destroy)
    root5.mainloop()

#-----------------------------------------------------------------------------------------------------------------------------------------    
# BEGINS
start()
login()

#-----------------------------------------------------------------------------------------------------------------------------------------
#CREATING DATABASE
# Creating user table in database for storing user details
try:
        conn = sqlite3.connect('anuja.db')
        c = conn.cursor()
        c.execute(
            'CREATE TABLE user (name VARCHAR(30), mobile VARCHAR(10), email VARCHAR(20), password VARCHAR(10), gender VARCHAR(10), dob VARCHAR(10))')
        conn.commit()
        conn.close()
except sqlite3.OperationalError:
        pass


# Creating book table in database
try:
        conn = sqlite3.connect('anuja.db')
        #conn.execute("PRAGMA foreign_keys = 1")
        c = conn.cursor()
        c.execute(
            'CREATE TABLE book(email VARCHAR(30), tkno VARCHAR(20), name VARCHAR(50), mobile VARCHAR(10), from_d VARCHAR(100), to_d VARCHAR(100), dot VARCHAR(10), adult CHAR(2), ticket_type VARCHAR(10), class_type VARCHAR(10), payment_type VARCHAR(10), FOREIGN KEY(name,mobile) REFERENCES user(name, mobile) )')
        conn.commit()
        conn.close()
except sqlite3.OperationalError:
        pass
    

'''
conn = sqlite3.connect('anuja.db')
c = conn.cursor()
c.execute('DROP TABLE IF EXISTS user')
conn.commit()
conn.close()
conn = sqlite3.connect('anuja.db')
c = conn.cursor()
c.execute('DROP TABLE IF EXISTS book')
conn.commit()
conn.close()
'''

