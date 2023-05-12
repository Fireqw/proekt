import tkinter as tk

import decimal as de

import numpy as np

import matplotlib.pyplot as plt

fig, ax = plt.subplots()

root = tk()

root.title('Calcuator funci')

buttons = ((('7', '8', '9', 'y = k / x ',)

          ('4', '5', '6', 'y = x * x',)

          ('1', '2', '3', 'y = 1 / x',)

          ('0', '.', '=', '+',)

          ))

          

activeStr = ''

stack = []

def calculate():

    global stack

    global label

    result = 0

    operand2 =  de(stack.pop())

    operation = stack.pop()

    operand1 = de(stack.pop())

    if operation == '+':

        result = operand1 + operand2

    if operation == 'y = 1 / x':

        result = fig, ax = plt.subplots()

        ax.set_title('График функции')

        ax.set_xlabel('x')

        ax.set_ylabel('y')

        x = np.linspace(-5, 5, 100)

        y = 1 / x

        ax.plot(x, y)

        plt.grid()

        plt.xlabel('ось x', fontsize=14)  

        plt.ylabel('ось y', fontsize=14)

        ax.set_xlabel('ось x')

        ax.set_ylabel('ось y')

        plt.legend()

        plt.show()

    if operation == 'y = k / x':

        result = operand1 / operand2

    if operation == 'y = x * x':

        result = operand1 * operand2

    

label = Label(root, text='0', width=35)

label.grid(row=0, column=0, columnspan=4, sticky="nsew")

button = Button(root, text='CE', command=lambda text='CE': click(text))

button.grid(row=1, column=3, sticky="nsew")

for row in range(4):

    for col in range(4):

        button = Button(root, text=buttons[row][col],

                command=lambda row=row, col=col: click(buttons[row][col]))

        button.grid(row=row + 2, column=col, sticky="nsew")

root.grid_rowconfigure(6, weight=1)

root.grid_columnconfigure(4, weight=1)

root.mainloop()
