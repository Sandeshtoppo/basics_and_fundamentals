#Lables and pack
import tkinter

#Define window
root = tkinter.Tk()
root.title("Label Basics!")
root.iconbitmap('Thinking.ico')
root.geometry('400x400')
root.resizable(0,0)
root.config(bg='blue')

#Create objects
name_label_1 = tkinter.Label(root, text='Hello, my name is Sandesh.')
name_label_1.pack(padx=5)

name_label_2 = tkinter.Label(root, text='Hello, my name is Sam', font=('Arial',18, 'bold'
))
name_label_2.pack()

name_label_3 = tkinter.Label(root, text=('Hello, my name is paul'), font=('Cambria',10), bg='grey')
name_label_3.pack(padx=10, pady=10)

name_label_4 = tkinter.Label(root, text='Hello, I am stucked', bg='#000000', fg='green')
name_label_4.pack(pady=10,ipadx=50,ipady=20, anchor='w') 
#anchor widgets keeps the label at the left side of the window.
#It gives the padding from label 2 and if we want to give the padding from the label 3 then we have use this one 'name_label_4.pack(pady=(0,10))'.

name_label_5 = tkinter.Label(root, text='Hello, My name is Pat', bg='#ffffff', fg='#123456')
# name_label_5.pack(anchor='e')
name_label_5.pack(fill='both',  expand=True,  padx=5,pady=5) # x only fills in the horizontal directions and y fills in the vetical directions. When we set expand=true it expands in the direction of the given direction. 

#Run the root window's main loop
root.mainloop()