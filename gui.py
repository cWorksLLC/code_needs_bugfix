from tkinter import *

root = Tk()


class Main:
    def __init__(self):
        root.title("my very cool gui program")
        root.geometry("400x250")
        self.wigets()
        root.mainloop()

    def wigets(self):
        label = Label(root, text="test lable", font="12", pady="10")
        label.pack(side=TOP)
        btn1 = Button(root, text="test button", padx="0", pady="0", font="12",
                      command=self.thing)
        btn1.pack(side=BOTTOM)

    def thing(self):
        print("test")


if __name__ == "__main__":
    Main()
