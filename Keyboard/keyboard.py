from tkinter import *
from functools import partial
from datetime import datetime
from datetime import date
import time
cu = datetime.now()

all_words = "english_words_479k.txt"

def home():


    def delete():
        notes = text.get("1.0","end")
        text.delete(1.0, END)
        for i in range (len(notes)-2):
            text.insert(END,notes[i])


    def save():
        notes = text.get("1.0", "end")
        date = "%s/%s/%s" % (cu.day, cu.month, cu.year)
        timing = time.strftime('%H:%M:%S')
        file1 = open("notes.txt", "w")
        file1.write("Date-"+date+" Time-"+timing)
        file1.write("\n")
        notes = notes.encode()
        notes = str(notes)
        file1.write(notes)
        file1.close()


    root = Tk()
    root.title("Py-Keyboard")
    root.configure(bg="sandybrown")
    root.state('zoomed')

    fr = Frame(root, bg="brown", borderwidth=20, relief=GROOVE)
    fr.pack()

    la = Label(fr, text="Py-Keyboard", fg="maroon", bg="white", font=("stencil", 30), width=60, height=2)
    la.pack()

    text = Text(root, height=7, width=108,font=("Calibri", 20))
    text.place(x=10, y=150)

    q = Button(root, text="Q", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"Q"))
    q.place(x=50, y=400)

    w = Button(root, text="W", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"W"))
    w.place(x=170, y=400)

    e = Button(root, text="E", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"E"))
    e.place(x=290, y=400)

    r = Button(root, text="R", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"R"))
    r.place(x=410, y=400)

    t = Button(root, text="T", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"T"))
    t.place(x=530, y=400)

    y = Button(root, text="Y", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"Y"))
    y.place(x=650, y=400)

    u = Button(root, text="U", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"U"))
    u.place(x=770, y=400)

    i = Button(root, text="I", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"I"))
    i.place(x=890, y=400)

    o = Button(root, text="O", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"O"))
    o.place(x=1010, y=400)

    p = Button(root, text="P", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"P"))
    p.place(x=1130, y=400)

    s1 = Button(root, text="\U0001f600", bg="orange", fg="black", width=3, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END, "\U0001f600"))
    s1.place(x=1250, y=400)

    s2 = Button(root, text="\U0001f601", bg="orange", fg="black", width=3, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END, "\U0001f601"))
    s2.place(x=1300, y=400)

    s3 = Button(root, text="\U0001f602", bg="orange", fg="black", width=3, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END, "\U0001f602"))
    s3.place(x=1350, y=400)

    s4 = Button(root, text="\U0001f603", bg="orange", fg="black", width=3, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END, "\U0001f603"))
    s4.place(x=1400, y=400)

    s5 = Button(root, text="\U0001f604", bg="orange", fg="black", width=3, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END, "\U0001f604"))
    s5.place(x=1450, y=400)

    a = Button(root, text="A", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"A"))
    a.place(x=50, y=470)

    s = Button(root, text="S", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"S"))
    s.place(x=170, y=470)

    d = Button(root, text="D", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"D"))
    d.place(x=290, y=470)

    f = Button(root, text="F", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"F"))
    f.place(x=410, y=470)

    g = Button(root, text="G", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"G"))
    g.place(x=530, y=470)

    h = Button(root, text="H", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"H"))
    h.place(x=650, y=470)

    j = Button(root, text="J", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"J"))
    j.place(x=770, y=470)

    k = Button(root, text="K", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"K"))
    k.place(x=890, y=470)

    l = Button(root, text="L", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"L"))
    l.place(x=1010, y=470)

    s6 = Button(root, text="\U0001f605", bg="orange", fg="black", width=3, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END, "\U0001f605"))
    s6.place(x=1250, y=470)

    s7 = Button(root, text="\U0001f606", bg="orange", fg="black", width=3, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END, "\U0001f606"))
    s7.place(x=1300, y=470)

    s8 = Button(root, text="\U0001f607", bg="orange", fg="black", width=3, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END, "\U0001f607"))
    s8.place(x=1350, y=470)

    s9 = Button(root, text="\U0001f608", bg="orange", fg="black", width=3, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END, "\U0001f608"))
    s9.place(x=1400, y=470)

    s10 = Button(root, text="\U0001f609", bg="orange", fg="black", width=3, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END, "\U0001f609"))
    s10.place(x=1450, y=470)

    z = Button(root, text="Z", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"Z"))
    z.place(x=50, y=540)

    x = Button(root, text="X", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"X"))
    x.place(x=170, y=540)

    c = Button(root, text="C", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"C"))
    c.place(x=290, y=540)

    v = Button(root, text="V", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"V"))
    v.place(x=410, y=540)

    b = Button(root, text="B", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"B"))
    b.place(x=530, y=540)

    n = Button(root, text="N", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"N"))
    n.place(x=650, y=540)

    m = Button(root, text="M", bg="green", fg="Honeydew2", width=8, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END,"M"))
    m.place(x=770, y=540)

    delete1 = Button(root, text="<---", bg="darkblue", fg="Honeydew2", width=10, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=partial(delete))
    delete1.place(x=890, y=540)

    delete2 = Button(root, text="All Clear", bg="darkblue", fg="Honeydew2", width=10, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.delete(1.0, END))
    delete2.place(x=1030, y=540)

    s11 = Button(root, text="\U0001f610", bg="orange", fg="black", width=3, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END, "\U0001f610"))
    s11.place(x=1250, y=540)

    s12 = Button(root, text="\U0001f611", bg="orange", fg="black", width=3, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END, "\U0001f611"))
    s12.place(x=1300, y=540)

    s13 = Button(root, text="\U0001f612", bg="orange", fg="black", width=3, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END, "\U0001f612"))
    s13.place(x=1350, y=540)

    s14 = Button(root, text="\U0001f613", bg="orange", fg="black", width=3, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END, "\U0001f613"))
    s14.place(x=1400, y=540)

    s15 = Button(root, text="\U0001f614", bg="orange", fg="black", width=3, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END, "\U0001f614"))
    s15.place(x=1450, y=540)

    space = Button(root, text="<Space>", bg="green", fg="Honeydew2", width=70, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=lambda x=text: x.insert(END," "))
    space.place(x=400, y=610)

    s16 = Button(root, text="\U0001f615", bg="orange", fg="black", width=3, overrelief=SUNKEN, font=("Calibri", 15),
                 borderwidth=2, command=lambda x=text: x.insert(END, "\U0001f615"))
    s16.place(x=1250, y=610)

    s17 = Button(root, text="\U0001f616", bg="orange", fg="black", width=3, overrelief=SUNKEN, font=("Calibri", 15),
                 borderwidth=2, command=lambda x=text: x.insert(END, "\U0001f616"))
    s17.place(x=1300, y=610)

    s18 = Button(root, text="\U0001f617", bg="orange", fg="black", width=3, overrelief=SUNKEN, font=("Calibri", 15),
                 borderwidth=2, command=lambda x=text: x.insert(END, "\U0001f617"))
    s18.place(x=1350, y=610)

    s19 = Button(root, text="\U0001f618", bg="orange", fg="black", width=3, overrelief=SUNKEN, font=("Calibri", 15),
                 borderwidth=2, command=lambda x=text: x.insert(END, "\U0001f618"))
    s19.place(x=1400, y=610)

    s20 = Button(root, text="\U0001f619", bg="orange", fg="black", width=3, overrelief=SUNKEN, font=("Calibri", 15),
                 borderwidth=2, command=lambda x=text: x.insert(END, "\U0001f619"))
    s20.place(x=1450, y=610)

    save = Button(root, text="Save Text", bg="brown", fg="Honeydew2", width=15, overrelief=SUNKEN, font=("Calibri", 15),borderwidth=2, command=partial(save))
    save.place(x=700, y=680)



    root.mainloop()

home()
