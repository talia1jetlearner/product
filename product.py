from tkinter import*
import tkinter as tk
import tkinter.messagebox
import random
number1= random.randint(1,10)
number2= random.randint(1,10)
product=number1*number2
def show_message():
    guessin= guess.get()
    g= int(guessin)
    if g==product:
        tkinter.messagebox.showinfo("correct","Correct! you guessed it. You are a Math Wiz!")
    else:
        tkinter.messagebox.showinfo("wrong","Wrong! The answer was "+ str(product))
def confirm():
    my_name= name.get()
    tkinter.messagebox.showinfo("hello","Hey "+ my_name +" guess the product of "+ str(number1) +" and "+str(number2))

window= Tk()
window.title("Math Wiz")
window.geometry("500x350")
title= Label(window,text="Are you a Math Wiz?",font="Arial 20")
title.place(x=150,y=5)
l_name= Label(window,text="what is your name:")
l_name.place(x=50,y=100)
name= Entry(window)
name.place(x=170,y=100)
ok= Button(window,text="OK",command=confirm)
ok.place(x=310,y=95)
g_label= Label(window,text="Take a guess:")
g_label.place(x=50,y=200)
guess= Entry(window)
guess.place(x=170,y=200)
guess_b= Button(window,text="GUESS",command=show_message)
guess_b.place(x=310,y=195)


window.mainloop()