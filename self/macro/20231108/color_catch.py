import pyautogui as pg
import pyperclip as pc
from PIL import ImageGrab
import time
from tkinter import *


def color_position():
    time.sleep(2)
    screen = ImageGrab.grab()
    print(pg.position())
    print(screen.getpixel(pg.position()))

    label1 = Label(root, text='x, y 좌표' + str(pg.position()))
    label1.pack()
    label2 = Label(root, text='color' + str(screen.getpixel(pg.position())))
    label2.pack()
    return [pg.position(), screen.getpixel(pg.position())]

root = Tk()
root.title("color&position")
# root.geometry('640x480+300+100')
# root.resizable(False, False)
btn1 = Button(root, padx=3, pady=3, text='2초 후 실행', command=color_position)
btn1.pack()
root.mainloop()

