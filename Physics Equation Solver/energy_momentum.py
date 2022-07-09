from cmath import sqrt
import tkinter
import math
from tkinter import *
from subprocess import call

root = Tk()
root.title('Energy,Momentum Calculater')
results_string = StringVar()
results_string.set('RESULTS')

for i in range(9):
    if i < 6:
        Grid.columnconfigure(root, i, weight=1)
    Grid.rowconfigure(root, i, weight=1)

###############################################################################################
# functional code
# function no. 1 to set all the variable to empty string
def clear_values():
    m.delete(0, END)
    v.delete(0, END)
    p.delete(0, END)
    e.delete(0, END)
    # a.delete(0, END)

###############################################################################################
# function no. 2 to set all the known variable in to the known dictionary
def get_known_values():
    known = {}
    if m.get() != '':
        m1 = float(m.get())
        known.update({'m': m1})
    if v.get() != '':
        v1 = float(v.get())
        known.update({'v': v1})
    if p.get() != '':
        p1 = float(p.get())
        known.update({'p': p1})
    if e.get() != '':
        e1 = float(e.get())
        known.update({'e': e1})
    # if a.get() != '':
    #     a1 = float(a.get())
    #     known.update({'a': a1})
    return known

##############################################################################################
# function no. 3 to calculate Mass and set final output into the result_string
def calc_m():
    global results_string
    known = get_known_values()
    if 'm' in known:
        m2 = known['m']
        work = 'm = m...'
        formula = 4
    elif len(known) < 2:
        formula = 0
        work = 'Need at least 2 known values to solve! \nProblem Not Solved!'
        m2 = 0.0
    elif 'p' in known and 'v' in known:
        formula = 1
    elif 'p' in known and 'e' in known:
        formula = 2
    elif 'e' in known and 'v' in known:
        formula = 3
    else:
        print('Something went wrong')
    
    if formula == 1:
        p2 = known['p']
        v2 = known['v']
        m2 = p2/v2
        work = 'm = p/v'
    
    elif formula == 2:
        p2 = known['p']
        e2 = known['e']
        m2 = (p2**2)/(2*e2)
        work = 'm = (p^2)/(2*e)'

    elif formula == 3:
        v2 = known['v']
        e2 = known['e']
        m2 = (2*e2)/(v2**2)
        work = '(2*e)/(v^2)'

    results_string.set(f'{work}\n Mass: {round(m2, 2)} kg')

##############################################################################################
# function no. 4 to calculate Velocity and set final output into the result_string
def calc_v():
    global results_string
    known = get_known_values()
    if 'v' in known:
        v2 = known['v']
        work = 'v = v...'
        formula = 4
    elif len(known) < 2:
        formula = 0
        work = 'Need at least 2 known values to solve! \nProblem Not Solved!'
        v2 = 0.0
    elif len(known) < 2:
        formula = 0
        work = 'Need at least 2 known values to solve! \nProblem Not Solved!'
        v2 = 0.0
    elif 'm' in known and 'p' in known:
        formula = 1
    elif 'p' in known and 'e' in known:
        formula = 2
    elif 'e' in known and 'm' in known:
        formula = 3
    else:
        print('something went wrong')

    if formula == 1:
        m2 = known['m']
        p2 = known['p']
        v2 = p2/m2
        work = 'p/m'

    elif formula == 2:
        p2 = known['p']
        e2 = known['e']
        v2 = 2*e2/p2
        work = '2*e/p'

    elif formula == 3:
        e2 = known['e']
        m2 = known[m]
        v2 = sqrt(2*e2/m2)
        work = '(2*e/m2)^1/2'
        
    results_string.set(f'{work}\n Velocity: {round(v2, 2)} m/sec')

##############################################################################################
# function no. 5 to calculate Momentum and set final output into the result_string
def calc_p():
    global results_string
    known = get_known_values()
    if 'p' in known:
        p2 = known['p']
        work = 'p = p...'
        formula = 4
    elif len(known) < 2:
        formula = 0
        work = 'Need at least 2 known values to solve! \nProblem Not Solved!'
        p2 = 0.0
    elif 'm' in known and 'v' in known:
        formula = 1
    elif 'v' in known and 'e' in known:
        formula = 2
    elif 'e' in known and 'm' in known:
        formula = 3
    else:
        print('Something went wrong')

    if formula == 1:
        m2 = known['m']
        v2 = known['v']
        p2 = m2*v2
        work = 'm*v'
    elif formula == 2:
        v2 = known['v']
        e2 = known['e']
        p2 = 2*e2/v2
        work = '2*e/v'
    elif formula == 3:
        e2 = known['e']
        m2 = known['m']
        p2 = sqrt(2*m2*e2)
        work = '2*m*e'
    results_string.set(f'work:{work}\n Momentum : {round(p2,20)} kg-m/s')

##############################################################################################
# function no. 5 to calculate Energy and set final output into the result_string
def calc_e():
    global results_string
    known = get_known_values()
    if 'e' in known:
        e2 = known['e']
        work = 'e = e...'
    elif 'm' in known and 'v' in known:
        formula = 1
    elif 'v' in known and 'p' in known:
        formula = 2
    elif 'p' in known and 'm' in known:
        formula = 3
    else:
        print('Somthing went wrong!')

    if formula == 1:
        m2 = known['m']
        v2 = known['v']
        e2 = (1/2)*(m2*(v2**2))
        work = '(1/2)*(m*(v^2))'

    elif formula == 2:
        v2 = known['v']
        p2 = known['p']
        e2 = p2*v2/2
        work = 'p*v/2'
    
    elif formula == 3:
        m2 = known['m']
        p2 = known['p']
        e2 = (p2**2)/(2*m2)
        work = '(p^2)/(2*m)'
    
    results_string.set(f'work : {work}\n Energy : {round(e2,2)} jule')

##############################################################################################
# function no. 6 to return back to the main window
def go_back():
    root.destroy()
    call(["python","main.py"])

# code to make GUI interface
label1 = Label(root, text='Enter The Known Variables', font='bold')
label1.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky='NESW')
m_label = Label(root, text='M-mass(kg):')
m_label.grid(row=1, column=0, columnspan=1, padx=10, pady=10, sticky='NESW')
m = Entry(root, borderwidth=5)
m.grid(row=1, column=1, columnspan=5, padx=10, pady=10, sticky='NESW')
v_label = Label(root, text='V-velocity(m/s):')
v_label.grid(row=2, column=0, columnspan=1, padx=10, pady=10, sticky='NESW')
v = Entry(root, borderwidth=5)
v.grid(row=2, column=1, columnspan=5, padx=10, pady=10, sticky='NESW')
p_label = Label(root, text='P-momentum(kg-m/s):')
p_label.grid(row=3, column=0, columnspan=1, padx=10, pady=10, sticky='NESW')
p = Entry(root, borderwidth=5)
p.grid(row=3, column=1, columnspan=5, padx=10, pady=10, sticky='NESW')
e_label = Label(root, text='E-energy(jule):')
e_label.grid(row=4, column=0, columnspan=1, padx=10, pady=10, sticky='NESW')
e = Entry(root, borderwidth=5)
e.grid(row=4, column=1, columnspan=5, padx=10, pady=10, sticky='NESW')
label2 = Label(root, text='Select What To Solve For', font='bold')
label2.grid(row=6, column=0, columnspan=6, padx=10, pady=10, sticky='NESW')
clear_button = Button(root, text='Clear Values', command=clear_values, font='bold')
clear_button.grid(row=7, column=0, columnspan=1, padx=10, pady=10, sticky='NESW')
m_button = Button(root, text='m', command=calc_m, font='bold')
m_button.grid(row=7, column=1, columnspan=1, padx=10, pady=10, sticky='NESW')
v_button = Button(root, text='v', command=calc_v, font='bold')
v_button.grid(row=7, column=2, columnspan=1, padx=10, pady=10, sticky='NESW')
p_button = Button(root, text='p', command=calc_p, font='bold')
p_button.grid(row=7, column=3, columnspan=1, padx=10, pady=10, sticky='NESW')
e_button = Button(root, text='e', command=calc_e, font='bold')
e_button.grid(row=7, column=4, columnspan=1, padx=10, pady=10, sticky='NESW')   
results = Label(root, textvariable=results_string, font='bold')
results.grid(row=8, column=0, columnspan=6, padx=10, pady=10, sticky='NESW')
back = Button(root, text='Back', command=go_back, font='bold')
back.grid(row=9, column=0, columnspan=6, padx=10, pady=10, sticky='NESW')
root.mainloop()