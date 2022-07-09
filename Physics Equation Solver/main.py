from subprocess import call
from tkinter import *
root = Tk()
root.title("Physics equation solver")
root.geometry('400x200')
clicked = StringVar()

#function to call user selected method
def sol():
    print(clicked.get())
    if(clicked.get()=="Kinematics Equation Solver"):
        root.destroy()
        call(["python","kinematics.py"])
    elif(clicked.get()=="Energy,Momentum Calculator"):
        root.destroy()
        call(["python","energy_momentum.py"])
    else:
        print('Please select an option')

menu = {"Kinematics Equation Solver","Energy,Momentum Calculator"}        
drop = OptionMenu(root,clicked,*menu)
drop.config(width=50)
drop.pack()
button = Button(root,text="Go",font='bold',bg='green',width=10,command=sol)
button.pack(side=BOTTOM)

root.mainloop()