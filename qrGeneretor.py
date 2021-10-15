# Importing libraries
import qrcode
from tkinter import *
import tkinter as tkr


# Creating the root Window
root = tkr.Tk()
root.title("QR-Code Generator")
root.geometry("500x130")
root.resizable(False, False)
root["background"] = "black"

# Creating Variable for grabbing the input
var = StringVar()


# Generate the QR Code
def generate_QR():
    img = qrcode.make(var.get())
    type(img)
    img.save(var.get() + ".jpg")


# lbl_exception = Label(root, text="Please type a link")
# lbl_exception.place(x=80, y=110)
lbl_Intro = Label(root, text="Please enter the link for the QR Code:", fg="white", bg="black")
lbl_Intro.place(x=5, y=10)
e_Link = Entry(root, borderwidth=0.5, width=45, fg="blue", bg="black", textvariable=var)
e_Link.place(x=210, y=10)
btn_Generate = Button(root, text="Generate", fg="red", bg="black", borderwidth="0", command=generate_QR)
btn_Generate.config(font=("Arial", 20))
btn_Generate.place(x=200, y=50)

tkr.mainloop()
