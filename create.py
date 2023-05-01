import tkinter as tk
from tkinter import messagebox as m
from facerec import facerecg

window = tk.Tk()
window.bind('<Escape>', lambda e: window.quit())
label1 = tk.Label(text="Face recognition")
label1.pack()   
label2 = tk.Label(text="some rules to follow:-")
label3 = tk.Label(text="press p to predict the face")
label4 = tk.Label(text="press p when green rectangle is formed around your face")
"""
label2 = tk.Label("yet to predict")
label2.pack()
label3 = tk.Label("yet to predict")
label3.pack()
"""

def prediting():
    global name
    global confident
    global msg
    name,confident,msg=facerecg()
    label2.config(text="name: "+name)
    label3.config(text=confident)
    label4.config(text=msg)

button1 = tk.Button(window,text='predict',command=prediting)

label2.pack()
label3.pack()
label4.pack()
button1.pack()

window.mainloop()