from tkinter import *
import random

# main window
root = Tk()
root.configure(bg = 'grey')

result_label = Label(root, text = "Result:    ", font = 16)
result_label.grid(row=2)

# functions

def roll(max):
    result = random.randint(1,max)
    result_label.configure(text = "Result: " + str(result))

# buttons to roll some dice dawg
d4 = Button(text = 'D4', command = lambda: roll(4), font = 16)
d4.grid(row=1)

d6 = Button(text = 'D6', command = lambda: roll(6), font = 16)
d6.grid(row=1, column = 2)

d8 = Button(text = 'D8', command = lambda: roll(8), font = 16)
d8.grid(row=1, column = 3)

d10 = Button(text = 'D10', command = lambda: roll(10), font = 16)
d10.grid(row=1, column = 4)

d12 = Button(text = 'D12', command = lambda: roll(12), font = 16)
d12.grid(row=1, column = 5)

d20 = Button(text = 'D20', command = lambda: roll(20), font = 16)
d20.grid(row=1, column = 6)

d100 = Button(text = 'D100', command = lambda: roll(100), font = 16)
d100.grid(row=1, column = 7)

# main loop
root.mainloop()