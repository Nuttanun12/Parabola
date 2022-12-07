import math
import tkinter as tk
from tkinter import Entry
from tkinter import Button
from tkinter import Label
from tkinter import END
from tkinter import Text

root = tk.Tk()
root.geometry("400x400")
root.maxsize(400,400)
root.minsize(400,400)
root.title("การหาความยาวส่วนโค้งพาราโบลา")
Label(root, text="ความกว้างส่วนโค้ง\nพาราโบลา", font='Georgia 13').place(x=20, y=30)
firstnum = Entry(root, width=13, font='Georgia 18 ')
firstnum.place(x=180, y = 30)
Label(root, text="ความสูงส่วนโค้ง\nพาราโบลา", font='Georgia 13').place(x=20, y=100)
secnum = Entry(root, width=13, font='Georgia 18 ')
secnum.place(x=180, y= 100)
Label(root, text="ความยาวส่วนโค้งพาราโบลา", font='Georgia 13').place(x=100, y=200)
result = Text(root, height= 2, width= 26)
result.place(x=90, y=230)

def calculatresult():
    result.delete('1.0', END)
    d = float(firstnum.get())
    h = float(secnum.get())
    b = (d**2)/(8*h)
    e = math.sqrt(1+(d**2)/(16*(h**2)))
    f = math.log((4*h/d)*(e+1))
    g = 2*h
    L = b*((g*e)+f)
    result2 = round(L, 2)
    result.insert(END, result2)

calculate = Button(root, text="Entry", width=10, command= calculatresult).place(x=150, y=160)
root.mainloop()