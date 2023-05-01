import tkinter as tk
from tkinter import messagebox as m
from facedet import createdataset
from facerec import facerecg
from database import datab

win = tk.Tk()
win.geometry("500x500")
win.bind('<Escape>', lambda e: win.quit())
win.title("Face recognition attendance system")
def open():
    f2 = tk.Frame()
    f2.place(x=0,y=0,width=500,height=500)

    greeting = tk.Label(f2,text="Register a student")
    greeting.pack()
    label1 = tk.Label(f2,text='Enter roll number')
    entry1 = tk.Entry(f2)
    label2 = tk.Label(f2,text='Enter Name')
    entry2 = tk.Entry(f2)
    
    def create():
        data1 = entry1.get()
        data2 = entry2.get()
        if (data2 == '' or data1 == ''):
            m.showerror(title="no data", message="Please enter data ")
        else:
            createdataset(data1, data2)
    button1 = tk.Button(f2, text="Open Camera",command=create)
    button2 = tk.Button(f2, text="Home",command=home)
    label1.pack()
    entry1.pack()
    label2.pack()
    entry2.pack()
    
    button1.pack()
    
    button2.pack()
    
def uiforpredict():
    f3= tk.Frame()
    f3.place(x=0,y=0,width=500,height=500)
    label1 = tk.Label(f3,text="Face recognition")
    label1.pack()   
    label2 = tk.Label(f3,text="some rules to follow:-")
    label3 = tk.Label(f3,text="press p to predict the face")
    label4 = tk.Label(f3,text="press p when green rectangle is formed around your face")
    label5 = tk.Label(f3,text="The data will be inserted to database if confidance is greater than 50")
    label2.pack()
    label3.pack()
    label4.pack()
    label5.pack()
    def prediting():
        global name
        global confident
        global msg
        global mass
        name,confident,msg=facerecg()
        if confident > 50:
            mass = datab(name,confident)
        else:
            mass = "The confident is less than 50 so data is not inserted"
        label2.config(text="name: "+name)
        label3.config(text=confident)
        label4.config(text=msg)
        label5.config(text=mass)
    button1 = tk.Button(f3,text='predict',command=prediting)
    button1.pack()
    button2 = tk.Button(f3, text="Home",command=home)
    button2.pack()




def home():
    f1 = tk.Frame()
    f1.place(x=0,y=0,width=500,height=500)
    button1 = tk.Button(f1,text="Register student",command=open)
    button2 = tk.Button(f1,text="Attendance",command=uiforpredict)

    button1.pack()
    button2.pack()
    win.mainloop()

home()