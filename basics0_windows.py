import tkinter
from turtle import bgcolor

#Define window
root = tkinter.Tk()
root.title('Windows Basics')
root.iconbitmap('Thinking.ico')
root.geometry('250x700')
root.resizable(0,1)
root.config(bg='blue')

#Second window
top = tkinter.Toplevel()
top.title('Second Window')
top.config(bg='dark blue')
top.geometry('200x200+500+50')

#Run root window
root.mainloop()