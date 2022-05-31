from tkinter import *

app = Tk()
app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)

bt1 = Button(app, text='Bt 1', font='Arial 36')
bt2 = Button(app, text='Bt 2', font='Arial 36')
bt3 = Button(app, text='Bt 3', font='Arial 36')
bt4 = Button(app, text='Bt 4', font='Arial 36')
bt5 = Button(app, text='Bt 5', font='Arial 36')
bt6 = Button(app, text='Bt 6', font='Arial 36')

bt1.grid(row=0, column=0, sticky=NSEW)
bt2.grid(row=0, column=1, sticky=NSEW)
bt3.grid(row=0, column=2, sticky=NSEW)
bt4.grid(row=1, column=0, sticky=NSEW)
bt5.grid(row=1, column=1, sticky=NSEW)
bt6.grid(row=1, column=2, sticky=NSEW)

app.mainloop()
