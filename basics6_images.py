#Images
from ctypes import sizeof
import tkinter
from PIL import ImageTk, Image

#Define window
root = tkinter.Tk()
root.title('Image Basics!')
root.iconbitmap('Thinking.ico')
root.geometry('700x700')
root.resizable(0,0)
root.config(bg='light grey')


#Define functions
def make_image():
    '''Print an image'''
    global wep_image
    
    wep_image = ImageTk.PhotoImage(Image.open('weap.jpeg'))
    wep_label = tkinter.Label(root, image=wep_image)
    wep_label.pack(pady=10)


#Basics...works for png

my_image = tkinter.PhotoImage(file='rocket.png')
my_label = tkinter.Label(root, image = my_image)
my_label.pack(pady=10)

my_button = tkinter.Button(root, image=my_image)
my_button.pack(pady=10)

#Not for jpeg
# wep_image = tkinter.PhotoImage(file='weap.jpeg')
# wep_label = tkinter.Label(root, image=wep_image)
# wep_image.pack()

#Using PIL for jpeg
# wep_image = ImageTk.PhotoImage(Image.open('weap.jpeg'))
# wep_label = tkinter.Label(root, image=wep_image)
# wep_label.pack(pady=10)

make_image()

#Run root window's main loop
root.mainloop()