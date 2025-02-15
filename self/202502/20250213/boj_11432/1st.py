import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline


def B(n):
    for x in G[n]:
        if V[x]:
            continue
        V[x] = 1

        if not C[x] or B(C[x]):
            C[x] = n
            return True

    return False


T = int(input())

for z in range(T):
    print(f"Data Set {z+1}:")

    M, N = map(int, input().split())
    G = [[] for _ in range(N+1)]

    V = [0] * (M+1)
    C = [0] * (M+1)

    for idx in range(1, N+1):
        temp = list(map(int, input().split()))
        G[idx].extend(temp[1:])

    ans = 0
    for n in range(1, N+1):
        V = [0] * (M+1)
        if B(n):
            ans += 1

    print(ans)
    print()