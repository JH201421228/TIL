import sys
import math
sys.stdin = open('input.txt')
input = sys.stdin.readline

S, P = map(int, input().split())

if S == P:
    print(1)
else:
    max_x1 = math.floor(S / math.e)
    max_x2 = max_x1 + 1

    n = 2
    while n <= max_x2:
        if S % n == 0:  # S를 n으로 나눌 수 있는 경우
            m = S // n  # 나머지 요소
            if n + m == S and n * m == P:  # 합과 곱이 S와 P와 같다면
                print(n)
                break
        n += 1
    else:
        print(-1)