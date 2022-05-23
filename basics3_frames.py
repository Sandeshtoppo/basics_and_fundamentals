#Frames

from operator import truediv
import tkinter

#Define window
root = tkinter.Tk()
root.title('Frames Basics!')
root.iconbitmap('Thinking.ico')
root.geometry('500x500')
root.config(bg='grey')

#Example of why to use frames

# name_label = tkinter.Label(root, text='Enter your name : ')
# name_label.pack()

# name_button = tkinter.Button(root, text="Submit your name : ")
# name_button.grid(row=0, column=1)

#Define frames
pack_frame = tkinter.Frame(root, bg='red')
grid_frame_1 = tkinter.Frame(root, bg='blue')
grid_frame_2 = tkinter.LabelFrame(root, text='Grid system rules', borderwidth=5)


#Pack frames onto root
pack_frame.pack(fill='both', expand=True)
grid_frame_1.pack(fill='x', expand=True)
grid_frame_2.pack(fill='both', expand=True,padx=10,pady=10 )

#Pack frames
tkinter.Label(pack_frame,text='text').pack()
tkinter.Label(pack_frame,text='text').pack()
tkinter.Label(pack_frame,text='text').pack()

#Grid 1 Layout
tkinter.Label(grid_frame_1, text='text').grid(row=0,column=0)
tkinter.Label(grid_frame_1, text='text').grid(row=1,column=1)
tkinter.Label(grid_frame_1, text='text').grid(row=2,column=2)
# tkinter.Label(grid_frame_1,text='aaaaaaaaaaaaaaaa').grid(row=3,column=2)

#Grid 2 layout 
tkinter.Label(grid_frame_2,text='aaaaaaaaaaaaaaaa').grid(row=0,column=0)

#Run the window's main 
root.mainloop()