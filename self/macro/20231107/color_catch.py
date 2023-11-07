import pyautogui as pg
import pyperclip as pc
from PIL import ImageGrab
import time

time.sleep(2)
screen = ImageGrab.grab()
print(pg.position())
print(screen.getpixel(pg.position()))
# color_set = screen.getpixel(pg.position())
# print(color_set)
# if color_set == (32, 33, 36):
#     print('good')
