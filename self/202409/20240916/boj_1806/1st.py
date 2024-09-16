import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


N, S = map(int, input().split())
arr = list(map(int, input().split()))
size = [float('inf')] * N

e, s = 0, 0
ans = float('inf')
temp = arr[s]

while True:
    if temp >= S:
        ans = min(e - s + 1, ans)
        temp -= arr[s]
        s += 1

        if ans == 1:
            break

    else:
        if e == N-1:
            break

        e += 1
        temp += arr[e]

    if s > e:
        break

if ans == float('inf'):
    print(0)
else:
    print(ans)