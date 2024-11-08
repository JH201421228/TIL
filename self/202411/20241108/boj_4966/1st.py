import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def is_disjoint(a, b):
    if b == 1:
        return False

    if a % b:
        return is_disjoint(b, a % b)
    else:
        return True

def B(n):
    for x in G[n]:
        if V[x]:
            continue
        V[x] = 1

        if not C[x] or B(C[x]):
            C[x] = n
            return True

    return False

while True:
    M, N = map(int, input().split())
    if not M and not N:
        break

    b = [0]
    while len(b) < M+1:
        b.extend(map(int, input().split()))

    r = [0]
    while len(r) < N+1:
        r.extend(map(int, input().split()))

    G = [[] for _ in range(M+1)]
    for i in range(1, M+1):
        b_ = b[i]
        for j in range(1, N+1):
            r_ = r[j]
            if is_disjoint(max(b_, r_), min(b_, r_)):
                G[i].append(j)

    ans = 0
    C = [0] * (N+1)
    for i in range(1, M+1):
        V = [0] * (N+1)
        if B(i):
            ans += 1

    print(ans)