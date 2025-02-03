import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def U(idx):
    while idx < N+1:
        T[idx] += 1
        idx += (idx & -idx)


def S(idx):
    res = 0
    while idx > 0:
        res += T[idx]
        idx -= (idx & -idx)

    return res


N = int(input())
Ns = [[int(input()), i] for i in range(N)]

T = [0] * (N+1)

Ns.sort(reverse=True)

for i in range(N):
    Ns[i][0] = N-i

Ns.sort(key= lambda x:x[1])

for i in range(N):
    print(i + 1 - S(Ns[i][0]))
    U(Ns[i][0])