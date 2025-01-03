import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def merge(s, e):
    if s < e:
        mid = (s+e) >> 1
        merge(s, mid)
        merge(mid+1, e)
        count(arr[s:mid+1], arr[mid+1:e+1], s, e)

def count(X, Y, s, e):
    global ans

    i, j, x, y, cnt = 0, 0, len(X), len(Y), len(X)
    temp = []

    while i < x and j < y:
        if X[i] > Y[j]:
            temp.append(Y[j])
            j += 1
            ans += cnt
        else:
            temp.append(X[i])
            i += 1
            cnt -= 1

    while i < x:
        temp.append(X[i])
        i += 1

    while j < y:
        temp.append(Y[j])
        j += 1

    for idx in range(s, e+1):
        arr[idx] = temp[idx-s]

ans = 0

N = int(input())

temp = list(map(int, input().split()))
arr = list(map(int, input().split()))
T = dict()

for i in range(N):
    T[temp[i]] = i

for i in range(N):
    arr[i] = T[arr[i]]

merge(0, N-1)
print(ans)