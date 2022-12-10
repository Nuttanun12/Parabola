import math
import tkinter as tk
from tkinter import Entry
from tkinter import Button
from tkinter import Label
from tkinter import END
from tkinter import Text

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    root.maxsize(400,400)
    root.minsize(400,400)
    root.title("การหาความยาวส่วนโค้งพาราโบลา")
    text1 = Label(root, text="ความกว้างส่วนโค้ง\nพาราโบลา", font='Georgia 13')
    text2 = Label(root, text="ความสูงส่วนโค้ง\nพาราโบลา", font='Georgia 13')
    text3 = Label(root, text="ความยาวส่วนโค้งพาราโบลา", font='Georgia 13')
    text4 = Label(root, text="ระยะโฟกัส c", font='Georgia 13')
    text5 = Label(root, text="ความยาวบนช่วง a", font='Georgia 13')
    firstnum = Entry(root, width=13, font='Georgia 18 ')
    firstnum.place(x=180, y = 30)
    secnum = Entry(root, width=13, font='Georgia 18 ')
    secnum.place(x=180, y= 100)
    result = Text(root, height= 2, width= 26)
    result.place(x=90, y=230)

    def calculatresult1():
        result.delete('1.0', END)
        try:
            d = float(firstnum.get())
            h = float(secnum.get())
            b = (d**2)/(8*h)
            e = math.sqrt(1+(d**2)/(16*(h**2)))
            f = math.fabs(math.log((4*h/d)*(e+1)))
            g = (16*(h**2))/d**2
            L = b*((g*e)+f)
            result.insert(END, L)
        except:
            pass

    def calculatresult2():
        result.delete('1.0', END)
        try:
            c = float(firstnum.get())
            a = float(secnum.get())
            d = math.sqrt((a**2)+((2*c)**2))
            e = (a*d)/((2*c)**2)
            f = math.sqrt((a**2)+((2*c)**2))
            g = math.fabs((f+a)/(2*c))
            h = math.log(g)
            i = (2*c)*((e+h))
            result.insert(END, i)
        except:
            pass
    
    def change1():
        text1.place_forget()
        text2.place_forget()
        calculate1.place_forget()
        text4.place(x=50, y=33)
        text5.place(x=30, y=102)
        calculate2.place(x=150, y=160)
        topage1['state'] = 'normal'
        topage2["state"] = 'disabled'
        firstnum.delete('0', END)
        secnum.delete('0', END)
        result.delete('1.0', END)

    def change2():
        text4.place_forget()
        text5.place_forget()
        calculate2.place_forget()
        text1.place(x=30, y=20)
        text2.place(x=40, y=90)
        calculate1.place(x=150, y=160)
        topage1['state'] = 'disabled'
        topage2["state"] = 'normal'
        firstnum.delete('0', END)
        secnum.delete('0', END)
        result.delete('1.0', END)

    calculate1 = Button(root, text="Entry", width=10, command= calculatresult1)
    calculate2 = Button(root, text="Entry", width=10, command= calculatresult2)
    topage1 = Button(root, text="ใช้ความสูง h หน่วย และความยาวฐาน d หน่วย", width=30, state="disable", command=change2)
    topage1.place(x= 85, y= 300)
    topage2 = Button(root, text="ใช้ระยะโฟกัส c หน่วยบนช่วง(-a,a)", width=30, command=change1)
    topage2.place(x= 85, y= 330)
    text1.place(x=30, y=20)
    text2.place(x=40, y=90)
    text3.place(x=100, y=200)
    calculate1.place(x=150, y=160)

root.mainloop()