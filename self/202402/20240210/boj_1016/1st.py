import sys
sys.stdin = open('iput.txt')
input = sys.stdin.readline

N, M = map(int, input().split())

def holiday():
    ans = M - N + 1
    check = [0] * (M-N+1)

    i = 2

    while i**2 <= M:
        power = i**2
        if N % power:
            mode = 1
        else:
            mode = 0

        j = N//power + mode

        while power * j <= M:
            if not check[power*j-N]:
                check[power*j-N] = 1
                ans -= 1
            j += 1
        i += 1

    print(ans)
holiday()