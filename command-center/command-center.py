from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('500x350')
GUI.title('Hacking Command Center')


Frame1 = Frame(GUI)
Frame1.place(x = 200, y = 200)

Button1 = ttk.Button(Frame1, text='Check Folder')
Button1.pack(ipadx=15, ipady=10)


GUI.mainloop()