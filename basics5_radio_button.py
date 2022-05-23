#Radio Button
from calendar import c
from cgitb import text
from importlib.metadata import PathDistribution
import numbers
import tkinter
from turtle import width
from tkinter import IntVar


#Define window
root = tkinter.Tk()
root.title('Radio Button Basics!')
root.iconbitmap('Thinking.ico')
root.geometry('350x350')
root.resizable(0,0)
root.config(bg='grey')


#Define functions
def make_label():
    '''Print to the screen'''
    if numbers.get() == 1:
        num_label = tkinter.Label(output_frames,text='1 one 1')
    elif numbers.get() == 2 :
        num_label = tkinter.Label(output_frames, text='2 two 2')
        
    num_label.pack()

#Define frames
input_frames = tkinter.LabelFrame(root, text='This is fun!', width=350, height=100)
output_frames = tkinter.Frame(root, width=350, height=250)
input_frames.pack(padx=10, pady=10)
output_frames.pack(padx=10, pady=(0,10))

 
#Define radion Buttons
numbers = IntVar()
numbers.set(1)

#Create widgets
radio_1 = tkinter.Radiobutton(input_frames, text='Print the number one!', variable=numbers, value=1)
radio_2 = tkinter.Radiobutton(input_frames, text='Print the number two!', variable=numbers, value=2)
print_button = tkinter.Button(input_frames, text='Pirnt the number!', command=make_label)




radio_1.grid(row=0, column=0, padx=10, pady=10)
radio_2.grid(row=0, column=1, padx=10, pady=10)
print_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)






#Run main window's loop
root.mainloop()
