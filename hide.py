from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hello World!")
root.geometry("400x400")
root.iconbitmap('C:/Users/natha/projects/codemy_tkinter_basics/favicon.ico')

# Create Button Function
def clicked():
    global output
    output = Label(root, text=my_entry.get())
    output.pack()


def hide():
    output.pack_forget()

def show():
    output.pack()

def destroy():
    output.destroy()

# Create Labels

my_label = Label(root, text="Enter Your Name:", font=("Helvetica", 18))
my_label.pack()

# Create Entry Widget (Text Input)

my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)

#Create Buttons

my_button = Button(root, text="Click Me!", command=clicked)
my_button.pack(pady=20)

hide_button = Button(root, text="Hide", command=hide)
hide_button.pack(pady=5)

show_button = Button(root, text="Show", command=show)
show_button.pack(pady=5)

destroy_button = Button(root, text="Destroy", command=destroy)
destroy_button.pack(pady=5)

root.mainloop()