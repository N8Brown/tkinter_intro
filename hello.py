from tkinter import *


root = Tk()

root.title("Hello World!")
root.geometry("400x400")

my_label = Label(root, text="Hello World!", fg="white", bg="black", font=("Helvetica", 32))
my_label.pack()

my_other_label = Label(root, text="This is my first tkinter project!", relief="groove")
my_other_label.pack(pady=50)

root.mainloop()