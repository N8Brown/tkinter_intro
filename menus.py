from tkinter import *


root = Tk()
root.title("Hello World!")
root.geometry("400x400")
root.iconbitmap('favicon.ico')

# Menu item functions
def fake_command():
    pass


# Create a menu instance
my_menu = Menu(root)
# Assign the menu to the root window
root.config(menu=my_menu)

# Create a submenu 
file_menu = Menu(my_menu, tearoff=0)
# Add it to the menu
my_menu.add_cascade(label='File', menu=file_menu)
# Add action item to the submenu in the for of a command/function
file_menu.add_command(label='New', command=fake_command)
file_menu.add_command(label='Open', command=fake_command)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

edit_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Copy', command=fake_command)
edit_menu.add_command(label='Cut', command=fake_command)
edit_menu.add_command(label='Paste', command=fake_command)

root.mainloop()