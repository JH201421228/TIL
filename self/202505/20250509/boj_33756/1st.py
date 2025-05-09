import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


arr = [888_888_888_888_888_888]

while True:
    temp = arr[-1] // 10
    if temp: arr.append(temp)
    else: break

for _ in range(int(input())):
    N = int(input())
    cnt = 0

    for n in arr:
        cnt += N//n
        N %= n

    if N: print("No")
    else:
        if cnt > 8: print("No")
        else: print("Yes")