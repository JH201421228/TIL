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


for _ in range(int(input())):
    N, M = map(int, input().split())
    G = [[] for _ in range(101)]
    for _ in range(M):
        temp = list(map(int, input().split()))
        for t in range(temp[0]+1, temp[1]+1):
            for a in temp[3:]:
                G[t].append(a)

    C = [0] * (N+1)
    for i in range(1, 101):
        V = [0] * (N+1)
        B(i)

    isPossible = True
    ans = 0
    for v in C[1:]:
        if not v:
            isPossible = False
            break
        else:
            ans = max(ans, v)

    if isPossible:
        print(ans)
    else:
        print(-1)