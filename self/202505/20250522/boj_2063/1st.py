import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


for _ in range(int(input())):
    N = int(input())
    arr = list(map(float, input().split()))
    arr.sort()

    flag = False

    while arr:

        arr_max, arr_sum = arr[-1], sum(arr)

        if 2*arr_max <= arr_sum:
            print("YES")
            flag = not flag
            break
        
        arr.pop()

    if flag: continue

    print('NO')
