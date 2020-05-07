from tkinter import *
import datetime



root = Tk()
root.title("Age Calculator")


#Input box for name
e = Entry(root, width=35, fg="black")
e.grid(column=1, row=0)



def button():

    l1 = Label(root, text="Hello " + e.get())

    l1.grid(column=3, row=0)





b1 = Button(root, text="Whats your name?:", command=button)

b1.grid(column=0, row=0)


#Input box for birthyear 
e2 = Entry(root, fg="black")

e2.grid(column=1, row=1)





def button2():

    year = datetime.datetime.now().year

    birthyear = e2.get()

    age = int(year)-int(birthyear)

    l2 = Label(root, text=("Your age is:", age), font=30, bg="black", fg="white")

    l2.grid(column=0, row=3)



b2 = Button(root, text="Whats your birthyear?:", command=button2)

b2.grid(column=0, row=1)


root.mainloop()

