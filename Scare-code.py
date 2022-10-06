import tkinter as tk
import random
import threading
import time
import os
import tkinter.messagebox
import shutil


def boom():
    window = tk.Tk()
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    a = random.randrange(0, width)
    b = random.randrange(0, height)
    window.title('Hello World')
    window.geometry("200x50" + "+" + str(a) + "+" + str(b))
    tk.Label(window, text='Warning', bg='red',
             font=('宋体', 17), width=20, height=4).pack()
    window.mainloop()

threads = []
for i in range(100):
    os.system('')
    t = threading.Thread(target=boom)
    threads.append(t)
    time.sleep(0.1)
    threads[i].start()
root = tkinter.Tk()
root.withdraw()
root = tkinter.Tk()
root.withdraw()
tkinter.messagebox.showerror('Error', 'The computer is infected with a virus')
from tkinter import messagebox
win1=tk.Tk()
messagebox.showinfo("Warning","Enjoy your last time")
os.system('taskkill /f /im python.exe')