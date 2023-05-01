
import tkinter as tk
from pathlib import Path
from tkinter import messagebox as m
from facedet import createdataset
window = tk.Tk()
greeting = tk.Label(text="Creating a dataset")
greeting.pack()
label1 = tk.Label(text='Enter roll number')
entry1 = tk.Entry()
label2 = tk.Label(text='Enter Name')
entry2 = tk.Entry()
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
window.bind('<Escape>', lambda e: window.quit())


def create():
    data1 = entry1.get()
    data2 = entry2.get()
    if (data2 == '' or data1 == ''):
            m.showerror(title="no data", message="no message")
    else:
        createdataset(data1, data2)


button1 = tk.Button(window, text="Open Camera", command=create)
button1.pack()
window.mainloop()
