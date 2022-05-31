from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('500x350')
GUI.title('Hacking Command Center')

button1 = Button(GUI, text='Check Folder')
button1.place(x = 50, y = 200)

button2 = ttk.Button(GUI, text='Check Folder')
button2.place(x = 200, y = 200)



GUI.mainloop()