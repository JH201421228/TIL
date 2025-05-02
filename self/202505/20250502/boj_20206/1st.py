import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def res_value(a, b, c, x):
    return (-a*x-c) / b

A, B, C = map(int, input().split())
x1, x2, y1, y2 = map(int, input().split())

if B:
    y3, y4 = res_value(A, B, C, x1), res_value(A, B, C, x2)
    y3, y4 = min(y3, y4), max(y3, y4)

    if y3 >= y2 or y4 <= y1: print("Lucky")
    else: print("Poor")
else:
    temp = -C/A

    if temp > x1 and temp < x2: print("Poor")
    else: print("Lucky")