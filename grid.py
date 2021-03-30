from tkinter import *


root = Tk()

root.title("Hello World!")
root.geometry("400x400")

# Create Button Function
def clicked():
    my_button = Button(root, text="You Clicked Me!")
    my_button.grid(row=2, column=0, columnspan=2)

# Create Labels

my_label = Label(root, text="Hello World!", fg="white", bg="black", font=("Helvetica", 32))
my_label.grid(row=0, column=0, columnspan=2)

my_other_label = Label(root, text="This is my first tkinter project!", relief="groove")
my_other_label.grid(row=1, column=0, sticky=W)

my_third_label = Label(root, text="This is my third label")
my_third_label.grid(row=1, column=1)

#Create Buttons

my_button = Button(root, text="Click Me!", command=clicked)
my_button.grid(row=2, column=0, columnspan=2)

root.mainloop()