from tkinter import *
window = Tk()
window.geometry("500x400+10-10")
window.title("my first GUI")
btn1 = Button(text = "Click", fg = "Pink", bg = "Pink")
btn1.place(x=200, y=200)
txtfld = Entry(window,border=2.50)
txtfld.place(x=175, y=150)


lbl = Label(window,text="My first demo")
lbl.place(x=175, y=100)

window.mainloop()