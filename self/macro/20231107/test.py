import pyautogui as pg
import pyperclip as pc
from PIL import ImageGrab
import time


# 처음 화면이 최대화면일때
# 로그인이 되어 있는 상태일때


# print(pg.size())
# box1 = pg.locateOnScreen('chrome.png')
# point1 = pg.center(box1)
# print(point1)
# time.sleep(0.5)
pg.moveTo(459, 1057) # 하단 크롬 좌표
time.sleep(0.5)
pg.click()
time.sleep(1)
# # 크롬 마크 찾아서 실행

# 최대화면 분기점
screen = ImageGrab.grab()
time.sleep(0.5)
pg.moveTo(1802, 56)
time.sleep(0.5)
color_set = screen.getpixel(pg.position())

if color_set == (32, 33, 36): # 최대화면인 상태
    pass
else: # 최대화면으로 만들기
    box2 = pg.locateOnScreen('new.png')
    point2 = pg.center(box2)
    print(point2)
    time.sleep(0.5)
    pg.moveTo(point2[0], point2[1])
    time.sleep(0.5)
    # 실행된 크롬에서 새로고침 찾기
    
    pg.moveRel(300, 0)
    time.sleep(0.5)
    pg.doubleClick()
    time.sleep(0.5)
    # 최대화 하기

box3 = pg.locateOnScreen('image.png')
point3 = pg.center(box3)
print(point3)
pg.moveTo(point3[0], point3[1])
time.sleep(0.5)
pg.moveRel(300, 0)
time.sleep(0.5)
pg.click()
time.sleep(0.5)
# 주소 입력창 클릭하기

pc.copy('https://edu.ssafy.com/')
time.sleep(0.5)
pg.hotkey('ctrl', 'v')
time.sleep(0.5)
pg.press('enter')
time.sleep(0.5)
# 싸피 주소로 이동


# 로그인 여부 분기점
screen = ImageGrab.grab()
time.sleep(0.5)
pg.moveTo(1624, 122)
time.sleep(0.5)
color_set_green = screen.getpixel(pg.position())

if color_set_green == (63, 206, 50): # 이미 로그인 된 상태
    pass
else:
    pg.moveTo(507, 532)
    time.sleep(0.5)
    pg.click()
    time.sleep(0.5)
    pc.copy('') #비밀번호 입력
    time.sleep(0.5)
    pg.hotkey('ctrl', 'v')
    time.sleep(0.5)
    # 비밀번호 입력

    pg.moveTo(640, 669)
    time.sleep(0.5)
    pg.click()
    time.sleep(0.5)
    # 로그인 버튼 클릭

pg.moveTo(649, 379)
time.sleep(0.5)
pg.click()
time.sleep(0.5)
# 퇴실버튼 누르기

pg.moveTo(952, 606)
time.sleep(0.5)
pg.click()
time.sleep(0.5)
# 확인 버튼 누르기

pg.moveTo(1897, 16)
time.sleep(0.5)
pg.click()
time.sleep(0.5)
# 윈도우 종료

pg.moveTo(1897, 16)
time.sleep(0.5)
# pg.click()
# time.sleep(0.5)
# 파이참 종료