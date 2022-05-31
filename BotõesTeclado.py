from tkinter import *


def soma():
    if num['text'] != 10:
        num['text'] += 1
    else:
        pass


def subt():
    if num['text'] != -10:
        num['text'] -= 1
    else:
        pass


mn = Tk()
mn.geometry('300x150+900+200')
mn.grid_rowconfigure(0, weight=1)
mn.grid_columnconfigure(0, weight=1)
mn.grid_columnconfigure(1, weight=1)
mn.grid_columnconfigure(2, weight=1)

num = Label(mn, text=0, font='Arial 20', )
men = Button(mn, text='-', font='Arial 20', background='#db212f', command=subt)
mai = Button(mn, text='+', font='Arial 20', background='#1bca83', command=soma)

men.grid(row=0, column=0, sticky=NSEW)
num.grid(row=0, column=1, sticky=NSEW)
mai.grid(row=0, column=2, sticky=NSEW)

mn.mainloop()
