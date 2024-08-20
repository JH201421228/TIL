import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


# s, e, i_ 사탕의 맛 번호
# v v번째 맛
# i tree idx
# v_ 개수

def S(s, e, v, i):
    if (s == e):
        return s

    mid = (s+e) // 2
    if tree[2*i] >= v:
        return S(s, mid, v, 2*i)
    else:
        return S(mid+1, e, v-tree[2*i], 2*i+1)


def U(s, e, v_, i_, i):
    if (s > i_ or e < i_):
        return

    tree[i] += v_
    if (s == e):
        return
    mid = (s+e) // 2
    U(s, mid, v_, i_, i*2)
    U(mid+1, e, v_, i_, i*2+1)


N = int(input())
tree = [0] * 4_000_004

for _ in range(N):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        i_ = S(1, 1_000_000, temp[1], 1)
        print(i_)
        U(1, 1_000_000, -1, i_, 1)
    else:
        U(1, 1_000_000, temp[2], temp[1], 1)
