from tkinter import *


root = Tk()

root.title("Hello World!")
root.geometry("400x400")

my_label = Label(root, text="Hello World!", fg="white", bg="black", font=("Helvetica", 32))
my_label.grid(row=0, column=0)

my_other_label = Label(root, text="This is my first tkinter project!", relief="groove")
my_other_label.grid(row=1, column=1)

root.mainloop()