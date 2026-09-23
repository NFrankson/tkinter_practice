from tkinter import *

root = Tk()

root.title("Welcome to GeekForGeeks")
# Set geometry (Widthxheight)
root.geometry('350x200')

#adding a label to the root window
lbl = Label(root, text = "Are you a geek?")
lbl.grid()

txt = Entry(root, width=10)
txt.grid(column=1, row=0)


def clicked():
    res = "You wrote " + txt.get()
    lbl.configure(text = res)


btn = Button(root, text = "Click me" ,
             fg = "red", command=clicked)

btn.grid(column=2, row=0)


# Execute tkinter
root.mainloop()