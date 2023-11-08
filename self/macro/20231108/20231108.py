from tkinter import *

root = Tk()
root.title("title")
root.geometry('640x480+300+100')
root.resizable(False, False)
btn1 = Button(root, padx=5, pady=10, text='btn1')
btn1.pack()
root.mainloop()