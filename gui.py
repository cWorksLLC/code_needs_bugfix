from tkinter import *
from tkinter import messagebox

def thing(self):
	print("test")

root = Tk()
root.title("my very cool gui programm")
root.geometry("400x250")

label = Label(text="test lable", font="12", pady="10")
label.pack(side=TOP)

btn1 = Button(text="test button", background="#000000", foreground="#ffffff", padx="0", pady="0", font="12", command=thing)
btn1.pack(side=BOTTOM)

root.mainloop()