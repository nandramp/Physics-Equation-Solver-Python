from tkinter import *

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#F26849')

def change_width(choice):
    choice = variable.get()
    dropdown.config(width=choice)

# width choices available.
width_size = [10, 15, 20, 25, 30]

# setting variable for Integers
variable = IntVar()

# creating widget
dropdown = OptionMenu(
    ws,
    variable,
    *width_size,
    command=change_width
)
# positioning widget
dropdown.pack(expand=True)

# infinite loop 
ws.mainloop()