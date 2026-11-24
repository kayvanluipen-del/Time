from tkinter import *
from tkinter.ttk import *
from time import strftime

clock_window = Tk()
clock_window.title("Clock")

def time():
    string = strftime("%H:%M:%S:%p")
    time_label.config(text=string)
    time_label.after(1000, time)
time_label = Label(clock_window,font=("calibri",40,"bold"),background="orange",foreground="white")
time_label.pack(anchor="center")

time()
clock_window.mainloop()