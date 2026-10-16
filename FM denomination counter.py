from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Fast Counter $$$")
root.configure(bg="light grey")
root.geometry("650x400")

upload = Image.open("FC2.png")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg="light grey")
label.palace(x=180, y=20)

label1 = Label(
    root,
    text="Hello user👋! Welcome to our fast denomination counter💵💰$$$"
    bg="light grey"
)
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo(
        "Alert",
        "Do you want to continue? this app may have viruses and malware!"
    )
    MsgBox == "ok":
     topwin()

    Button1 = Button
    