import tkinter as tk
from tkinter import *

res = 0
num = 0

def click(value):
    global res, num
    if str(value).isdigit():
        num = num * 10 + value
    elif value == '+':
        res += num
        num = 0
    elif value == '-':
        res -= num
        num = 0
    elif value == '*':
        res *= num
        num = 0
    elif value == '/':
        res /= num
        num = 0

def reset():
    global res, num
    res = 0
    num = 0

def final():
    global res
    print(res)

def on_enter():
    final()

window = Tk()
window.geometry("400x400")
window.title("Calculator")

zero = Button(window, text="0", command=lambda: click(0), width=4, padx=9, pady=5)
zero.place(x=100, y=250)

dot = Button(window, text=". ", command=lambda: click('.'), padx=5, pady=5)
dot.place(x=160, y=250)

one = Button(window, text="1", command=lambda: click(1), padx=5, pady=5)
one.place(x=100, y=220)

two = Button(window, text="2", command=lambda: click(2), padx=5, pady=5)
two.place(x=130, y=220)

three = Button(window, text="3", command=lambda: click(3), padx=5, pady=5)
three.place(x=160, y=220)

four = Button(window, text="4", command=lambda: click(4), padx=5, pady=5)
four.place(x=100, y=190)

five = Button(window, text="5", command=lambda: click(5), padx=5, pady=5)
five.place(x=130, y=190)

six = Button(window, text="6", command=lambda: click(6), padx=5, pady=5)
six.place(x=160, y=190)

seven = Button(window, text="7", command=lambda: click(7), padx=5, pady=5)
seven.place(x=100, y=160)

eight = Button(window, text="8", command=lambda: click(8), padx=5, pady=5)
eight.place(x=130, y=160)

nine = Button(window, text="9", command=lambda: click(9), padx=5, pady=5)
nine.place(x=160, y=160)

plus = Button(window, text="+", command=lambda: click('+'), height=3, padx=5, pady=5, width=1)
plus.place(x=190, y=160)

minus = Button(window, text="-", command=lambda: click('-'), padx=5, pady=3)
minus.place(x=190, y=130)

mul = Button(window, text="*", command=lambda: click('*'), padx=5, pady=3)
mul.place(x=160, y=130)

div = Button(window, text="/", command=lambda: click('/'), padx=5, pady=3)
div.place(x=130, y=130)

C = Button(window, text="C", command=reset, pady=3, width=2)
C.place(x=100, y=130)

equal = Button(window, text="=", command=lambda: click('='), height=3, width=2, pady=3)
equal.place(x=190, y=224)

entry = Entry(window, width=19)
entry.place(x=100, y=100)

window.mainloop()
