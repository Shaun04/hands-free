from os import link
import tkinter as tk
from tkinter import Entry, Text, Label
from tkinter.constants import END
from maindbscript import *

'''
Version: 1.0
^______^
'''
root = tk.Tk()
root.geometry("550x400")
root.title("Hands free")

def submit():
    try:
        c = TaskCreater()
        c.add_data(date.get(), int(time.get()), title.get(), data.get(), link.get())

    except ValueError:
        print("Time should be an integer")
    
    time.delete(0, END)
    title.delete(0, END)
    data.delete(0, END)
    link.delete(0, END)
    

date = Entry(root, width= 40)
date.grid(row=0, column=1, padx= 20)
time = Entry(root, width= 40)
time.grid(row=1, column=1, padx= 20)
title = Entry(root, width= 40)
title.grid(row=2, column=1, padx= 20)
data = Entry(root, width= 40)
data.grid(row=3, column=1, padx= 20)
link = Entry(root, width= 40)
link.grid(row=4, column=1, padx= 20)

date_label = Label(root, text="Date (Write in the form DD MM YYYY)")
date_label.grid(row=0, column=0, pady=(10, 0))
time_label = Label(root, text="Time (Write in the 24 hour format: HHMM")
time_label.grid(row=1, column=0)
title_label = Label(root, text="Title (For Notification fill both title and data)")
title_label.grid(row=2, column=0)
data_label = Label(root, text="Data")
data_label.grid(row=3, column=0)
link_label = Label(root, text="Link")
link_label.grid(row=4, column=0)


but = tk.Button(root, text="Add data", padx=20,pady=5, command=submit)
but.grid(row=5, column=0, columnspan=2, padx=20,pady=20, ipadx=137)


root.mainloop()
