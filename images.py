from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hello World!")
root.geometry("400x400")
root.iconbitmap('C:/Users/natha/projects/codemy_tkinter_basics/favicon.ico')

# Create Button Function
def clicked():
    my_button = Label(root, text=my_entry.get()).pack()

# Add Images
my_image = ImageTk.PhotoImage(Image.open('app.jpg'))
my_image_label = Label(image=my_image)
my_image_label.pack()


# Create Labels

my_label = Label(root, text="Enter Your Name:", font=("Helvetica", 18))
my_label.pack()

# Create Entry Widget (Text Input)

my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)

#Create Buttons

my_button = Button(root, text="Click Me!", command=clicked)
my_button.pack(pady=20)

root.mainloop()