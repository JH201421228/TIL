import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
import math

def func(n):
    return S/n
# 만족하는 리스트가 존재하는가?
# 존재한다면
S, P = map(int, input().split())
n_1 = int(S//math.e)
n_2 = n_1 + 1
# print(P**(1/n_1))

if n_1 and func(n_1) >= P**(1/n_1):
    # print(n_1, '보다 작은 값')
    if S == P:
        print(1)
        exit(0)
    start, end = 2, n_1
    while start <= end:
        mid = (start + end) >> 1
        if func(mid) < P**(1/mid):
            start = mid + 1
        else:
            end = mid - 1
    print(start)
elif func(n_2) >= P**(1/n_2):
    print(n_2)
else:
    print(-1)